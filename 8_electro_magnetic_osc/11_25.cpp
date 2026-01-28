#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <windows.h>

using namespace std;

const double C = 3.0e8; // швидкість світла, м/с
const double PI = 3.14159265358979323846;

// Функція для парсингу рівняння струму та витягування кутової частоти ?
// Приймає рівняння типу: I=0.3sin(15.7t), 0.3sin(15.7t), 0,3sin(15,7t)
// Повертає true якщо парсинг успішний, false - якщо помилка
bool parseEquation(const string& eq, double& omega) {
    string s = eq;
    
    // Видаляємо всі пробіли з рядка
    string cleaned = "";
    for (size_t i = 0; i < s.length(); i++) {
        if (s[i] != ' ') cleaned += s[i];
    }
    
    // Шукаємо "sin(" в рядку
    size_t sinPos = cleaned.find("sin(");
    if (sinPos == string::npos) return false;
    
    // Позиція після "sin("
    size_t startPos = sinPos + 4;
    
    // Витягуємо число після "sin(" до символу 't' або '*'
    string numStr = "";
    for (size_t i = startPos; i < cleaned.length(); i++) {
        char c = cleaned[i];
        // Якщо зустрічаємо 't' або '*' - закінчуємо
        if (c == 't' || c == 'T' || c == '*') break;
        // Додаємо цифри, крапку або кому
        if (isdigit(c) || c == '.' || c == ',') {
            if (c == ',') c = '.'; // Заміна коми на крапку
            numStr += c;
        }
    }
    
    // Перетворюємо рядок у число
    if (numStr.empty()) return false;
    
    try {
        omega = atof(numStr.c_str());
        if (omega <= 0) return false;
        return true;
    } catch (...) {
        return false;
    }
}

// Функція для форматованого виведення чисел
string formatNumber(double value) {
    char buffer[100];
    
    if (value >= 1e9) {
        long long num = (long long)(value / 1e9);
        sprintf(buffer, "%lld * 10^9", num);
        return string(buffer);
    } else if (value >= 1e6) {
        long long num = (long long)(value / 1e6);
        sprintf(buffer, "%lld * 10^6", num);
        return string(buffer);
    } else if (value >= 1e3) {
        long long num = (long long)(value / 1e3);
        sprintf(buffer, "%lld * 10^3", num);
        return string(buffer);
    } else if (value >= 1) {
        sprintf(buffer, "%.2f", value);
        return string(buffer);
    } else if (value >= 1e-3) {
        sprintf(buffer, "%.4f", value);
        return string(buffer);
    } else {
        sprintf(buffer, "%.2e", value);
        return string(buffer);
    }
}

int main() {
    // Встановлення кодування Windows-1251 для кирилиці
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    
    cout << "==========================================" << endl;
    cout << " РОЗРАХУНОК ДОВЖИНИ ЕЛЕКТРОМАГНІТНОЇ ХВИЛІ" << endl;
    cout << "==========================================" << endl;
    cout << endl;
    
    cout << "Оберіть спосіб введення:" << endl;
    cout << "1 - Ввести рівняння (наприклад: 0.3sin(15.7t))" << endl;
    cout << "2 - Ввести w окремо" << endl;
    cout << "Вибір: ";
    
    int choice;
    cin >> choice;
    cin.ignore(); // Очищення буфера після введення числа
    
    double omega;
    
    if (choice == 1) {
        // Варіант 1: Парсинг рівняння
        cout << endl;
        cout << "Введіть рівняння: ";
        string equation;
        getline(cin, equation);
        
        if (!parseEquation(equation, omega)) {
            cout << "Помилка парсингу! Використайте формат: 0.3sin(15.7t)" << endl;
            return 1;
        }
        cout << "w = " << omega << " рад/с" << endl;
    } else {
        // Варіант 2: Пряме введення omega
        cout << endl;
        cout << "Введіть w (рад/с): ";
        cin >> omega;
        if (omega <= 0) {
            cout << "Помилка! w повинно бути > 0" << endl;
            return 1;
        }
    }
    
    // Розрахунки за формулами
    double T = (2 * PI) / omega;  // Період коливань
    double lambda = C * T;         // Довжина електромагнітної хвилі
    
    // Виведення результатів
    cout << endl;
    cout << "==========================================" << endl;
    cout << " РОЗВ'ЯЗОК" << endl;
    cout << "==========================================" << endl;
    cout << endl;
    
    cout << "1. Період коливань:" << endl;
    cout << "   T = 2*pi/w = 2*pi/" << omega << endl;
    cout << "   T = " << formatNumber(T) << " с" << endl;
    cout << endl;
    
    cout << "2. Довжина електромагнітної хвилі:" << endl; 
    cout << "   lambda = c * T" << endl;
    cout << "   lambda = " << formatNumber(C) << " м/с * " << formatNumber(T) << " с" << endl;
    cout << "   lambda = " << formatNumber(lambda) << " м" << endl;
    
    // Виведення у кілометрах для зручності
    if (lambda >= 1000) {
        cout << fixed << setprecision(2);
        cout << "   lambda = " << lambda / 1000.0 << " км" << endl;
    }
    
    cout << endl;
    
    // Попередження про нереалістичні значення
    if (lambda > 1e6) {
        cout << "УВАГА: Довжина хвилі нереалістична" << endl;
        cout << "       для коливального контуру!" << endl;
    }
    
    cout << "==========================================" << endl;
    
    return 0;
}
