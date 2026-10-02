n = int(input())
s = input()
print(sum(1 for i in range(1, n) if s[i] == s[i-1]))
