#Вар5
s = input().strip()
t = input().strip()
if len(s) > 1000 or len(t) > 1000:
    print("Больше 1 килобазы")
elif len(t) > len(s):
    print("Подстрока длиннее строки")
else:
    p = []
    for i in range(len(s) - len(t) + 1): #индексикация
        if s[i:i + len(t)] == t:
            p.append(i + 1) 

    print(' '.join(map(str, p)))