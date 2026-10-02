import sys
d = list(map(int, sys.stdin.read().split()))
print("\n".join(str(k + (k - 1) // (n - 1)) for n, k in zip(d[1::2], d[2::2])))
