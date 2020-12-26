from itertools import product

A = input()
B = input()

A_new = [int(i) for i in A.split()]
B_new = [int(i) for i in B.split()]

print(*product(A_new, B_new))
