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

    cout << "Задача 3.42. Обертання колеса (гальмування)\n\n";

    double n1 = inputPositive("Початкова частота n1 (об/хв): ");
    double n2 = inputPositive("Кінцева частота n2 (об/хв): ");
    double I  = inputPositive("Момент інерції I (кг·м^2): ");
    double t  = inputPositive("Час гальмування t (с): ");

    double w1 = 2 * M_PI * (n1 / 60.0);
    double w2 = 2 * M_PI * (n2 / 60.0);

    double alpha = (w2 - w1) / t;

    double M = I * alpha;

    double phi = w1 * t + alpha * t * t / 2.0;

    double A = M * phi;

    double N = phi / (2 * M_PI);

    cout << "\nРЕЗУЛЬТАТИ:\n";
    cout << "Кутове прискорення a = " << alpha << " рад/с^2" << endl;
    cout << "Момент сил гальмування M = " << M << " Н·м" << endl;
    cout << "Робота сил гальмування A = " << A << " Дж" << endl;
    cout << "Кількість обертів N = " << N << endl;

    return 0;
}

