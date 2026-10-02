n = int(input())
lucky = [x for x in range(1, 1001) if set(str(x)) <= {"4", "7"}]
print("YES" if any(n % x == 0 for x in lucky) else "NO")
