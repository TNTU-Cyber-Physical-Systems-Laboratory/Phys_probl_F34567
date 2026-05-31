import sys, math
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

print("Problem 18.9\n")

theta_D = float(input("Debye temperature θ_D (K): "))
T = float(input("Temperature T (K): "))

C_V = (12 * math.pi**4 / 5) * R * (T / theta_D)**3

print(f"\nT/θ_D = {T/theta_D:.4f}")
print(f"C_V = {C_V:.4f} J/(mol·K)")