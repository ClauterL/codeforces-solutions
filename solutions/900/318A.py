n, k = map(int, input().split())
odd = (n + 1) // 2
print(2 * k - 1 if k <= odd else 2 * (k - odd))
