#include <iostream>
#include <cmath>
#include <clocale>

int main() {
    setlocale(LC_CTYPE, "ukr");

    // константи 
    const double R = 8.314;       // Універсальна газова стала
    const double M = 0.040;       // Молярна маса аргону
    const double gamma = 5.0 / 3.0; // Показник адіабати для одноатомного газу

   // змінні
    double m_g, T1, P1, P2;   
    
    std::cout << "^^^Розрахунок температури газу, відношення початкового об'єму до кінцевого і роботи газу^^^" << std::endl;
    
    std::cout << "Введіть масу газу (г): ";
    std::cin >> m_g;
    
    std::cout << "Введіть початкову температуру (К): ";
    std::cin >> T1;
    
    std::cout << "Введіть початковий тиск (Па): ";
    std::cin >> P1;
    
    std::cout << "Введіть кінцевий тиск (Па): ";
    std::cin >> P2;

    // Переведення маси в кілограми 
    double m = m_g / 1000.0;

    // 1. Обчислення кінцевої температури T2
    double power_T = (gamma - 1.0) / gamma; 
    double T2 = T1 * std::pow(P2 / P1, power_T);

    // 2. Обчислення відношення об'ємів V1 / V2
    double power_V = 1.0 / gamma;           
    double V_ratio = std::pow(P2 / P1, power_V);

    // 3. Обчислення роботи, виконаної газом A
    double A = (m / M) * (R / (gamma - 1.0)) * (T1 - T2);

    // Виведення результатів
    std::cout << "\n^^^Результат розрахунків^^^" << std::endl;
    std::cout << "Кінцева температура газу = " << T2 << " K" << std::endl;
    std::cout << "Відношення початкового об'єму до кінцевого = " << V_ratio << std::endl;
    std::cout << "Робота, виконана газом = " << A << " Дж" << std::endl;
    
    return 0;
}
