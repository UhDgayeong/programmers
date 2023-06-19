from collections import defaultdict
import sys

n = int(sys.stdin.readline())
members = defaultdict(list)

for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    members[age].append(name)

members = dict(sorted(members.items()))

for m in members:
    for n in members[m]:
        print(m, n)