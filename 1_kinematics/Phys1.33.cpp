#include <iostream>
#include <cmath>
#include <clocale>
#ifdef _WIN32
#include <windows.h>
#endif
using namespace std;

double X(double t) {
    return 2.0 + t - 0.5 * t * t * t;
}

double V(double t) {
    return 1.0 - 1.5 * t * t;
}

double A(double t) {
    return -3.0 * t;
}

int main() {
    setlocale(LC_ALL, "");
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
#endif
    
    double t1 = 0.0;
    double t2 = 3.0;
    double dt = t2 - t1;
    
    double x1 = X(t1);
    double x2 = X(t2);
    double Vc = (x2 - x1) / dt;
    cout << "Середня швидкість: (" << x2 << " - " << x1 << ") / " << dt << " = " << Vc << " м/с" << endl;
    
    double v1 = V(t1);
    double v2 = V(t2);
    double ac = (v2 - v1) / dt;
    cout << "Середнє прискорення: (" << v2 << " - " << v1 << ") / " << dt << " = " << ac << " м/с^2" << endl;
    
    return 0;
}