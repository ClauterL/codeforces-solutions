s = input().strip()
n = int(s)
print(n if n >= 0 else max(n, int(s[:-1]), int(s[:-2] + s[-1])))
