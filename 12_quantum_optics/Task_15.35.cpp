//15.35. Визначте енергію, масу та імпульс фотона, якому відповідає довжина хвилі 380 нм.

#include <iostream>
#include <clocale>

using namespace std;

int main()
{
   setlocale(LC_CTYPE, "ukr");

    double h = 6.626e-34;   // Стала Планка
    double c = 3.0e8;       // Швидкість світла в вакуумі

    double lambda_nm;

    cout << "Визначення енергії, маси та імпульсу фотона:" << endl;

    cout << "Введіть довжину хвилі фотона lambda (нм): ";
    cin >> lambda_nm;

    if (lambda_nm <= 0) {
        cout << "Довжина хвилі повинна бути додатною,а не від'ємною\n";
        system("pause");
        return 1;
    }

    // Переведення довжини хвилі в метри 
    double lambda = lambda_nm / 1e9; 

    // Обчислення енергії фотона
    double E = (h * c) / lambda;

    // Обчислення маси фотона
    double m = h / (c * lambda);

    // Обчислення імпульсу фотона
    double p = h / lambda;

    // Виведення результатів
    cout << "Енергія фотона E = " << E << " Дж" << endl;
    cout << "Маса фотона m = " << m << " кг" << endl;
    cout << "Імпульс фотона p = " << p << " кг*м/с" << endl;

    system("pause");
    return 0;
}
