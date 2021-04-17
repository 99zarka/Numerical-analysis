def calc_table_element(i,matrix_row,last_x):
    res=0.0
    res+=matrix_row[-1]

    for j in range(0,len(matrix_row)-1):
        if j==i: continue
        res-=matrix_row[j]*last_x[j]

    return res/matrix_row[i]

def check_equalization(last_x,next_x):
    for i in range (0, len(last_x)):
        if last_x[i] != next_x[i]:
            return False
    return True

print('Project for "Numerical analysis". under the supervision of Dr. Mahmoud Gamal')
print('by:')
print('\t\tMohamed Yosry ElZarka 19100')
print('\t\tYoussef Mohamed Elsheheimy 19124')
print('\t\tOmar Abd Al-Halim Khalil 19138\n')

print("This is a program to calculate the numerical solution of a system of linear equations using The Jacobi Method.\n")

while True:
    n=int( input('Enter the number of equations: ') )
    print("Enter Elements of each row of the AUG matrix with the dimensions of ({} Rows X {} Columns)".format(n,n+1))
    table=[]
    matrix=[]
    last_x=[]
    next_x=[]
    for i in range(0,n):
        table.append([0.0])
        last_x.append(0.0)
        next_x.append(0.0)
        matrix.append([]) #declare n equations
        matrix[i]=[float(item) for item in input("Enter row #{} : ".format(i+1)).split()] 
        while len(matrix[i])!=n+1:
            print("ERROR, Please enter",n+1, "items per row")
            matrix[i].clear
            matrix[i]=[float(item) for item in input("Enter row #{} : ".format(i+1)).split()] 

    for i in range(0,n):
        print("row #",i+1,":",matrix[i])

    for iterations in range(0,200):
        for i in range(0,n):
            next_x[i]=calc_table_element(i, matrix[i],last_x)
            next_x[i]=round(next_x[i],3)
            table[i].append(next_x[i])
        if check_equalization(last_x,next_x):
            break
        last_x=next_x.copy()

    for i in range(0,n):
        print ('\nx{}= '.format(i+1),table[i])

    print('')
    for i in range(0,n):
        print('x{}= '.format(i+1),last_x[i])

    print("\nafter", iterations+1 ,"iterations.")
    print("\n\n____________________________________________")
    print("try another system of linear equations")