# http://www.pythonchallenge.com/pc/def/map.html

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def get_shift_char(char, shift_by=0):
    return chr(ord(char)-shift_by)

def translate_str_by_shifting(str, shift_by=0):
    result = ''
    for letter in str:
        result += get_shift_char(letter, shift_by=shift_by)
    return result

print translate_str_by_shifting(str, -2)

# word 'map' comes from original resolved text (str)
print translate_str_by_shifting('map', -2)


