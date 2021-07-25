import fileinput as fi
import sys
import argparse
import random
import string

keywords = ["False",	"await",	"else",	"import",	"pass",
"None",	"break",	"except",	"in",	"raise",
"True",	"class",	"finally",	"is",	"return",
"and",	"continue",	"for",	"lambda",	"try",
"as",	"def",	"from",	"nonlocal",	"while",
"assert",	"del",	"global",	"not",	"with",
"async",	"elif",	"if",	"or",	"yield"]

allowed_chars = string.ascii_letters

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help = '.py file to have names obfuscated.', type = str)
parser.add_argument('input_names', help = '.txt file containing names/symbols to obfuscate', type = str)

args = parser.parse_args()

def main() -> None:

    obfuscated_symbols = generate_obfuscated_symbols()
    for line in read_input_file():
        replace_symbol_in_line(line, obfuscated_symbols)


def replace_symbol_in_line(line: str, symbol_dict: dict) -> str:
    new_line = line
    for symbol in symbol_dict:
        new_line = new_line.replace(symbol, symbol_dict[symbol])
    print(f"New line: {new_line}")
    pass

    
def read_input_file() -> list[str]:
    print(f"\nInput file path: {args.input_file}")
    print(f"Input file content:")  
    lines = []
    for line in fi.input(files = args.input_file):
        print(f"*   {line}", end='')
        if(line.replace('\n', '').strip() == ''):
            continue
        lines.append(line.replace('\n', '').strip())
    return lines
          
def generate_obfuscated_symbols() -> dict[str, str]:
    print(f"\nInput names path: {args.input_file}")
    print(f"Input names:") 
    symbol_dict = {}
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
    
if __name__ == "__main__":
    main()
