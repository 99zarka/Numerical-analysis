#include<iostream>
#include<iomanip>
using namespace std;

void intro();
void input_matrix(double Matrix[100][100],int* n);
void print_matrix(double Matrix[100][100],int n);
void Gauss_Elimination(double Matrix[100][100],int n);
void BACKWARD_SUBSTITUTION(double Matrix[100][100],double res[100],int n);
void print_solution(double res[100],int n);

int main()
{
    intro();
	double Matrix[100][100], res[100];
	int n;
	while(1)
    {
	input_matrix( Matrix , &n );
	cout << "\n ---------------------------------\n";
	cout << "\n AUG Matrix is:\n";
	print_matrix( Matrix , n );// Printing AUG original Matrix
	Gauss_Elimination( Matrix , n ); // Gauss Elimination
	cout << "\n Matrix after Gauss Elimination is:\n";
	print_matrix( Matrix , n ); //Printing the Matrix after Gauss Elimination
	BACKWARD_SUBSTITUTION( Matrix , res , n ); // BACKWARD SUBSTITUTION
	print_solution( res , n ); // OUTPUT
	cout<<"\nTry anther one\n";
    }
	return 0;
}

void intro()
{
    cout<<"Project for 'Numerical Analysis' under the supervision of Dr. Mahmoud Gamal.\n";
    cout<<"by:\n\t\tMohamed Yosry ElZarka      19100.\n\t\tYoussef Mohamed ElSheheimy 19124.\n\t\tOmar Abd Al-Halim Khalil   19138.\n";
    cout<<"\nThis is a program to calculate the solution of a system of linear equations using Gauss Elimination.\n";
    cout<<"The user can determine the number of equations to be solved.\n";
}

void input_matrix(double Matrix[100][100],int* n)
{
	cout << "\nEnter the number of equations: ";
	cin >> *n;
	cout << "Enter Elements of each row of the AUG matrix with the dimensions of (" << *n << " Rows X " << *n+1  <<" Columns)\n";
	for (int i = 0; i < *n; i++)
	{
		cout << "\tEnter Row #" << i + 1 << ":  ";
		for (int j = 0; j < *n + 1; j++)
            cin >> Matrix[i][j];
	}
}

void print_matrix(double Matrix[100][100],int n)
{
    for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n + 1; j++)
        {
			if(j==n)cout <<"| ";
			cout<< setw(6) << setprecision(2)   << Matrix[i][j];
        }
        cout << endl;
	}
	cout << "\n ---------------------------------\n";
}

void Gauss_Elimination(double Matrix[100][100],int n)
{
	for (int j = 0; j < n - 1; j++)
		for (int i = j + 1; i < n; i++)
		{
			double op = Matrix[i][j] / Matrix[j][j];
			for (int k = 0; k < n + 1; k++)
				Matrix[i][k] -= Matrix[j][k] * op;
		}
}

void BACKWARD_SUBSTITUTION(double Matrix[100][100],double res[100],int n)
{
	for (int i = n - 1; i >= 0; i--)
	{
		double op = 0.0;
		for (int j = i + 1; j < n; j++)
			op += Matrix[i][j] * res[j];
		res[i] = (Matrix[i][n] - op) / Matrix[i][i];
	}
}

void print_solution(double res[100],int n)
{
	cout << "\n The Solution is:\n";
	for (int i = 0; i < n; i++)
		cout << "x[" << i + 1 << "]=" << setw(5) << setprecision(11) << res[i] << endl;
    cout << "\n ---------------------------------\n";
}

