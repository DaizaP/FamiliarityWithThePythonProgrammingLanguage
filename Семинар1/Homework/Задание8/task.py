# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
chocLength = int(input('Введите длину шоколадки: '))
chocWidth = int(input('И ширину: '))
r = range(chocLength, chocWidth * chocLength, chocLength)
r1 = range(chocWidth, chocWidth * chocLength, chocWidth)
slices = int(input('Введите кол-во долек, которые вы хотите отломить: '))
b = bool(0)
i = 0
while i < len(r):
    if r[i] == slices:
        b = bool(1)
    i += 1

i = 0
while i < len(r1):
    if r1[i] == slices:
        b = bool(1)
    i += 1

print(chocLength, chocWidth, slices, '-> yes' if b else '-> no')

