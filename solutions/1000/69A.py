n = int(input())
v = [list(map(int, input().split())) for _ in range(n)]
print("YES" if all(sum(col) == 0 for col in zip(*v)) else "NO")
