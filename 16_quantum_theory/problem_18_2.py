import sys, math
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

print("Problem 18.2\n")

theta_E = float(input("Einstein temperature θ_E (K): "))
T = float(input("Temperature T (K): "))

x = theta_E / T
ex = math.exp(x)

C_V = 3 * R * x**2 * ex / (ex - 1)**2

print(f"\nθ_E/T = {x:.3f}")
print(f"C_V = {C_V:.4e} J/(mol·K)")