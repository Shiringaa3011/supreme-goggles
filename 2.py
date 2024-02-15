import csv

'''
Данные из таблицы student.csv необходимо отсортировать по столбцу оценки(score) с помощь
сортировки вставками (В задаче нельзя использовать встроенные функции сортировок!). Из
полученного списка выделите первых 3х победителей из 10 класса. Данные о победителях
необходимо вывести в формате
'''

f = open('предпроф\students.csv', encoding='utf8')
f_reader = csv.reader(f, delimiter=',', quotechar='"')
ans = list(f_reader)[1:]
#сортировка

for i in range(1, len(ans)):
    j_i = 0
    j = i - 1
    k = ans[i]
    while (ans[j][-1] != 'None' and k[-1] != 'None') and (int(ans[j][-1]) < int(k[-1])) and j >= 0:
        ans[j+1] = ans[j]
        j -= 1
    ans[j+1] = k

q = 0
print('10 класс')
for i in ans:
    if i[-2][:2] == '10':
        q += 1
        fio = i[1].split(' ')[1][0] + '.' + i[1].split(' ')[0]
        print(f'{q} место: {fio}')
        print(i[-1])
    if q == 3:
        break