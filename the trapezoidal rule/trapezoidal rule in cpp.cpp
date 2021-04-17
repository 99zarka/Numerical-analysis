#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;
int main()
{
    cout<<"Project for 'Numerical Analysis' under the supervision of Dr. Mahmoud Gamal."<<endl;
    cout<<"by:\n\t\tMohamed Yosry ElZarka      19100.\n\t\tYoussef Mohamed ElSheheimy 19124.\n\t\tOmar Abd Al-Halim Khalil   19138.\n";

	fstream Xline, Yline;
	Yline.open("Y.txt", ios::app);
	Xline.open("X.txt", ios::app);

	double  x[1000] = { 0 }, fx[1000] = { 0 }, h = 0, res = 0;
	int n;
	cout<<"This is a program to calculate the numerical integration of a function using the trapezoidal rule.\n";

	cout << "Enter The Number of dots(n) : ";
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cout << "Enter value of x = ";
		cin >> x[i];
		Xline << x[i] << ",";
		cout << "Enter value of F(x) at x of "<<x[i]<<" = ";
		cin >> fx[i];
		Yline << fx[i] << ",";
		res += fx[i];
		if (i)h += x[i] - x[i - 1];
	}

	h /= n - 1;

	res -= fx[0] * 0.5;
	res -= fx[n - 1] * 0.5;

ofstream out ("X.txt");
ofstream out1 ("Y.txt");


for(int i=0;i<n+1;i++)
    cout<<"-----------";
    cout<<endl;
                cout<<setw(10)<<left<<"x"<<"|";
int counter=0;
       for(counter =0 ; counter < n ; counter++)
        {
            out<<x[counter];
            cout<<setw(10)<<left<<x[counter]<<"|";
	    }
	    cout<<endl;
	    for(int i=0;i<n+1;i++)
    cout<<"-----------";
    cout<<endl;
                cout<<setw(10)<<left<<"F(x)"<<"|";
	    for(counter =0 ; counter < n ; counter++)
        {
            out1<<fx[counter];
            cout<<setw(10)<<left<<fx[counter]<<"|";
	    }
	    cout<<endl;
for(int i=0;i<n+1;i++)
    cout<<"-----------";
    cout<<endl;

	cout<< endl<<"Trapezoidal Rule sum = " <<res * h;
	cin>>res;
	return 0;
}
