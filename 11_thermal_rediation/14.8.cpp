#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;

int main() {
    setlocale(LC_CTYPE, "ukr");
    
    //Константи
     double sigma = 5.67e-8;
     double R= 1.496e11;
     const double S = 1.0; 
     const double t = 1.0;

    // Змінні
    double T, r_sun;
    
    std::cout << "~~~Визначення сонячної сталої~~~" << std::endl;

    std::cout << "Введіть температуру поверхні Сонця (К): ";
    std::cin >> T;

    std::cout << "Введіть радіус Сонця (м): ";
    std::cin >> r_sun;

    // Розрахунок енергетичної світності Сонця 
    double W = sigma * std::pow(T, 4);

    // Розрахунок сонячної сталої 
    double C = W * std::pow(r_sun / R, 2);


    // Виведення результатів
    std::cout << "\n~~~Результат~~~" << std::endl;
    std::cout << "Сонячна стала = " << C << " Вт/м^2" << std::endl;

    return 0;
}
