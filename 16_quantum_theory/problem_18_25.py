import sys
sys.stdout.reconfigure(encoding='utf-8')

k_B = 1.38e-23
e = 1.6e-19

print("Problem 18.25\n")

T = float(input("Temperature (K): "))
DeltaE = float(input("Energy gap (eV): ")) * e

alpha = -DeltaE / (2*k_B*T**2)

print(f"\nα = {alpha:.4e} K^-1")