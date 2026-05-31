import sys
sys.stdout.reconfigure(encoding='utf-8')

lam = float(input("lambda (nm): ")) * 1e-9
lam_red = float(input("lambda_red (nm): ")) * 1e-9

if lam >= lam_red:
    fraction = 0.0
else:
    fraction = 1 - lam / lam_red

print("Problem 15.11")
print(f"  lambda = {lam*1e9:.0f} nm")
print(f"  lambda_red = {lam_red*1e9:.0f} nm")

print("  E ~ 1/lambda")
print("  Fraction = 1 - lambda/lambda_red")

print(f"  Fraction = {fraction:.4f} ({fraction*100:.1f}%)")