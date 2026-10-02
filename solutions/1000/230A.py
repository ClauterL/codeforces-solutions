s, n = map(int, input().split())
d = sorted(tuple(map(int, input().split())) for _ in range(n))
for x, y in d: s = s + y if s > x else -1
print("YES" if s > 0 else "NO")
