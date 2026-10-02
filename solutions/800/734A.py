n = int(input())
s = input().strip()
a, d = s.count("A"), s.count("D")
print("Anton" if a > d else ("Danik" if d > a else "Friendship"))
