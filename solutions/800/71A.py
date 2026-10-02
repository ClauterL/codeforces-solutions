n = int(input())
words = [input().strip() for _ in range(n)]
print("\n".join(s if len(s) <= 10 else f"{s[0]}{len(s)-2}{s[-1]}" for s in words))
