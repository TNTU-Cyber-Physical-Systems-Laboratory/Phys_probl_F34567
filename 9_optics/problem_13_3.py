import sys
sys.stdout.reconfigure(encoding='utf-8')

lambda1 = float(input("Enter lambda1 (um): ")) * 1e-6

lambda2 = 14 * lambda1 / 19

print("Problem 13.3")
print(f"  lambda1 = {lambda1 * 1e6:.2f} um")
print("  7th bright fringe (case 1) = 10th dark fringe (case 2)")
print("  => lambda2 = 14 * lambda1 / 19")
print(f"  lambda2 = {lambda2 * 1e9:.1f} nm ({lambda2 * 1e6:.4f} um)")
