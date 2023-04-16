# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
#
# ноутбук
#     12

def rus_letter(text):
    alphabet = set('АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    return not alphabet.isdisjoint(text)


def eng_letter(text):
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return not alphabet.isdisjoint(text)


def score(text):
    count = int()
    for letter in range(len(text)):
        if rus_letter(text) and not eng_letter(text):       # Проверяем, смотреть ли в русский алфавит
            for (key, value) in alphabetRus.items():
                if set(value).intersection(text[letter]):
                    count += int(key)
                    break
        elif eng_letter(text) and not rus_letter(text):     # Проверяем, смотреть ли в английский алфавит
            for (key, value) in alphabetEng.items():
                if set(value).intersection(text[letter]):
                    count += int(key)
                    break
        else:
            print('Некорректное слово')
            break
    return count


alphabetEng = {
    '1': {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'},        # Алфавит. Ключ - очки,
    '2': {'D', 'G'},                                                # значение - буквы. Мне так показалось проще.
    '3': {'B', 'C', 'M', 'P'},
    '4': {'F', 'H', 'V', 'W', 'Y'},
    '5': {'K'},
    '8': {'J', 'X'},
    '10': {'Q', 'Z'}
}
alphabetRus = {
    '1': {'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
    '2': {'Д', 'К', 'Л', 'М', 'П', 'У'},
    '3': {'Б', 'Г', 'Ё', 'Ь', 'Я'},
    '4': {'Й', 'Ы'},
    '5': {'Ж', 'З', 'Х', 'Ц', 'Ч'},
    '8': {'Ш', 'Э', 'Ю'},
    '10': {'Ф', 'Щ', 'Ъ'}
}
# Вводим слово, переводим в верхний регистр, посимвольно засовываем в список
word = list(str(input('Введите ваше слово: ')).upper())
print(''.join(word).title())
print('Очки: ', score(word))
