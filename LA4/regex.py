import re
# regEx function for identifier


def identifier(test_string):
    pattern = '([_][A-Za-z0-9_]+)|([A-Za-z][A-Za-z0-9]*)'

    #test_string = input('enter variable: ')

    result = re.match(pattern, test_string)
    if result:
            #print("Search successful.")
            return True
    else:
            #print("Search unsuccessful.")
            return False


def Comments(word):
    pattern = r'[!!][\s\S]*[!!]'
    if(re.fullmatch(pattern, word)):
        return True
    else:
        return False

#print(identifier('9'))
def DecimalConst(digit):
    #pattern = r'^[-+]?[0-9] *\.[0-9]+$'
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'

    if(re.fullmatch(pattern, digit)):
        return True
    else:
        return False


def integerConst(digit):
    pattern = '[+-]?[0-9]+'

    if(re.fullmatch(pattern, digit)):
        return True
    else:
        return False


def stringConstant(exp):
    #pattern = 'r([\"][\d\D\s\S\W\w]+[\"])'
    pattern = r'"(?:[^\\]|(?:\\.))*"'
    if(re.fullmatch(pattern, exp)):
        return True
    else:
        return False
#print(integerConst('9a'))


def charConstant(c):
    pattern = '(\'.|[^\\[n|s|t|r|\'|\"]]\')'
    #pattern=r'"(.*?)"\s(\d{3})'
    if(re.fullmatch(pattern, c)):
        print("True")
    else:
        print("False")
