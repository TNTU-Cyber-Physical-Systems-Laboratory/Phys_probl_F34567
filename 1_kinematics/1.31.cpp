#include <iostream>
#include <cmath>
#include <iomanip> 
#include <locale>
using namespace std;

int main() {
setlocale(LC_CTYPE, "ukr");
    //Вхідні дані
     // Початкова швидкість, м/с
    const double v0 = 10.0;   
    // Початковий кут, градуси
    const double alpha1_degrees = 45.0; 
     // Кут №2 , градуси
    const double alpha2_degrees = 30.0;  
     // Прискорення вільного падіння, м/с^2
    const double g = 9.8;     

    //Переведення кутів у радіани
    const double alpha1_radians = alpha1_degrees * M_PI / 180.0;
    const double alpha2_radians = alpha2_degrees * M_PI / 180.0;

    //Обчислення часу t
    // При спуску кут від'ємний (-alpha), або ми використовуємо абсолютне значення:
    // tan(alpha) = - (v0 sin(alpha0) - gt) / (v0 cos(alpha1))
    // gt = v0 sin(alpha0) + v0 cos(alpha1) tan(alpha2)
    // t = (v0 / g) * (sin(alpha1) + cos(alpha1) * tan(alpha2))
    
    //Обчислення чисельника в дужках:
    double numerator_down = sin(alpha1_radians) + cos(alpha1_radians) * tan(alpha2_radians);

    //Обчислення часу:
    double t = (v0 / g) * numerator_down;

    //Виведення результатів
    cout << "1.31" << endl;
    cout << "Початкова швидкість (v0): " << v0 << " м/с" << endl;
    cout << "Початковий кут (alpha1): " << alpha1_degrees << " градусів" << endl;
    cout << "Кінцевий кут (alpha2): " << alpha2_degrees << " градусів" << endl;
    cout << "Прискорення вільного падіння (g): " << g << " м/с^2" << endl;
  
    cout << "Час, коли вектор швидкості утворює 30 градусів:" << endl;
    cout << "t= " << t << " секунд" << endl;

    return 0;
}
