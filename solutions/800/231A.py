n = int(input())
print(sum(1 for _ in range(n) if sum(map(int, input().split())) >= 2))
