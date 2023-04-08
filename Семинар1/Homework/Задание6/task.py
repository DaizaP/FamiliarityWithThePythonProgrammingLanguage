# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
import random
choise = input('Выберите ручной ввод или автоматический (Ручной/Авто): ')
choise = choise.lower()
while(choise != 'n'):
    if(choise == 'ручной'):
        n = int(input('Введите шестизначный номер билета: '))
        n = str(n)
        if((int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5]))):
            print(n,'->','Yes')
            break
        else:
            print(n,'->','No')
            break
    elif(choise == 'авто'):
        n = random.randint(100000, 999999)
        n = str(n)
        if((int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5]))):
            print(n,'->','Yes')
        else:
            print(n,'->','No')
        while( ( int(n[0])+int(n[1])+int(n[2]) ) != ( int(n[3])+int(n[4])+int(n[5]) ) ):
            n = int(n)
            n = random.randint(100000, 999999)
            n = str(n)
        print(n, '->', 'Yes')
        break
    else:
        choise = input('Я вас не понял. Введите повторно (Ручной/Авто): ')