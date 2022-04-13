# Написать функцию valid_ISBN10, которая получает строку (ISBN-номер) и проверяет ее на правильность. 
# ISBN-номер состоит из 10 знаков, Первые девять - цифры от 0 до 9. Последний знак - цифры от 0 до 9 или 'X' для обозначения 10.
# ISBN-номер валидный, если сумма произведений цифр на их позицию, взятая по остатку от деления на 11 дает 0.
#
# Примеры:
# valid_ISBN10('1112223339') ==> True 
# 
# ISBN     : 1 1 1 2 2 2 3 3 3  9
# позиция  : 1 2 3 4 5 6 7 8 9 10
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0 ==> True

import traceback


def valid_ISBN10(isbn):
    a = 0
    isbn = list(isbn)
    lenght = len(isbn)
    for i in range(0, lenght-1):
        if not isbn[i].isdigit():
            print("False")
            return False
        b = int(isbn[i])
        c = i+1
        a += b * c
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    c = lenght
    isbn[-1] = int(isbn[-1])
    a += isbn[-1] * c    
    d = lenght + 1
    final = a%d
    if final == 0:
        conclusion = True
    else:
        conclusion = False
    print(conclusion)
    
    
    return conclusion


# Тесты
try:
    assert valid_ISBN10('1112223339') == True
    assert valid_ISBN10('048665088X') == True
    assert valid_ISBN10('1293000000') == True
    assert valid_ISBN10('1234554321') == True
    assert valid_ISBN10('1234512345') == False
    assert valid_ISBN10('1293') == False
    assert valid_ISBN10('X123456788') == False
    assert valid_ISBN10('ABCDEFGHIJ') == False
    assert valid_ISBN10('XXXXXXXXXX') == False    
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
