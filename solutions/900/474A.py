kb = "qwertyuiopasdfghjkl;zxcvbnm,./"
d = input().strip()
s = input().strip()
sh = -1 if d == "R" else 1
print("".join(kb[kb.index(c) + sh] for c in s))
