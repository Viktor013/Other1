import re
 
 
number = input("Введите число: ")

m = re.match("[-+]\d+[.]\d+|\d+[.]\d+|[-+]\d+[.]\d+[eE][-+]\d+|\d+[.]\d+[eE][-+]\d+|\d+[eE][-+]\d+|[-+]\d+[eE][-+]\d+", number)

print(m)
    
