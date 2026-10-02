n = int(input())
a = sorted(map(int, input().split()), reverse=True)
total, acc, k = sum(a), 0, 0
while acc * 2 <= total: acc, k = acc + a[k], k + 1
print(k)
