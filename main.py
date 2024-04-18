print('Привет! Надеюсь, ты ознакомился с правилами игры :), введи количество поколений:')
generation = int(input())   #количество поколений
print('Введите строку:')
str0 = list(input())    #вводится строка
last_index = len(str0) - 1  #последний индекс строки
count = 0   #счетчик живых клеток
while generation != 0 or count == len(str0):
    for i in range(len(str0)):
        if i == 0:
            if str0[last_index] == '#' and str0[i + 1] == '#':
                str0[i] = '_'
            if str0[last_index] == '_' and str0[i + 1] == '_':
                str0[i] = '_'
            if str0[last_index] == '_' and str0[i + 1] == '#':
                str0[i] = '#'
            if str0[last_index] == '#' and str0[i + 1] == '_':
                str0[i] = '#'

        if i == last_index:
            if str0[i - 1] == '#' and str0[0] == '#':
                str0[i] = '_'
            if str0[i - 1] == '_' and str0[0] == '_':
                str0[i] = '_'
            if str0[i - 1] == '_' and str0[0] == '#':
                str0[i] = '#'
            if str0[i - 1] == '#' and str0[0] == '_':
                str0[i] = '#'

        else:
            if str0[i - 1] == '#' and str0[i + 1] == '#':
                str0[i] = '_'
            if str0[i - 1] == '_' and str0[i + 1] == '_':
                str0[i] = '_'
            if str0[i - 1] == '_' and str0[i + 1] == '#':
                str0[i] = '#'
            if str0[i - 1] == '#' and str0[i + 1] == '_':
                str0[i] = '#'
        for k in range(len(str0)):  #проверка, остались ли живые клетки
            if str0[k] == '_':
                count = count + 1
        if count == len(str0):
            print('Упс! Живых клеток не осталось :(')
            print('(для окончания программы введите любой символ)')
            input()
            exit()
    generation = generation - 1
    print(*str0)

if count != len(str0):
    print('Игра окончена, остались живые клетки!')
    print('(для окончания программы введите любой символ)')
    input()