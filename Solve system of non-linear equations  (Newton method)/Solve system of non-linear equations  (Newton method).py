import math
from sympy import * #for differentiation & mathematical functions
import numpy as np #matrix operations

pi=3.141592653589793
e=2.718281828459045

print('Project for "Numerical analysis". under the supervision of Dr. Mahmoud Gamal')
print('by:')
print('\t\tMohamed Yosry ElZarka 19100')
print('\t\tYoussef Mohamed Elsheheimy 19124')
print('\t\tOmar Abd Al-Halim Khalil 19138\n')

print("This is a program to calculate the numerical solution of a system of non-linear equations using (Newton's method).\n")

print("""
you can use parentheses () in addition to the following mathematical operators:
(+ Add), (- Subtract), (* Multiply), (/ Divide), (% Modulus), (// Floor division), (** Exponent)
you can also use the following constants:
\t pi=3.141592653589793
\t e=2.718281828459045
note: Trigonometric functions sin(x), asin(x), cos(x), acos(x), tan(x), atan(x) 'equivalent of tan-1(x)' use radian values.
      log(x,y)= log(x) / log(y) ,,, ln(x)
""")

def check_equalization(recent_x,previous_x):
    for i in range (0, len(recent_x)):
        if recent_x[i] != previous_x[i]:
            return False
    return True

decimal_point_precision=4

while True:
    n=int( input('Enter the number of equations: ') )
    equations, equations_values, jacobian_matrix, jacobian_values= [] , [0]*n , [] , []

    for i in range(0,n):
        equations.append( str(input("Enter the equation #{}:    0 = ".format(i+1))) )
        jacobian_matrix.append([])
        jacobian_values.append([0]*n)
    last_x , current_x= [] , []
    for i in range(0,n):
        last_x.append( float(input("Enter the initial x{} = ".format(i+1))) )

    for i in range(0,n): #partial differntiaion matrix
        for j in range(0,n):
            jacobian_matrix[i].append(  diff( equations[i] , 'x'+str(j+1) ) ) 

    print("\njacobian matrix=",jacobian_matrix)

    print("\n        ",end="")
    for i in range(0,n):
        print("x{}          ".format(i+1),end="")
    print("")
    print("i=0",end="")
    for i in range(0,n):
        last_x[i]=round( last_x[i] , decimal_point_precision )
        print(" | %.4f | "%last_x[i],end="")
    print("")

    dictionary_of_last_x={}

    for iterations in range(1,500): #maximum number of iterations is 500
        for i in range(0,n): #updating the values of matrices
            dictionary_of_last_x['x'+str(i+1)]=last_x[i]
        for i in range(0,n): 
            equations_values[i]=round( eval(equations[i],dictionary_of_last_x) , decimal_point_precision)
        for i in range(0,n):
            for j in range(0,n):
                jacobian_values[i][j]=round( eval(str(jacobian_matrix[i][j]),dictionary_of_last_x) , decimal_point_precision )

        A = np.array(last_x) #matrix declarations
        B = np.array(jacobian_values)
        C = np.array(equations_values)

        current_x=np.subtract(A, np.dot( np.linalg.inv(B)  , C ) ) #matrix operations

        print("i={}".format(iterations),end="")
        for i in range(0,n):
            current_x[i]=round( current_x[i] , decimal_point_precision )
            print(" | %.4f | "%current_x[i],end="")
        print("")
        if check_equalization(current_x,last_x):
            break
        last_x=current_x

    print("\nAfter",iterations,"iterations, The solution is at")
    for i in range(0,n):
        print("\t\tx{} =".format(i+1),last_x[i])
    print("\n____________________________________________")
    print("Try another system of non-linear equations.")