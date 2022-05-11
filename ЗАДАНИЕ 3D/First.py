import re
 
 
number = input("Введите число: ")

m = re.match("\1\.\1", number)

print(m)
    
