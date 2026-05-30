import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Problem 17.16")
print()

print("ψ(r) = A exp(-r² / (2a²))")
print()

print("Normalization:")
print("∫ 4πr²|ψ|² dr = 1")
print("A = 1 / (π^(3/4) a^(3/2))")
print()

print(f"π^(3/4) = {math.pi**(3/4):.4f}")

print()
print("Most probable radius:")
print("r_mp = a")