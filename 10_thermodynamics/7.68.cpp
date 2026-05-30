//7.68. Обчисліть внутрішню енергію 14 г азоту при 300 К.

#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double m, M, T;
    const double R = 8.31;
    cout << "Введіть масу газу m (г): ";
    cin >> m;
    if (m <= 0) {
        cout << "Помилка! Маса повинна бути додатною!\n";
        return 1;
    }
    cout << "Введіть молярну масу M (г/моль): ";
    cin >> M;
    if (M <= 0) {
        cout << "Помилка! Молярна маса повинна бути додатною!\n";
        return 1;
    }
    cout << "Введіть температуру T (К): ";
    cin >> T;
    if (T <= 0) {
        cout << "Помилка! Температура повинна бути більшою за 0!\n";
        return 1;
    }

    m = m * pow(10, -3);
    M = M * pow(10, -3);

    // Для двоатомного газу i = 5
    int i = 5;
    double U = (i / 2.0) * (m / M) * R * T;
    cout << "\nВнутрішня енергія газу U = "
        << U << " Дж" << endl;

    return 0;
}