n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sum(1 for x in a if x >= a[k-1] and x > 0))
