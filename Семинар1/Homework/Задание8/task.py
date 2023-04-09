# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
chocLength = int(input('Введите длину шоколадки: '))
chocWidth = int(input('И ширину: '))
slices = int(input('Введите кол-во долек, которые вы хотите отломить: '))
print(chocLength, chocWidth, slices, '-> yes'
if slices % chocWidth == 0 or slices % chocLength == 0 and slices < chocLength * chocWidth else '-> no')
