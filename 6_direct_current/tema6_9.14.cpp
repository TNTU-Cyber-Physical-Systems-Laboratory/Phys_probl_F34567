#include <iostream>
#include <iomanip>
#include <cmath> 
#include <string>
#include <sstream>


std::string toPhysFormat(double value, int precision = 2) {
    if (std::abs(value) < 1000 && std::abs(value) > 0.001) {
        std::stringstream ss;
        ss << std::fixed << std::setprecision(precision) << value;
        return ss.str();
    }
    std::stringstream ss;
    ss << std::scientific << std::setprecision(precision) << value;
    std::string s = ss.str();
    size_t ePos = s.find('e');
    if (ePos == std::string::npos) return s;
    int exponent = std::stoi(s.substr(ePos + 1));
    return s.substr(0, ePos) + " * 10^" + std::to_string(exponent);
}

int main() {
    // 1. Вхідні дані з умови
    const double epsilon = 4.5; // ЕРС однієї батарейки, В
    const double r = 3.0;       // Внутрішній опір однієї батарейки, Ом
    const double U = 220.0;     // Напруга лампи, В
    const double P = 60.0;      // Потужність лампи, Вт

    // 2. Розрахунки
    // Струм, який споживає лампа: I = P / U
    double I = P / U;

    // Кількість батарейок: N = U / (epsilon - I * r)
    double N_exact = U / (epsilon - I * r);
    
    // Округлюємо вгору, бо нам потрібна ціла кількість батарейок для забезпечення роботи
    int N_rounded = std::ceil(N_exact);

    // 3. Вивід результатів
    std::cout << "         Rezultaty obchyslen " << std::endl;
    
    std::cout << "Strum u koli (I):           " << std::fixed << std::setprecision(3) << I << " A" << std::endl;
    
    std::cout << "Tochne znachennia N:        " << std::fixed << std::setprecision(2) << N_exact << std::endl;
    
    std::cout << "Potribna kilkist batareiok: " << N_rounded << " sht." << std::endl;
    


    return 0;
}