#include <iostream>
using namespace std;

double inputPositive(string text)
{
    double x;
    while (true)
    {
        cout << text;
        cin >> x;

        if (cin.fail() || x <= 0)
        {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Помилка: введено недопустиме значення! Спробуй ще раз.\n";
        }
        else break;
    }
    return x;
}

int main()
{
    system("chcp 1251 > nul");

    cout << "=== Задача 3.4 — два вантажі через блок ===\n\n";

    double m1 = inputPositive("Введи m1 (кг): ");
    double m2 = inputPositive("Введи m2 (кг): ");
    double M  = inputPositive("Введи масу блока M (кг): ");

    double g = 9.8;

    double a = ( (m1 - m2) * g ) / ( m1 + m2 + 0.5 * M );

    double T1 = m1 * (g - a);
    double T2 = m2 * (g + a);

    cout << "\nПрискорення вантажів a = " << a << " м/с^2\n";
    cout << "Натяг нитки з боку m1: T1 = " << T1 << " Н\n";
    cout << "Натяг нитки з боку m2: T2 = " << T2 << " Н\n";

    return 0;
}

