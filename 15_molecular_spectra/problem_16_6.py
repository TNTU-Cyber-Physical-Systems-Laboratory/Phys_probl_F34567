import sys
sys.stdout.reconfigure(encoding='utf-8')

R_H = 1.097e7
lam_min = 380e-9
lam_max = 760e-9

print("Problem 16.6\n")

n_start = int(input("Start n (e.g. 3): "))
n_end = int(input("End n (e.g. 20): "))

count = 0

for n in range(n_start, n_end):
    lam = 1 / (R_H * (1/4 - 1/n**2))
    visible = lam_min <= lam <= lam_max

    if visible:
        count += 1

    print(f"n={n}: {lam*1e9:.1f} nm {'← visible' if visible else ''}")

    if lam < lam_min:
        break

print(f"\nVisible lines: {count}")