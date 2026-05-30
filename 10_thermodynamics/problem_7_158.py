import sys
sys.stdout.reconfigure(encoding='utf-8')

W = float(input("Enter work W (J): "))
T_cold = float(input("T_cold (K): "))
T_hot = float(input("T_hot (K): "))

COP = T_cold / (T_hot - T_cold)

Q_cold = COP * W
Q_hot = Q_cold + W

print("Problem 7.158")
print(f"  W = {W/1e3:.2f} kJ")
print(f"  T_cold = {T_cold:.1f} K, T_hot = {T_hot:.1f} K")

print(f"  COP = {COP:.2f}")
print(f"  Q_cold = {Q_cold:.1f} J ({Q_cold/1e3:.2f} kJ)")
print(f"  Q_hot = {Q_hot:.1f} J ({Q_hot/1e3:.2f} kJ)")