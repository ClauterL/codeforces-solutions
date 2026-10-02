rows = [input().split() for _ in range(5)]
r, c = next((i, j) for i in range(5) for j in range(5) if rows[i][j] == '1')
print(abs(r - 2) + abs(c - 2))
