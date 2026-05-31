import sys, math
sys.stdout.reconfigure(encoding='utf-8')

k_B = 1.38e-23
e = 1.6e-19

print("Problem 18.23\n")

DeltaE = float(input("Band gap (eV): ")) * e
T1 = float(input("T1 (K): "))
T2 = float(input("T2 (K): "))

factor = DeltaE / (2*k_B)
ratio = math.exp(factor*(1/T1 - 1/T2))

print(f"\nR1/R2 = {ratio:.3f}")