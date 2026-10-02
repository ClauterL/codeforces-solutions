import sys
d = list(map(int, sys.stdin.read().split()))
print("\n".join("YES" if k * (k + 1) // 2 <= x <= k * (2 * n - k + 1) // 2 else "NO" for n, k, x in zip(d[1::3], d[2::3], d[3::3])))
