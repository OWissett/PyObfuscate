import fileinput as fi
import sys
import argparse
import random
import string
import re

keywords = ["False",	" await ",	"else",	"import",	"pass",
"None",	"break",	"except",	"in",	"raise",
"True",	"class",	"finally",	"is",	"return",
"and",	"continue",	"for",	"lambda",	"try",
"as",	"def",	"from",	"nonlocal",	"while",
"assert",	"del",	"global",	"not",	"with",
"async",	"elif",	"if",	"or",	"yield"]

allowed_chars = string.ascii_letters

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help = '.py file to have names obfuscated.', type = str)
parser.add_argument('--input_names', help = '.txt file containing names/symbols to obfuscate', type = str)
parser.add_argument('outfile', help = 'Name of the output file', type = str)

args = parser.parse_args()

def main() -> None:

    output_list = []
    obfuscated_symbols = generate_obfuscated_symbols()
    
    for line in read_input_file():  
        if (line.strip() == ''):
            continue
        obfuscated_line = obfuscate_line(line, obfuscated_symbols)
        output_list.append(obfuscated_line)

    with open(args.outfile, "w") as outfile:
        outfile.write('\n'.join(output_list))
    
def autodetect_symbols(line: str) -> list[str]:
    symbols = []
    # Do some regex magic
    regex_pattern_function_def = r"(?<=def )(.)*(?=\()"

    # Find function symbol - only one per line
    function_symbol = re.findall(regex_pattern_function_def, line) # Only one function can be defined per line
    if(len(function_symbol) != 0):
        symbols.extend(function_symbol)

    # TODO: Implement parameter symbol detection
    # Find all function parameters for each 
    #regex_pattern_function_params = r"(?<=def %s\()(.)*(?=\))" % function_symbol # This will match the full string of parameters (e.g. not separately)
    #param_string = re.findall(regex_pattern_function_params, line)

    # Find variable symbols
    regex_pattern_gvariables = r"(?<=^)[a-zA-Z0-9_]*(?= {0,2}\=)"
    gvariable_symbols = re.findall(regex_pattern_gvariables, line.strip())
    if(len(gvariable_symbols) != 0):
        symbols.extend(gvariable_symbols)

    # Find library aliases
    regex_pattern_lib       = r"(?<=import) (.)*$"
    regex_pattern_lib_alias = r"(?<=as )(.)*$"
    lib_alias = re.findall(regex_pattern_lib_alias, re.findall(regex_pattern_lib, line.strip()))
    if(len(lib_alias) != 0):
        symbols.extend(lib_alias)
        
    return symbols

def obfuscate_line(line: str, symbol_dict: dict) -> str:
    new_line = line
    for symbol in symbol_dict:
        if(symbol in keywords):
            continue

        regex_pattern_sol = r"(^)%s(?!(_|[a-zA-Z0-9]))" % (symbol.strip()) # This pattern should match only the symbol at start of line (sol) or after an opening bracket
        regex_pattern     = r"\s%s(?!(_|[a-zA-Z0-9]))" % (symbol.strip()) # matches symbol when in-line and is preceded with whitespace
        regex_pattern_after_bracket = r"(\()%s(?!(_|[a-zA-Z0-9]))" % (symbol.strip())
        regex_pattern_after_cbracket = r"(\{)%s(?!(_|[a-zA-Z0-9]))" % (symbol.strip())
        regex_pattern_after_sbracket = r"(\[)%s(?!(_|[a-zA-Z0-9]))" % (symbol.strip())
        regex_pattern_comments = r"\s#(.)*$"

        #if(re.match(regex_pattern_sol, line) != None):
        new_line = re.sub(regex_pattern_sol, symbol_dict[symbol], new_line)
        new_line = re.sub(regex_pattern, " " + symbol_dict[symbol], new_line)  
        new_line = re.sub(regex_pattern_after_bracket, "(" + symbol_dict[symbol], new_line)
        new_line = re.sub(regex_pattern_after_cbracket, "{" + symbol_dict[symbol], new_line)
        new_line = re.sub(regex_pattern_after_sbracket, "[" + symbol_dict[symbol], new_line)   
        new_line = re.sub(regex_pattern_comments,"", new_line)   
        
    return new_line
    
def read_input_file() -> list[str]:
    print(f"\nInput file path: {args.input_file}")
    print(f"Input file content:")  
    lines = []
    for line in fi.input(files = args.input_file):
        print(f"*   {line}", end='')
        lines.append(line.replace('\n', ''))
    return lines
          
def generate_obfuscated_symbols() -> dict[str, str]:

    symbol_dict = {}
    if(args.input_names == None):
        print("No names provided. Automatic detection will be attempted.")
        for line in read_input_file():  
            if (line.strip() == ''): # Skip whitespace only lines
                continue
            symbols_in_line = autodetect_symbols(line)
            for symbol in symbols_in_line:
                if symbol in symbol_dict:
                    continue
                else:
                    symbol_dict[symbol] = generate_random_word(10)
        print(symbol_dict)
    else:
        print(f"\nInput names path: {args.input_file}")
        print(f"Input names:") 
        for word in fi.input(files = args.input_names):
            if(' ' in word):
                raise Exception("Names must not contain spaces! Ensure one name per row!") 
            if(word.replace('\n', '') == ''): 
                continue    
            print("*   " + word.replace('\n', ''))
            symbol_dict[word.replace('\n', '')] = generate_random_word(10)    
        print(f"\nSymbol_dict: {symbol_dict}")
    return symbol_dict

def generate_random_word(length: int) -> str:
    return ''.join(random.choice(allowed_chars) for i in range(length))
    
def generate_junk() -> str:
    return ""

if __name__ == "__main__":
    main()
