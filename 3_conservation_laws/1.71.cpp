#include <iostream>
#include <iomanip>
#include <iomanip> 
#include <locale>

using namespace std;

int main() {
setlocale(LC_CTYPE, "ukr");
{
    //Вхідні дані
    // Маса човна 1, кг
    const double m1 = 150.0; 
    // Маса човна 2, кг
    const double m2 = 110.0; 
    // Початкова швидкість човна 1, м/с
    const double v1 = 10.0;  
    // Початкова швидкість човна 2, м/с 
    const double v2 = 15.0;  
    // Маса кожного вантажу, кг
    const double m = 10.0;   
    
    // Швидкість човна 1 після обміну (v'1)
    // Імпульс до: m*v1 (свій) + m*(-v2) (отриманий вантаж)
    // Імпульс після: m1*v'1
    // M1*v'1 = M1*v1 - m*v2
    
    double v_after_1 = (m1 * v1 - m * v2) / m1;

    // Швидкість човна 2 після обміну (v'2)
    // Імпульс до: M2*(-v2) (свій) + m*v1 (отриманий вантаж)
    // Імпульс після: M2*v'2
    // M2*v'2 = m*v1 - M2*v2
    
    double v_after_2 = (m * v1 - m2 * v2) / m2;
    
    //Виведення результатів
    cout << "1.71" << endl;
    cout << " m1 = " << m1 << " кг, v1 = " << v1 << " м/с" << endl;
    cout << " m2 = " << m2 << " кг, v2 = " << v2 << " м/с " << endl;
    cout << " Маса вантажу (m) = " << m << " кг" << endl;
    
    cout << "Швидкість першого човна після обміну:" << endl;
    cout << "v'1 = " << v_after_1 << " м/с" << endl;
    
    cout << "Швидкість другого човна після обміну:" << endl;
    cout << "v'2 = " << v_after_2 << " м/с" << endl;
}
    return 0;
}
