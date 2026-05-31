import sys, math
sys.stdout.reconfigure(encoding='utf-8')

k_B = 1.38e-23
e = 1.6e-19

print("Problem 18.21\n")

T = float(input("Temperature change ΔT (K): "))
mass_ratio = float(input("m*_h / m*_e: "))

dE = (3/4) * k_B * T * math.log(mass_ratio)

print(f"\nΔE_F = {dE:.4e} J ({dE/e*1e3:.2f} meV)")