import csv

'''
Все ребята сдали свои проекты и получили оценки на защите, но Хадаров Владимир все прослушал
и просит помочь ему узнать какую оценку за проект он получил. Пожалуйста, подскажите
Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id>

Пока помогали Владимиру увидели, что многие ученики потеряли свои оценки при выкачке с
сайта. Из-за этого нет возможности посмотреть общую статистику. Чтобы избежать путаницы
поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой.
Сохраните данные в новую таблицу с названием student_new.csv
'''

f = open('предпроф\students.csv', encoding='utf8')
f_reader = csv.reader(f, delimiter=',', quotechar='"')
ans = list(f_reader)[1:]

#ищем оценку Хадарова Владимира
for i in ans:
    if 'Хадаров Владимир' in i[1]:
        print(f'Ты получил: {i[-1]}, за проект - {i[2]}')

#ищем средние значения по классам
classes = {}
for i in ans:
    if i[3] not in classes:
        classes[i[3]] = []
    if i[-1].isdigit():
        classes[i[3]].append(int(i[-1]))

#заполняем None средними значениями с округлением
for i in ans:
    if i[-1] == 'None':
        score = round(sum(classes[i[3]]) / len(classes[i[3]]), 3)
        i[-1] = str(score)

#записываем данные в файл
f_write = open('предпроф\student_new.csv', 'w', encoding='utf8')
f_write.write('id,Name,titleProject_id,class,score\n')
for i in ans:
    f_write.write(', '.join(i) + '\n')
f_write.close()
f.close()