#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>

// Функція для перетворення числа у вигляд "база * 10^степінь"
std::string toPhysFormat(double value, int precision = 2) {
    std::stringstream ss;
    // Спочатку отримуємо стандартний науковий формат (наприклад, 4.74e-12)
    ss << std::scientific << std::setprecision(precision) << value;
    std::string s = ss.str();

    size_t ePos = s.find('e');
    if (ePos == std::string::npos) return s;

    std::string base = s.substr(0, ePos);
    std::string expStr = s.substr(ePos + 1);
    
    // Перетворюємо степінь у число, щоб прибрати зайві нулі та плюси (наприклад, +02 -> 2)
    int exponent = std::stoi(expStr);

    return base + " * 10^" + std::to_string(exponent);
}

int main() {
    // 1. Точні фізичні константи
    const double m = 9.11e-31;     // Маса електрона, кг
    const double e = 1.602e-19;    // Заряд електрона, Кл
    const double eps0 = 8.854e-12; // Електрична стала, Ф/м

    // 2. Вхідні дані
    const double d = 5.3e-3;       // Відстань, м
    const double v = 1e6;          // Швидкість, м/с

    // 3. Розрахунки
    double U = (m * v * v) / (2 * e);
    double E = U / d;
    double sigma = E * eps0;

    // 4. Гарний вивід результатів
    std::cout << "                    RESULTS                  " << std::endl;
    
    // Напруга зазвичай невелика, її можна вивести просто числом
    std::cout << "1) Riznytsia potentsialiv (U):   " 
              << std::fixed << std::setprecision(3) << U << " V" << std::endl;

    // Напруженість та густина — у твоєму форматі
    std::cout << "2) Napruzhenist polia (E):      " 
              << toPhysFormat(E, 2) << " V/m" << std::endl;

    std::cout << "3) Gustyna zariadu (sigma):     " 
              << toPhysFormat(sigma, 2) << " Kl/m^2" << std::endl;

    return 0;
}