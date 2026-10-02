c = sum(1 for ch in input().strip() if ch in "47")
print("YES" if c in (4, 7) else "NO")
