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
            cout << "Помилка: введено недопустиме значення.\n";
        }
        else break;
    }
    return x;
}

int main()
{
    system("chcp 1251 > nul");

    cout << "=== Задача 9.13 — Струм короткого замикання ===\n\n";

    double R1 = inputPositive("Введи R1 (Ом): ");
    double I1 = inputPositive("Введи I1 (А): ");
    double R2 = inputPositive("Введи R2 (Ом): ");
    double I2 = inputPositive("Введи I2 (А): ");

    // внутрішній опір r
    double r = (I1 * R1 - I2 * R2) / (I2 - I1);

    // ЕРС
    double E = I1 * (R1 + r);

    // струм КЗ
    double Ikz = E / r;

    cout << "\nВнутрішній опір r = " << r << " Ом\n";
    cout << "ЕРС джерела ? = " << E << " В\n";
    cout << "Струм короткого замикання Iкз = " << Ikz << " А\n";

    return 0;
}

