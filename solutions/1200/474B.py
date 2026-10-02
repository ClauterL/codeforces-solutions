import sys, bisect
from itertools import accumulate
d = sys.stdin.buffer.read().split()
n = int(d[0]); pre = list(accumulate(map(int, d[1:1+n]))); m = int(d[1+n])
print("\n".join(str(bisect.bisect_left(pre, q) + 1) for q in map(int, d[2+n:2+n+m])))
