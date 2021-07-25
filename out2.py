import fileinput as fi
import sys
import argparse
import random
import string

ZchvZjPZtD = ["False",	"await",	"else",	"import",	"pass",
"None",	"break",	"except",	"in",	"raise",
"True",	"class",	"finally",	"is",	"return",
"and",	"continue",	"for",	"lambda",	"try",
"as",	"def",	"from",	"nonlocal",	"while",
"assert",	"del",	"global",	"not",	"with",
"async",	"elif",	"if",	"or",	"yield"]

yYTmCNZJrN = string.ascii_letters

kyFKxiBEbj = argparse.ArgumentParser()
kyFKxiBEbj.add_argument('input_file', help = '.py file to have names obfuscated.', type = str)
kyFKxiBEbj.add_argument('input_names', help = '.txt file containing names/symbols to obfuscate', type = str)

FIOVpLEuGd = kyFKxiBEbj.parse_args()

def main() -> None:

    bVjqJlPEbz = lNuhWirNUs()
    for DvkiAiBxPZ in ovTGUrcwLg():
        PskHRiLGoW(DvkiAiBxPZ, bVjqJlPEbz)

def PskHRiLGoW(DvkiAiBxPZ: str, fjkCWjdlpJ: dict) -> str:
    UEwPODBnyl = DvkiAiBxPZ
    for XzoOfFIgGI in fjkCWjdlpJ:
        UEwPODBnyl = UEwPODBnyl.replace(XzoOfFIgGI, fjkCWjdlpJ[XzoOfFIgGI])
    print(f"New DvkiAiBxPZ: {UEwPODBnyl}")
    pass
    
def ovTGUrcwLg() -> list[str]:
    print(f"\nInput file path: {FIOVpLEuGd.input_file}")
    print(f"Input file content:")  
    MKCptnOIvk = []
    for DvkiAiBxPZ in fi.input(files = FIOVpLEuGd.input_file):
        print(f"*   {DvkiAiBxPZ}", end='')
        if(DvkiAiBxPZ.replace('\n', '').strip() == ''):
            continue
        MKCptnOIvk.append(DvkiAiBxPZ.replace('\n', '').strip())
    return MKCptnOIvk
          
def lNuhWirNUs() -> dict[str, str]:
    print(f"\nInput names path: {FIOVpLEuGd.input_file}")
    print(f"Input names:") 
    fjkCWjdlpJ = {}
    for word in fi.input(files = FIOVpLEuGd.input_names):
        if(' ' in word):
            raise Exception("Names must not contain spaces! Ensure one name per row!") 
        if(word.replace('\n', '') == ''): 
            continue    
        print("*   " + word.replace('\n', ''))
        fjkCWjdlpJ[word.replace('\n', '')] = generate_random_word(10)    
    print(f"\nSymbol_dict: {fjkCWjdlpJ}")
    return fjkCWjdlpJ
    

def generate_random_word(length: int) -> str:
    return ''.join(random.choice(yYTmCNZJrN) for i in range(length))
    
if __name__ == "__main__":
    main()