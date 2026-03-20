//Автор: Mykola Kuryliv (Студент ТНТУ)
//Задача: № 7.151 (Тема 10. Закони термодинаміки)
//Опис: Програма для обчислення ККД циклу (1-2-3) та ASCII-візуалізації P-V діаграми.

#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
using namespace std;
// Функція для малювання P-V діаграми
void draw_advanced_pv_diagram(double T1, double T2, double gamma) {
    const int height = 15;
    const int width = 50;
    // Розрахунок ключових параметрів для масштабів
    double r_T = T2 / T1;
    double V1 = 1.0; 
    double V3 = pow(r_T, 1.0 / (gamma - 1.0)); // Співвідношення V3/V1
    double P1 = 1.0;                           // Умовний початковий тиск
    double P2 = P1 * r_T;                      // Ізохора (P~T)
    double P3 = P2 * pow(V1 / V3, gamma);      // Адіабата
    double P_max = P2;
    double V_max = V3;
    double P_scale = P_max / height;
    double V_scale = (V_max * 1.1) / width;
    cout << "\n--- Спрощена P-V діаграма ---\n";
    cout << "P ^\n";
    for (int row = height; row >= 0; --row) {
        double P_curr = row * P_scale;  
        // Малюємо вісь P з відмітками
        if (row % 5 == 0) cout << setw(4) << fixed << setprecision(1) << P_curr << " ┤";
        else cout << "     │";
        for (int col = 0; col <= width; ++col) {
            double V_curr = col * V_scale;
            if (V_curr < V1 * 0.5) { cout << " "; continue; }
            // 1. Ізохора 1-2 (Вертикальна лінія)
            bool isochore = (abs(V_curr - V1) < V_scale * 0.6) && (P_curr >= P1 && P_curr <= P2);         
            // 2. Адіабата 2-3 (P = P2 * (V1/V)^gamma)
            double P_adiab = P2 * pow(V1 / V_curr, gamma);
            bool adiabat = (abs(P_curr - P_adiab) < P_scale * 0.6) && (V_curr >= V1 && V_curr <= V3);            
            // 3. Ізотерма 3-1 (P = P1 * (V1/V))
            double P_isot = P1 * (V1 / V_curr);
            bool isotherm = (abs(P_curr - P_isot) < P_scale * 0.4) && (V_curr >= V1 && V_curr <= V3);
            if (isochore)      cout << "║"; // Ізохора
            else if (adiabat)  cout << "▓"; // Адіабата
            else if (isotherm) cout << "░"; // Ізотерма
            else               cout << " ";
        }
        cout << "\n";
    }
    cout << "     └" << string(width, '-') << "> V\n";
    cout << "      (║ - ізохора, ▓ - адіабата, ░ - ізотерма)\n";
}
int main() {
    // Налаштування консолі для виводу символів
    #ifdef _WIN32
        system("chcp 65001 > nul"); // Для коректного відображення UTF-8 у Windows
    #endif
    cout << fixed << setprecision(3);
    cout << "========================================================\n";
    cout << "   РОЗРАХУНОК ТЕРМОДИНАМІЧНОГО ЦИКЛУ (1-2-3)\n";
    cout << "========================================================\n\n";
    double T1, T2, gamma;
    const double R = 8.314;
    // Введення даних
    cout << "Введіть мінімальну температуру T1 (K) [напр. 260]: ";
    cin >> T1;
    cout << "Введіть максимальну температуру T2 (K) [напр. 520]: ";
    cin >> T2;
    cout << "Введіть показник адіабати γ (1.67-одноатомний, 1.4-двоатомний): ";
    cin >> gamma;

    if (T2 <= T1 || T1 <= 0 || gamma <= 1) {
        cout << "\n[Помилка] Некоректні термодинамічні параметри!\n";
        return 1;
    }
    // Фізичні обчислення
    double r_T = T2 / T1;
    double Cv = R / (gamma - 1.0);   
    // ККД за виведеною формулою: eta = 1 - (T1 * ln(T2/T1)) / (T2 - T1)
    double ratio = log(r_T) / (r_T - 1.0);
    double eta = 1.0 - ratio;
    double eta_carnot = 1.0 - (T1 / T2);
    // Вивід результатів
    cout << "\n--------------------------------------------------------\n";
    cout << "РЕЗУЛЬТАТИ ОБЧИСЛЕНЬ:\n";
    cout << "--------------------------------------------------------\n";
    cout << "Відношення температур T2/T1:  " << r_T << endl;
    cout << "Відношення об'ємів V3/V1:    " << pow(r_T, 1.0 / (gamma - 1.0)) << endl;
    cout << "--------------------------------------------------------\n";
    cout << "ККД даного циклу (η):        " << eta * 100.0 << " %\n";
    cout << "ККД циклу Карно (η_c):       " << eta_carnot * 100.0 << " %\n";
    cout << "--------------------------------------------------------\n";
    // Малювання графіка
    draw_advanced_pv_diagram(T1, T2, gamma);
    cout << "\nРозрахунок завершено успішно.\n";
    return 0;
}