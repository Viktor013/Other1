# Написать функцию parse_molecule, которая в строке, представляющей из себя молекулярную формулу,
# подмсчитывает количество всех атомов и возвращает результат в виде словаря.
#
# Пример:
# water =
# parse_molecule('H2O') ==> {'H': 2, 'O': 1}
# parse_molecule('Mg(OH)2') ==> {'Mg': 1, 'O: 2, 'H': 2}


import traceback


def parse_molecule(s):
    doublemode = 0
    doubleend = 0
    doublebeginning = 0
    doubletemplenght = 0
    doublemultiplier = 1
    temp = 0
    templenght = 0
    temparray = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
    tempmultiplier = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    beginning = 0
    multiplier = 1
    truemultiplier = 1
    Bill = 1
    Francis = 1
    dictionary2 = {}
    s = list(s)
    lenght = len(s)
    for i in range(0, lenght-1):
        if s[i].islower():
            s[i-1] += s[i]
            s.remove(s[i])
            lenght = len(s)
        if s[i] == ']':
            doublemode = 1
            doubleend = i
            
    if doublemode == 1:
        for i in range(0, lenght-1):
            if s[i].isdigit() and i == 1: 
                dictionary2 = {s[i-1]: int(s[i])}
            if s[i].isdigit() and s[i-1] != ']':
                tempmultiplier[i-1] = int(s[i])
            if s[i-1] == '[':
                doublebeginning = i
                doubletemplenght = i
                while s[i] != ']':
                    if s[i] == '(':
                        beginning = i
                        templenght = i
                        while s[i] != ')':
                            if s[i].isdigit():
                                tempmultiplier[i-1] = int(s[i])
                            temparray[i] = s[i]
                            i += 1
                            templenght += 1
                        multiplier = int(s[i+1])
                        for i in range(beginning, templenght):
                            if not s[i].isdigit():
                                tempmultiplier[i] = tempmultiplier[i] * multiplier
                    if s[i].isdigit() and s[i+1] != ')':
                        tempmultiplier[i-1] = int(s[i])
                    temparray[i] = s[i]
                    i += 1
                    doubletemplenght += 1
                doublemultiplier = int(s[i+1])
                Francis = s.index('O', 0)
                Bill = s.index('O', 5)
                tempmultiplier[Francis] += tempmultiplier[Bill]
                for i in range(doublebeginning, doubletemplenght):
                    if not s[i].isdigit() and s[i] != '(' and s[i] != ')' and s[i] != ']' and i != Bill:
                        truemultiplier = tempmultiplier[i] * doublemultiplier
                        tempdict = dict.fromkeys(temparray[i], truemultiplier)
                        dictionary2.update(tempdict)
                multiplier = 1
                print(dictionary2)
        
        return dictionary2


    else:
        for i in range(0, lenght-1):
            if not s[i].isdigit() and not s[i+1].isdigit() and i == 0:
                dictionary2 = {s[i]: multiplier}
            if s[i].isdigit() and s[i-1] != ')' and s[i+1] != ')' and s[i-1] != ']' and s[i+1] != ']':
                multiplier = int(s[i])
                tempdict = dict.fromkeys(s[i-1], multiplier)
                dictionary2.update(tempdict)
                multiplier = 1
            if s[i-1] == '(':
                beginning = i
                templenght = i
                while s[i] != ')':
                    if s[i].isdigit():
                        tempmultiplier[i-1] = int(s[i])
                    temparray[i] = s[i]
                    i += 1
                    templenght += 1
                multiplier = int(s[i+1])
                for i in range(beginning, templenght):
                    if not s[i].isdigit():
                        truemultiplier = tempmultiplier[i] * multiplier
                        tempdict = dict.fromkeys(temparray[i], truemultiplier)
                        dictionary2.update(tempdict)
                multiplier = 1
        if not s[-1].isdigit():
            tempdict = dict.fromkeys(s[-1], multiplier)
            dictionary2.update(tempdict)
        print(dictionary2)
        
        return dictionary2


# Тесты
try:
    assert parse_molecule("H2O") == {'H': 2, 'O': 1}
    assert parse_molecule("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
    assert parse_molecule("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
