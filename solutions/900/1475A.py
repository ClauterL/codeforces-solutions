import sys
data = sys.stdin.read().split()
print("\n".join("YES" if int(x) & (int(x) - 1) else "NO" for x in data[1:]))
