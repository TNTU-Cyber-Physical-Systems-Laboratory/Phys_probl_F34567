#include <iostream>
#include <cmath>
using namespace std;
double x1, F1, x2, A, k;
int main()
{
	cout << "x1 = "; cin >> x1;
	cout << "F1 = "; cin >> F1;
	cout << "x2 = "; cin >> x2;
	k = F1 / x1;
	A = (k * pow(x2, 2.0)) / 2;
	cout << "A = " << A << endl;
}