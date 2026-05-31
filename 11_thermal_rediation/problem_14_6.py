import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

sigma = 5.67e-8

U = float(input("U (V): "))
I = float(input("I (A): "))
d = float(input("d (m): "))
L = float(input("L (m): "))
epsilon = float(input("epsilon: "))

P = U * I
A = math.pi * d * L

T = (P / (epsilon * sigma * A)) ** 0.25

print("Problem 14.6")
print(f"  P = {P:.2f} W")
print(f"  d = {d*1e3:.3f} mm, L = {L*1e2:.2f} cm")
print(f"  A = pi*d*L = {A:.4e} m^2")
print(f"  epsilon = {epsilon:.3f}")
print(f"  T = {T:.0f} K")