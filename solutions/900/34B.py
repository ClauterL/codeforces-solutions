n, m = map(int, input().split())
a = sorted(map(int, input().split()))
print(-sum(x for x in a[:m] if x < 0))
