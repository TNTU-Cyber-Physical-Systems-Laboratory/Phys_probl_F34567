#include <iostream>
#include <cmath>
#include <clocale>

int main() {
    setlocale(LC_CTYPE, "ukr");

    // Константи
    const double h = 6.626e-34;       // Стала Планка
    const double m = 9.109e-31;     // Маса електрона
    const double q = 1.602e-19; // Заряд електрона

    // Змінні
    double U, d, l;
    
    std::cout << ":::Знаходження відстань між сусідніми максимумами дифракційної картини:::" << std::endl;

    // Введення даних
    std::cout << "Введіть прискорюючу напругу U (В): ";
    std::cin >> U;

    std::cout << "Введіть відстань між щілинами d (мкм): ";
    std::cin >> d;

    std::cout << "Введіть відстань до екрана l (см): ";
    std::cin >> l;

    // Переведення одиниць в систему СІ (метри)
    double D = d * 1e-6; // з мкм в метри
    double L = l * 1e-2;      // з см в метри

    // 1. Обчислення довжини хвилі де Бройля для електрона
    double lambda = h / std::sqrt(2.0 * m * q * U);

    // 2. Обчислення відстань між сусідніми максимумами на екрані
    double delta_x = (lambda * L) / D;

    // Переведемо результат у міліметри для зручності сприйняття
    double delta_x_mm = delta_x * 1000.0;

    // Виведення результатів
    std::cout << "\n::: Результати обчислень:::" << std::endl;
    std::cout << "Відстань між сусідніми максимумами (delta_x) = " <<  delta_x_mm  << " мм" << std::endl;

    return 0;
}
