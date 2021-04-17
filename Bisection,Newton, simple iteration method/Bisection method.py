import math
from sympy import *
pi=3.141592653589793
e=2.718281828459045

print('Project for "Numerical analysis". under the supervision of Dr. Mahmoud Gamal')
print('by:')
print('\t\tMohamed Yosry ElZarka 19100')
print('\t\tYoussef Mohamed Elsheheimy 19124')
print('\t\tOmar Abd Al-Halim Khalil 19138\n')

print("This is a program to calculate the numerical solution of a non-linear equation using (Bisection method).\n")

print("""
you can use parentheses () in addition to the following mathematical operators:
(+ Add), (- Subtract), (* Multiply), (/ Divide), (% Modulus), (// Floor division), (** Exponent)
you can also use the following constants:
\t pi=3.141592653589793
\t e=2.718281828459045
note: Trigonometric functions sin(x), asin(x), cos(x), acos(x), tan(x), atan(x) 'equivalent of tan-1(x)' use radian values.
      log(x,y)= log(x) / log(y) ,,, ln(x)
""")

while True:
    equation=str(input("Enter the equation: x = Ф(x) = "))
    a=float(eval(input("Enter the start of interval a: ")))
    b=float(eval(input("Enter the  end  of interval b: ")))
    x=a
    fa=round(eval(equation),4)
    x=b
    fb=round(eval(equation),4)
    if fa*fb>=0:
        print("\nThere is no roots in this interval, try again.")
        print("____________________________________________")
        continue
    print("    a         b         c       f(c)")
    i=0
    while True:
        i+=1
        c=round( (a+b)/2 , 4)
        x=c
        fc=round(eval(equation),4)
        x=a
        fa=round(eval(equation),4)
        print(" %.4f |"%a," %.4f |"%b," %.4f |"%c," %.4f "%fc)
        if fc==0: break
        if (fc*fa < 0): 
            b=c
        else:
            a=c
    print("\nAfter",i,"iterations, The root of the function is at x =",c)
    print("\n____________________________________________")
    print("Try another function.")