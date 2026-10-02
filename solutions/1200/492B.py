n, l = map(int, input().split())
a = sorted(map(int, input().split()))
d = max(max(a[i] - a[i-1] for i in range(1, n)) / 2 if n > 1 else 0, a[0], l - a[-1])
print("%.10f" % d)
