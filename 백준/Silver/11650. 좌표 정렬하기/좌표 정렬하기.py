from collections import defaultdict
import sys

n = int(sys.stdin.readline())
dots = defaultdict(list)

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots[x].append(y)

dots = dict(sorted(dots.items(), key = lambda x : x[0]))

for x in dots:
    dots[x].sort()
    for y in dots[x]:
        print(x, y)