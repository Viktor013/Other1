# Написать функцию scramble, которая получает две строки и определяет: 
# можно ли из букв первой строки перестановкой получить второе слово.
#
# Примеры:
# scramble('rkqodlw', 'world') ==> True

import traceback


def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    lenght1 = len(s1)
    lenght2 = len(s2)
    tail = 0
    for i in range(0, lenght1):
        for temp in range(0, lenght2):
            if s1[i] == s2[temp]:
                tail += 1
                s2[temp] = 0
    print(tail)
    if tail == lenght2:
        conclusion = True
    else:
        conclusion = False
    print(conclusion)
                
        

    
    return conclusion 


# Тесты
try:
    assert scramble('rkqodlw', 'world') ==  True
    assert scramble('cedewaraaossoqqyt', 'codewars') == True
    assert scramble('katas', 'steak') == False
    assert scramble('scriptjava', 'javascript') == True
    assert scramble('scriptingjava', 'javascript') == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
