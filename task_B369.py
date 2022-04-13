# Написать функцию parse_molecule, которая в строке, представляющей из себя молекулярную формулу,
# подмсчитывает количество всех атомов и возвращает результат в виде словаря.
#
# Пример:
# water =
# parse_molecule('H2O') ==> {'H': 2, 'O': 1}
# parse_molecule('Mg(OH)2') ==> {'Mg': 1, 'O: 2, 'H': 2}


import traceback


def parse_molecule(s):
    s = list(s)
    lenght = len(s)
    for i in range(0, lenght-1):
        if s[i].islower():
            s[i-1] += s[i]
            s.remove(s[i])
    
    print(s)
        
            

    
    return 1


# Тесты
try:
#    assert parse_molecule("H2O") == {'H': 2, 'O': 1}
    assert parse_molecule("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
#    assert parse_molecule("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
