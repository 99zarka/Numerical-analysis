import math
from sympy import *
pi=3.141592653589793
e=2.718281828459045

print('Project for "Numerical analysis". under the supervision of Dr. Mahmoud Gamal')
print('by:')
print('\t\tMohamed Yosry ElZarka 19100')
print('\t\tYoussef Mohamed Elsheheimy 19124')
print('\t\tOmar Abd Al-Halim Khalil 19138\n')

print("This is a program to calculate the numerical solution of a non-linear equation using (simple iteration method).\n")

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
    x0=float(eval(input("Enter x0 = ")))
    x = Symbol('x')
    x_list=[x0]
    equation_derivative= diff(equation,x)
    print("\nФ'(x)= ",equation_derivative)
    del x #because We will need it as a float value not as a symbol
    x=x0
    test= eval( str(equation_derivative) )
    if abs(test)>=1:
        print("\nThe function failed the test and diverges.\n\t |Ф'(x)| = {} > 1 ".format(test))
    else:
        for i in range(1,200): #maximum number of iterations is 200
            x=x_list[i-1] #update x
            x_list.append( eval(equation) ) #calculating new x
            x_list[i]=round(x_list[i],5)
            if x_list[i]==x_list[i-1]:
                break
        print("\nXn = ",x_list)
        print("\nAfter",i,"iterations, The solution of the function is at x =",x_list[i])
    print("\n____________________________________________")
    print("Try another function.")