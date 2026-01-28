#include <iostream>
#include <cmath>
using namespace std;
double A1, A2, y, A;
const double w = 3.14;
int main()
{
	cout << "A1= "; cin >> A1;
	cout << "A2= "; cin >> A2;
	A = sqrt(pow(A1,2.0) + pow(A2,2.0));
	y = tan(A1 / A2);
	cout << "A= " << A << endl;
	cout << "y= " << y << endl;
	return 0;
}