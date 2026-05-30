import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Problem 6.104\n")

l = int(input("Enter l (e.g. 1 for p-orbital): "))
s = 0.5

j_values = [abs(l - s), abs(l + s)]

print("\nTotal angular momentum j values:")
for j in sorted(j_values):
    print(f"  j = {j}")

print("\nSpectroscopic notation:")
for j in sorted(j_values):
    print(f"  ^2P_(j={j})")

n_min = int(input("\nEnter minimum n: "))
n_max = int(input("Enter maximum n: "))

print("\nStates:")
for n in range(n_min, n_max + 1):
    for j in sorted(j_values):
        print(f"  n={n}, l={l}, j={j} -> {n}P_{j}")