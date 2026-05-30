import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Problem 17.38\n")

l = int(input("Enter l (0=s,1=p,2=d): "))

ml_range = range(-l, l + 1)

for ml in ml_range:
    for ms in [0.5, -0.5]:
        print(f"l={l}, ml={ml:+d}, ms={ms:+.1f}")

print(f"\nTotal states: {2 * (2*l + 1)}")