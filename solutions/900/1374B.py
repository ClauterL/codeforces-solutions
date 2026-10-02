import sys
def f(n): a = (n & -n).bit_length() - 1; m = n >> a; b = max(i for i in range(40) if m % 3**i == 0); return -1 if m != 3**b or a > b else 2 * b - a
print("\n".join(str(f(int(x))) for x in sys.stdin.read().split()[1:]))
