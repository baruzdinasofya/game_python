print('Привет! Надеюсь, ты ознакомился с правилами игры :), введи строку')
str0 = list(input()) #вводится строка
last_index = len(str0) - 1 #последний индекс строки
count = 0 #счетчик живых клеток
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
    print(*str0)
    for k in range(len(str0)):
        if str0[k] != '#':
            count = count + 1
    if count == len(str0):
        print('Упс! Во всех клетках не осталось жизни :(')
        print('(для окончания программы введите любой символ)')
        input()
        break