'''
This code is released under MIT license
'''


def code_to_char(code):
    code_char_mapping_string="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"   
    return code_char_mapping_string[code] 

def char_to_code(char):
    if len(char)==1:
        code_char_mapping_string="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        return code_char_mapping_string.find(char)
    else: 
        raise Exception("Char Input Has to be a Single Character")
        
def calc_checksum_digit(input_string):
    index = 0
    checksum = 0 
    for single_char in input_string.upper():
        multiplier = (index % 2) + 1
        checksum = checksum + (multiplier * char_to_code(single_char)) % 36 \
        + (multiplier * char_to_code(single_char)) // 36
        index=index+1
        return code_to_char((36 - (checksum % 36)) % 36)
 

def main(argv):
    for arg in argv:
        print(arg,"has checksum digit: ",calc_checksum_digit(arg)) 
              
if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
