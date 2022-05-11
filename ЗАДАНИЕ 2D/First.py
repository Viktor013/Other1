import math
 

e = 2.718
z = 3
x = 7
k = 9



def math_task1(x, a, z, y, b):
    pow1 = pow(7+ abs(x - a*z), 1/4)
    pow2 = pow(pow(x, 2)+ 2.25*pow(y, 2), 1/2)+1
    middle = pow1 / pow2
    zero = middle + 0.05*a*b - math.log(pow(b, 2), 3)
    print(zero)


def math_task2(z, x, k):
    EEEE = pow(e, abs(z-1.2)) * pow(1 + math.cos(pow(x, 3)), 2) + pow(math.tan(k*z), 2)
    print(EEEE)


math_task2(z, x, k)


    

    
