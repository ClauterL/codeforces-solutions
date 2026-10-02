n, m = map(int, input().split())
a = list(map(int, input().split()))
pos, t = 1, 0
for x in a: t += (x - pos) % n; pos = x
print(t)
