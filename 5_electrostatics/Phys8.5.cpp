#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
const double k_const = 9e9;
double q1, r12, q2, q3, r13, r23;
double F13, F23, F_result, cos_alpha;

int main()
{
    cout << "Введіть дані (заряди в нКл, відстані в см):" << endl;
    cout << "q1 (нКл) = "; cin >> q1;
    cout << "q2 (нКл) = "; cin >> q2;
    cout << "q3 (нКл) = "; cin >> q3;
    cout << "r12 (см) = "; cin >> r12;
    cout << "r13 (см) = "; cin >> r13;
    cout << "r23 (см) = "; cin >> r23;
    double Q1 = q1 * 1e-9;
    double Q2 = q2 * 1e-9;
    double Q3 = q3 * 1e-9;
    double R12 = r12 * 0.01;
    double R13 = r13 * 0.01;
    double R23 = r23 * 0.01;
    F13 = k_const * (abs(Q1 * Q3) / pow(R13, 2.0));
    F23 = k_const * (abs(Q2 * Q3) / pow(R23, 2.0));
    cos_alpha = (pow(R13, 2.0) + pow(R23, 2.0) - pow(R12, 2.0)) / (2.0 * R13 * R23);
    F_result = sqrt(pow(F13, 2.0) + pow(F23, 2.0) + 2.0 * F13 * F23 * cos_alpha);
    cout << setprecision(8) << fixed << endl;
    cout << "--- Проміжні розрахунки ---" << endl;
    cout << "Модуль F13 = " << F13 << " Н" << endl;
    cout << "Модуль F23 = " << F23 << " Н" << endl;
    cout << "Косинус кута між силами (cos(alpha)) = " << cos_alpha << endl;

    cout << "--------------------------" << endl;
    cout << "Результуюча сила F = " << F_result << " Н" << endl;
    cout << "Результуюча сила F (Scientific) = " << scientific << F_result << " Н" << endl;

    return 0;
}