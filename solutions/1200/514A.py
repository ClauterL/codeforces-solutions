s = input().strip()
r = "".join(str(min(int(c), 9 - int(c))) for c in s)
print(("9" if s[0] == "9" else r[0]) + r[1:])
