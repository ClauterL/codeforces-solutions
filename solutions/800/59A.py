s = input().strip()
u = sum(1 for c in s if c.isupper())
print(s.upper() if u > len(s) - u else s.lower())
