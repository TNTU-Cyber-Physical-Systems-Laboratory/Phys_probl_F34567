//13.22. На щілину, ширина якої 2 мкм, падає нормально паралельний пучок монохроматичного світла з довжиною хвилі 589 нм. Знайдіть кути, у напрямку яких будуть спостерігатися мінімуми світла.

#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double a, lambda;
    const double pi = 3.1415926535;
    cout << "Введіть ширину щілини a (мкм): ";
    cin >> a;

    if (a <= 0) {
        cout << "Помилка! Ширина щілини повинна бути додатною!\n";
        return 1;
    }
    cout << "Введіть довжину хвилі lambda (нм): ";
    cin >> lambda;

    if (lambda <= 0) {
        cout << "Помилка! Довжина хвилі повинна бути додатною!\n";
        return 1;
    }

    a = a * pow(10, -6);
    lambda = lambda * pow(10, -9);
    cout << "\nМінімуми світла:\n";
    for (int k = 1; ; k++)
    {
        double value = k * lambda / a;

        if (value > 1)
            break;

        double phi_rad = asin(value);
        double phi_deg = phi_rad * 180 / pi;

        cout << "k = " << k
            << ": phi = ±" << phi_deg
            << " градусів" << endl;
    }

    return 0;
}