#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <limits>
using namespace std;

double inputPositive(string text)
{
    double x;
    while (true)
    {
        cout << text;
        cin >> x;

        if (cin.fail())
        {
            cout << "Помилка: введено не число!" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (x <= 0)
        {
            cout << "Помилка: значення повинно бути > 0!" << endl;
            continue;
        }

        return x;
    }
}

int main()
{
    system("chcp 1251 > nul");

    cout << "Задача 8.5. Сили Кулона\n\n";

    double q1 = inputPositive("q1 (нКл): ") * 1e-9;
    double q2 = inputPositive("q2 (нКл): ") * 1e-9;
    double q3 = inputPositive("q3 (мКл): ") * 1e-3;

    double r31 = inputPositive("Відстань r31 (см): ") / 100.0;
    double r32 = inputPositive("Відстань r32 (см): ") / 100.0;
    double d   = inputPositive("Відстань між q1 і q2 (см): ") / 100.0;

    const double k = 9e9;

    double F31 = k * fabs(q1 * q3) / (r31 * r31);
    double F32 = k * fabs(q2 * q3) / (r32 * r32);

    double cos_theta = (r31*r31 + r32*r32 - d*d) / (2 * r31 * r32);

    double F3 = sqrt(F31*F31 + F32*F32 - 2 * F31 * F32 * cos_theta);

    cout << "\nСила F31 = " << F31 << " Н" << endl;
    cout << "Сила F32 = " << F32 << " Н" << endl;
    cout << "cos(theta) = " << cos_theta << endl;
    cout << "Результуюча сила F3 = " << F3 << " Н" << endl;

    return 0;
}

