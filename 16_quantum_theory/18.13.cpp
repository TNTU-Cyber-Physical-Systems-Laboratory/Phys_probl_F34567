#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale> 

int main() {
    setlocale(LC_CTYPE, "ukr");

    // Константи
    double h = 6.626e-34;      // Стала Планка 
    double Me = 9.11e-31;     // Маса електрона 
    double Na = 6.022e23;     // Число Авогадро 
    double eV = 1.602e-19;    // 1 електрон-вольт 
    double Pi = M_PI;

    // Змінні для вводу
    double rho, M;
    
    std::cout << "~~Знаходження макс.енергії електрона, середньої енергії електрона і тиску електронного газу~~\n";

    std::cout << "Введіть густину металу (кг/м^3): ";
    std::cin >> rho;
    std::cout << "Введіть молярну масу (кг/моль): ";
    std::cin >> M;

    // 1. Розрахунок концентрації електронів n
    double n = (rho * Na) / M;

    // 2. Максимальна енергія електрона (Енергія Фермі) Ef
    double Ef_joules = (pow(h, 2) / (8 * Me)) * pow((3 * n) / Pi, 2.0/3.0);
    double Ef_eV = Ef_joules / eV;

    // 3. Середня енергія електрона <E>
    double E_avg_joules = 0.6 * Ef_joules;
    double E_avg_eV = E_avg_joules / eV;

    // 4. Тиск електронного газу P
    double P = (2.0 / 5.0) * n * Ef_joules;

    // Вивід результатів
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "\n~~ Результати розрахунків ~~" << std::endl;
    std::cout << "1) Максимальна енергія (Енергія Фермі):" << std::endl;
    std::cout << "   " << Ef_eV << " еВ" << std::endl;
    
    std::cout << "2) Середня енергія електрона:" << std::endl;
    std::cout << "   " << E_avg_eV << " еВ" << std::endl;

    std::cout << "3) Тиск електронного газу:" << std::endl;
    std::cout << "   " << P << " Па" << std::endl;
    std::cout << "\n~~ Задачу вирішено! :3 ~~" << std::endl;

    return 0;
}
