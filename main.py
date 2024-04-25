print('Привет! Надеюсь ты ознакомился с правилами игры, Начнем.')
const = '1'
while const == '1':
    print('Введите длину мира:')
    len_world = int(input())
    list_word = list(len_world * ' ')
    list2 = list(len_world * ' ')
    print('Введите номера ячеек, в которых вы бы хотели зародить жизнь:')
    number = input().split()
    for i in number:
        list_word[int(i) - 1] = '#'
        list2[int(i) - 1] = '#'
    print('Введите количество поколений:')
    a = int(input())
    print('0)' + ''.join(list_word))
    for j in range(a):
        for i in range(len(list_word)):
            if i != len(list_word) - 1:
                if list_word[i - 1] == '#' and list_word[i + 1] == '#':
                    list2[i] = ' '
                elif list_word[i - 1] == ' ' and list_word[i + 1] == ' ':
                    list2[i] = ' '
                elif list_word[i - 1] == '#' and list_word[i + 1] == ' ':
                    list2[i] = '#'
                elif list_word[i - 1] == ' ' and list_word[i + 1] == '#':
                    list2[i] = '#'
            elif i == len(list_word) - 1:
                if list_word[i - 1] == '#' and list_word[0] == '#':
                    list2[i] = ' '
                elif list_word[i - 1] == ' ' and list_word[0] == ' ':
                    list2[i] = ' '
                elif list_word[i - 1] == '#' and list_word[0] == ' ':
                    list2[i] = '#'
                elif list_word[i - 1] == ' ' and list_word[0] == '#':
                    list2[i] = '#'
        print(str(j + 1) + ')' + ''.join(list2))
        for i in range(len(list2)):
            list_word[i] = list2[i]
    print('Хотите продолжить играть:')
    print('1) да')
    print('2) нет')
    const = input()
print('До встречи! (для завершения программы введите любой символ)')
input()
