#include <iostream>
#include <cmath>
#include <iomanip> 
#include <locale>
using namespace std;

int main() {
setlocale(LC_CTYPE, "ukr");
    //����� ���
     // ��������� ��������, �/�
    const double v0 = 10.0;   
    // ���������� ���, �������
    const double alpha1_degrees = 45.0; 
     // ��� �2 , �������
    const double alpha2_degrees = 30.0;  
     // ����������� ������� ������, �/�^2
    const double g = 9.8;     

    //����������� ���� � ������
    const double alpha1_radians = alpha1_degrees * M_PI / 180.0;
    const double alpha2_radians = alpha2_degrees * M_PI / 180.0;

    //���������� ���� t
    // ��� ������ ��� ��'����� (-alpha), ��� �� ������������� ��������� ��������:
    // tan(alpha) = - (v0 sin(alpha0) - gt) / (v0 cos(alpha1))
    // gt = v0 sin(alpha0) + v0 cos(alpha1) tan(alpha2)
    // t = (v0 / g) * (sin(alpha1) + cos(alpha1) * tan(alpha2))
    
    //���������� ���������� � ������:
    double numerator_down = sin(alpha1_radians) + cos(alpha1_radians) * tan(alpha2_radians);

    //���������� ����:
    double t = (v0 / g) * numerator_down;

    //��������� ����������
    cout << "1.31" << endl;
    cout << "��������� �������� (v0): " << v0 << " �/�" << endl;
    cout << "���������� ��� (alpha1): " << alpha1_degrees << " �������" << endl;
    cout << "ʳ������ ��� (alpha2): " << alpha2_degrees << " �������" << endl;
    cout << "����������� ������� ������ (g): " << g << " �/�^2" << endl;
  
    cout << "���, ���� ������ �������� ������� 30 �������:" << endl;
    cout << "t= " << t << " ������" << endl;

    return 0;
}
