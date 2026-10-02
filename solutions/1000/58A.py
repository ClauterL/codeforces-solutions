s = input().strip()
it = iter(s)
print("YES" if all(c in it for c in "hello") else "NO")
