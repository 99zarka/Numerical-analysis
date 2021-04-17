print('Project for "Numerical analysis". under the supervision of Dr. Mahmoud Gamal')
print('by:')
print('\t\tMohamed Yosry ElZarka 19100')
print('\t\tYoussef Mohamed Elsheheimy 19124')
print('\t\tOmar Abd Al-Halim Khalil 19138\n')

print("This is a program to calculate the numerical integration of a function using the trapezoidal rule.\n")
while True:
    n=int( input("enter the number of dots: ") )
    s=float( input("enter the start of the integration: ") )
    e=float( input("enter the end of the integration: ") )
    h=(e-s)/(n-1)
    X=[]
    fX=[]
    for i in range(0,n):
        X.append( float( s+h*i ) )
        
    print("\nyou can use parentheses () in addition to the following mathematical operators:")
    print("(+ Add), (- Subtract), (* Multiply), (/ Divide), (% Modulus), (// Floor division), (** Exponent)\n")
    x = 1
    stri=str(input("enter the equation: f(x)= "))

    sum=0
    for i in range(0,n):
        x=X[i]
        fX.append( eval(stri) )
        sum+=fX[i]
    sum= sum - 0.5*fX[0] - 0.5*fX[n-1]
    print('\nh=',h)
    print("x=",X)
    print("f(x)=",fX)
    print("")
    print("from",s,"to",e, "   ∫ f(x) dx= ∫",stri,"dx=",sum*h)
    print('__________________________')
    print('Try another integration.')
