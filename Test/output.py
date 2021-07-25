import fileinput as fi
import sys
import argparse
import random
import string
RvLaLmUwBI = ["False",	"await",	"else",	"import",	"pass",
"None",	"break",	"except",	"in",	"raise",
"True",	"class",	"finally",	"is",	"return",
"and",	"continue",	"for",	"lambda",	"try",
"as",	"def",	"from",	"nonlocal",	"while",
"assert",	"del",	"global",	"not",	"with",
"async",	"elif",	"if",	"or",	"yield"]
jORVmmiejC = string.ascii_letters
FCLRPxSqDU = argparse.ArgumentParser()
FCLRPxSqDU.add_argument('input_file', help = '.py file to have names obfuscated.', type = str)
FCLRPxSqDU.add_argument('input_names', help = '.txt file containing names/symbols to obfuscate', type = str)
glSUGflRgx = FCLRPxSqDU.parse_args()
def main() -> None:
    XoyKQFxwff = generate_obfuscated_symbols()
    for line in read_input_file():
        replace_symbol_in_line(line, XoyKQFxwff)
def replace_symbol_in_line(line: str, MiypUjynoI: dict) -> str:
    oieZHaLfIZ = line
    for symbol in MiypUjynoI:
        oieZHaLfIZ = oieZHaLfIZ.replace(symbol, MiypUjynoI[symbol])
    print(f"New line: {oieZHaLfIZ}")
    pass
def read_input_file() -> list[str]:
    print(f"\nInput file path: {glSUGflRgx.input_file}")
    print(f"Input file content:")  
    ebyYEwsRHo = []
    for line in fi.input(files = glSUGflRgx.input_file):
        print(f"*   {line}", end='')
        if(line.replace('\n', '').strip() == ''):
            continue
        ebyYEwsRHo.append(line.replace('\n', '').strip())
    return ebyYEwsRHo
def generate_obfuscated_symbols() -> dict[str, str]:
    print(f"\nInput names path: {glSUGflRgx.input_file}")
    print(f"Input names:") 
    MiypUjynoI = {}
    for word in fi.input(files = glSUGflRgx.input_names):
        if(' ' in word):
            raise Exception("Names must not contain spaces! Ensure one name per row!") 
        if(word.replace('\n', '') == ''): 
            continue    
        print("*   " + word.replace('\n', ''))
        MiypUjynoI[word.replace('\n', '')] = generate_random_word(10)    
    print(f"\nSymbol_dict: {MiypUjynoI}")
    return MiypUjynoI
def generate_random_word(length: int) -> str:
    return ''.join(random.choice(jORVmmiejC) for i in range(length))
if __name__ == "__main__":
    main()