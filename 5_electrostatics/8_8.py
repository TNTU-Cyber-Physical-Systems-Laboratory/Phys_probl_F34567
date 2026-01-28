import math

# Константа закону Кулона
K = 9e9
# Прискорення вільного падіння
G = 9.8

def calculate_charge():
    print("=== Калькулятор заряду кульок (Задача 8.8) ===")
    
    while True:
        print("\n--- Введіть дані ---")
        try:
            # Введення даних
            m_grams = input("Маса кульки (грами) : ")
            m = float(m_grams) / 1000 if m_grams else 0.1 / 1000
            
            l_cm = input("Довжина нитки (см) : ")
            l = float(l_cm) / 100 if l_cm else 0.2
            
            angle_deg = input("Кут відхилення (градуси) : ")
            alpha_deg = float(angle_deg) if angle_deg else 30.0
            
            # Переведення кута в радіани
            alpha_rad = math.radians(alpha_deg)
            
            # Розрахунок за виведеною формулою: q = l * sin(a) * sqrt( (mg * tan(a) * sqrt(3)) / (k * tan(a) * sqrt(3)) )
            # Спрощена формула (працює ідеально для 30 градусів, для інших - повна):
            # Повна формула з виведення: q = sqrt( (mg * tan(alpha) * sqrt(3) * l^2 * sin^2(alpha)) / k )
            # Але краще використати крок за кроком для точності:
            
            # 1. Сила тяжіння
            F_gravity = m * G
            
            # 2. Необхідна електрична сила (F_e = mg * tan(alpha))
            F_electric = F_gravity * math.tan(alpha_rad)
            
            # 3. Відстань між кульками a = sqrt(3) * l * sin(alpha)
            a = math.sqrt(3) * l * math.sin(alpha_rad)
            
            # 4. Зв'язок сили F_electric з зарядом: F_electric = (sqrt(3) * k * q^2) / a^2
            # q^2 = (F_electric * a^2) / (sqrt(3) * K)
            q_squared = (F_electric * (a**2)) / (math.sqrt(3) * K)
            
            q = math.sqrt(q_squared)
            
            # Вивід
            print(f"---------------------------")
            print(f"Необхідний заряд q: {q:.2e} Кл")
            print(f"Або в нанокулонах:  {q * 1e9:.2f} нКл")
            
        except ValueError:
            print("Помилка! Будь ласка, вводьте коректні числа.")
            
    
if __name__ == "__main__":
    calculate_charge()