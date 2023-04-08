f = int(56)
d = int(56)
# Priority operation
print(f + d)  # 6
print(f - d)  # 7
print(f * d)  # 2
print(round(f / d, 0))  # 3
print(round(f % d, 0))  # 5
print(f // d)  # 4
print(f ** d)  # 1
print("{} - {} - {} - {} - {}".format(f + d, f - d, f * d, f / d, f % d))
username = 'Маша'
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Ильдар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)
