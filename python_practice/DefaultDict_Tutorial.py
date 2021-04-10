n = 5
m = 2
first_list = ['a', 'a', 'b', 'a', 'b']
second_list = ['a', 'b', 'c']

from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(i+1)
    
for j in range(m):
    a = input()
    if a in d.keys():
        print(*d[a])
    else:
        print(-1)
