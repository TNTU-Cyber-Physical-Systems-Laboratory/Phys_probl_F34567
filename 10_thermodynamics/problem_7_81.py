import sys
sys.stdout.reconfigure(encoding='utf-8')

Q = float(input("Enter heat absorbed Q (J): "))

delta_U = 0  # isothermal process

W = Q - delta_U

print("Problem 7.81")
print(f"  Heat absorbed Q = {Q:.1f} J")
print("  Isothermal process: T = const => delta_U = 0 J")
print(f"  First law: W = Q - delta_U = {W:.1f} J")