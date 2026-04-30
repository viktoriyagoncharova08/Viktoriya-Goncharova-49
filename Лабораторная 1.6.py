#Вар6
import itertools
n = int(input())
t = 1
for i in range(1, n + 1):
    t *= i  
t *= 2 ** n  
print(t)
for perm in itertools.permutations(range(1, n + 1)):
    for signs in itertools.product([-1, 1], repeat=n):
        result = [perm[i] * signs[i] for i in range(n)]
        print(' '.join(map(str, result)))