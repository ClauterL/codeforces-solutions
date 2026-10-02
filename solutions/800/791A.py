a, b = map(int, input().split())
y = 0
while a <= b: a, b, y = a * 3, b * 2, y + 1
print(y)
