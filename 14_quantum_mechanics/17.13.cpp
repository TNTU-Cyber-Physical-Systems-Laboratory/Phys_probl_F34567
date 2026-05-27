#include <iostream>
#include <cmath>
#include <clocale>

int main() {
    setlocale(LC_CTYPE, "ukr");

    // Константи
    const double h = 6.626e-34;         // Стала Планка, Дж*с
    const double m = 9.109e-31;       // Маса електрона, кг
    const double q = 1.602e-19;  // Заряд електрона, Кл
    const double pi = 3.14159265358979; // Число Пі

    // Змінна
    double l; 

    std::cout << "===Оцінка мінімальної кінетичної енергії електрона===" << std::endl;
    
    std::cout << "Введіть розмір області локалізації l (нм): ";
    std::cin >> l;

    // Переведення нанометрів у метри 
    double l_m = l * 1e-9;

    // Обчислення мінімального імпульсу
    double p_min = h / (2.0 * pi * l_m);

    // Обчислення мінімальної кінетичної енергії
    double E_k_min = std::pow(p_min, 2) / (2.0 * m);
    
    // Конвертація в електронвольти
     double E_k_min_eV = E_k_min / q;

    std::cout << std::fixed << std::setprecision(4);
    std::cout << "\n===Результати обчислень===" << std::endl;
    std::cout << "Мінімальна кінетична енергія E_min (еВ): " << E_k_min_eV << "еВ" << std::endl;

    return 0;
}
