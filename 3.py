import csv

f = open('предпроф\students.csv', encoding='utf8')
ans = list(csv.reader(f, delimiter=',', quotechar='"'))[1:]

a = input()
while a != 'СТОП':
    f = 1
    for i in ans:
        if i[-3] == a:
            fio = i[1].split(' ')[1][0] + '.' + i[1].split(' ')[0]
            print(f'Проект № {a} делал: {fio} он(а) получил(а) оценку - {i[-1]}.')
            f = 0
            break
    if f:
        print('Ничего не найдено')
    a = int(input())