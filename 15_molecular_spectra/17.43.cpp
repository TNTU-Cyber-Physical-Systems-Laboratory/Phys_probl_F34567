#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale>

int main() {
    // Підключення українського локалізатора
    setlocale(LC_CTYPE, "ukr");

    std::cout << std::fixed << std::setprecision(6);

    double e= 1.602176634e-19;
	double m= 9.1093822e-31;
	double h_bar= 6.62607015e-34;
	double epsilon_0= 8.854187817e-12;

    std::cout << "~~Розрахунок еквівалентного струму електрона~~\n";
    
    std::cout << "Заряд електрона e : "<< e << "Кл\n";
    
    std::cout << "Маса електрона m : "<< m << "кг\n";
    
    std::cout << "Зведена стала Планка h_bar : "<< h_bar << "Дж*с\n";
    
    std::cout << "Електрична стала : "<< epsilon_0 << "Ф/м\n";

    // 1. Розрахунок радіуса першої орбіти (r1)
    double r1 = (4 * M_PI * epsilon_0 * std::pow(h_bar, 2)) / (m * std::pow(e, 2));
    
    // 2. Розрахунок швидкості на першій орбіті (v1) за постулатом Бора (mvr = h_bar)
    double v1 = h_bar / (m * r1);
    
    // 3. Розрахунок еквівалентного струму I = e / T, де T = 2*PI*r / v
    // Отже, I = (e * v1) / (2 * PI * r1)
    double current = (e * v1) / (2 * M_PI * r1);

    std::cout << "\n~~~Результати розрахунку~~~\n";
    std::cout << "Радіус першої орбіти (r1): " << r1 << " м\n";
    std::cout << "Швидкість електрона (v1):  " << v1 << " м/с\n";
    std::cout << "Еквівалентний струм (I):   " << current << " А\n";
     std::cout << "\nЗадачу вирішено! ^_^\n";
    return 0;
}
