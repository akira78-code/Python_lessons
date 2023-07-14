#Задача 1 машина

# from math import ceil
# print("Введите расстояние, которые проезжает машина за 1 день : ")
# distance_of_day = float(input())
# print('Введите длину маршрута : ')
# distance = float(input())
# print('Количество дней, необходимых для проезда по маршруту -> {}'.format(ceil(distance/distance_of_day)))

#Задача 3 школа

# count_of_klass = 3
# i_klass = 1
# quantity = 0
# print('Введите количисевто ученик в каждом из 3 классов : ')
# while count_of_klass > 0 :
#     print('Введите количество учеников в {} классе'.format(i_klass))
#     temp = int(input())
#     quantity+=temp
#     i_klass+=1
#     count_of_klass-=1
# n_quantity = round(quantity/2)
# print('Наименьшее колличество парт -> {}'.format(n_quantity))

#Задача 5 Вагоны
# from random import randrange
# napravlenie = randrange(0, 2)
# print('Введите номер вагона :')
# n_vagon = int(input())
# print('Введите порядковый номер вагона от головы поезда : ')
# p_vagon = int(input())
# if(napravlenie == 0) : print('Недостаточно информации')
# if(napravlenie == 1 and p_vagon == 1) : print('Количество вагонов в поезде {}'.format(n_vagon))

#задача 7 високосный год
# print('Введите год : ')
# year = int(input())
# if ((year % 4 == 0 or year % 400 == 0) and year % 100 != 0 ) : print('Год високосный')
# else : (print('Год не високосный'))