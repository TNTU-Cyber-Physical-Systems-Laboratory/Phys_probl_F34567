#include <iostream>
#include <cmath>
#include <clocale>

int main() {
    setlocale(LC_CTYPE, "ukr");

    // Константи
    double sigma = 5.67e-8; // Стала Стефана-Больцмана
    double r_o = 1.496e11;  // Радіус земної орбіти (відстань від Землі до Сонця)
    double r_s = 6.96e8;    // Радіус Сонця

    // Змінні
    double T; // Температура поверхні Сонця

    std::cout << "~~~Визначення сонячної сталої~~~" << std::endl;

    std::cout << "Введіть температуру поверхні Сонця (К): ";
    std::cin >> T;

    // Розрахунок енергетичної світності Сонця
    double R = sigma * std::pow(T, 4);

    // Розрахунок сонячної сталої
    double C = R * std::pow(r_s / r_o, 2);

    // Виведення результатів
    std::cout << "\n~~~Результат~~~" << std::endl;
    std::cout << "Сонячна стала = " << C << " Вт/м^2" << std::endl;

    return 0;
}
