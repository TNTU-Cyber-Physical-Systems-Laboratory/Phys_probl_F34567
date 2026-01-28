#include <iostream>
#include <cmath>
using namespace std;
double m, R, r, d, I, I1, I2, I0, M;
int main()
{
	cout << "m="; cin >> m;
	cout << "R="; cin >> R;
	cout << "r="; cin >> r;
	cout << "d="; cin >> d;
	M = m * pow(r / R, 2);
	I0 = 0.5 * m * pow(R, 2.0);
	I1 = 0.5 * M * pow(r, 2.0);
	I2 = I1 + M * pow(d,2.0);
	I = I0 - I2;
	cout << "I=" << I << endl;
	return 0;
}