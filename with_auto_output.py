import fileinput as fi
import sys
import argparse
import random
import string
ZJGSozcksW = ["False",	"await",	"else",	"import",	"pass",
"None",	"break",	"except",	"in",	"raise",
"True",	"class",	"finally",	"is",	"return",
"and",	"continue",	"for",	"lambda",	"try",
"as",	"def",	"from",	"nonlocal",	"while",
"assert",	"del",	"global",	"not",	"with",
"async",	"elif",	"if",	"or",	"yield"]
YUTquFBZeJ = string.ascii_letters
yYfDeytEfz = argparse.ArgumentParser()
yYfDeytEfz.add_argument('input_file', help = '.py file to have names obfuscated.', type = str)
yYfDeytEfz.add_argument('input_names', help = '.txt file containing names/symbols to obfuscate', type = str)
BfhloHTqXa = yYfDeytEfz.parse_args()
def main() -> None:
    dpSBulNgrj = generate_obfuscated_symbols()
    for line in read_input_file():
        replace_symbol_in_line(line, dpSBulNgrj)
def replace_symbol_in_line(line: str, fVYWfQKQuP: dict) -> str:
    yUvLidzguQ = line
    for symbol in fVYWfQKQuP:
        yUvLidzguQ = yUvLidzguQ.replace(symbol, fVYWfQKQuP[symbol])
    print(f"New line: {yUvLidzguQ}")
    pass
def read_input_file() -> list[str]:
    print(f"\nInput file path: {BfhloHTqXa.input_file}")
    print(f"Input file content:")  
    oZQipsMwDR = []
    for line in fi.input(files = BfhloHTqXa.input_file):
        print(f"*   {line}", end='')
        if(line.replace('\n', '').strip() == ''):
            continue
        oZQipsMwDR.append(line.replace('\n', '').strip())
    return oZQipsMwDR
def generate_obfuscated_symbols() -> dict[str, str]:
    print(f"\nInput names path: {BfhloHTqXa.input_file}")
    print(f"Input names:") 
    fVYWfQKQuP = {}
    for word in fi.input(files = BfhloHTqXa.input_names):
        if(' ' in word):
            raise Exception("Names must not contain spaces! Ensure one name per row!") 
        if(word.replace('\n', '') == ''): 
            continue    
        print("*   " + word.replace('\n', ''))
        fVYWfQKQuP[word.replace('\n', '')] = generate_random_word(10)    
    print(f"\nSymbol_dict: {fVYWfQKQuP}")
    return fVYWfQKQuP
def generate_random_word(length: int) -> str:
    return ''.join(random.choice(YUTquFBZeJ) for i in range(length))
if __name__ == "__main__":
    main()