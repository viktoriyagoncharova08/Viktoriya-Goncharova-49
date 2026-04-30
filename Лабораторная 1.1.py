#Вар1
n = int(input())
k = int(input())
if n == 1 or n == 2:
    print(1)
else:
    m2 = 1
    m1 = 1
    for i in range(3, n + 1):
        c = m1 + k * m2
        m2, m1 = m1, c
    print(m1)
    