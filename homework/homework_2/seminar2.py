#Задача 10
# import random
# n = int(input("Введите количество монет на столе : "))
# #20
# rand = random.randrange(0,(n+1))
# storona = round(random.random())
# if storona == 1 :
#     gerb = rand
#     reshka = n-gerb
# else :
#     reshka = rand
#     gerb = n-reshka
# if gerb > reshka : print(f'Всего {n} монет на столе. Из них решкой вверх лежат - {reshka}, а гербом - {gerb}.'
#                              f'Минимальное число монет которые надо перевернуть - {reshka} монет лежащих вверх решкой.')
# else : print(f'Всего {n} монет на столе. Из них решкой вверх лежат - {reshka}, а гербом - {gerb}.'
#                              f'Минимальное число монет которые надо перевернуть - {gerb} монет лежащих вверх гербом.')

#Задача 12
# import random
# import math
# x = random.randrange(0,1001)
# y = random.randrange(0,1001)
# print(f'x - {x}')
# print(f'y - {y}')
# sum = x+y
# print(f'Их сумма - {sum}')
# pr = x*y
# print(f'Их произведение - {pr}')
#
# x1 = (sum - math.sqrt((sum*sum) - 4 * pr))/2
# y1 = sum - x1
# print (f'x = {x1}, y = {y1}')

#Задача 14

# n = int(input("Введите число: "))
# m = 2
# while m < n:
#     print(m, end=' ')
#     m = m * 2

#Задача 1 * Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

# num = (input('Введите число :'))
# if num.count('.') > 0 : num = float(num)
# else : num = int(num)
# #num = 174 #17
# def int_sum(num) :
#     temp_num = num
#     delitel = 0.1
#     count_digit = 0
#     result = 0
#     while temp_num > 0:
#         temp_num = (int(temp_num / 10))
#         delitel *= 10
#         count_digit += 1
#     delitel = int(delitel)
#     while count_digit > 0:
#         result += int(num / delitel) % 10
#         delitel /= 10
#         count_digit -= 1
#     return result
# def float_sum(num) :
#     zero_count = 0
#     result = 0
#     while zero_count != 8:
#         result += int(round(num, 1)) % 10
#         num *= 10
#         if int(round(num, 1)) % 10 == 0: zero_count += 1
#         if int(round(num, 1)) % 10 != 0: zero_count = 0
#     return result
# #0.10000501
#
# if (type(num) == int) :
#     print(int_sum(num))
# if (type(num) == float) :
#     print(float_sum(num))

# #Задача 2
#
# import random
# import time
#
# rand = random.randrange(1,16)
# def inputNumbers(x):
#     count = x
#     predicat_list = list(range(count))
#     for i in predicat_list :
#         predicat_list[i] = input(f"Введите значение {predicat_list[i]} из {len(predicat_list)} : ")
#     return predicat_list
#
# predicat = inputNumbers(rand)
#
# def check_predicat (predicat) :
#     left = 'not ' + '(' + ' or '.join(predicat) + ')'
#     right ='(' + 'not ' + ' and not '.join(predicat) + ')'
#     result = eval(f'{left}' + ' == ' + f'{right}')
#
#     if result == True:
#         print(f"Утверждение истинно")
#     else:
#         print(f"Утверждение ложно")
#
# start = time.time()
# count = 100
# while count != 0 :
#     check_predicat(predicat)
#     count-=1
#
# end = time.time()
# print(f'Время затраченное на выполнение программы - {end} секунд')


# #Задача 3


# import collections
# import itertools
#
# num = int(input("Введите число :"))
# def get_prime_divisors(n): #
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             n /= i
#             yield i
#         else:
#             i += 1
#
#     if n > 1:
#         yield n
#
#
# def calc_product(iterable):
#     acc = 1
#     for i in iterable:
#         acc *= i
#     return acc
#
#
# def get_all_divisors(n):
#     primes = get_prime_divisors(n)
#
#     primes_counted = collections.Counter(primes)
#
#     divisors_exponentiated = [
#         [div ** i for i in range(count + 1)]
#         for div, count in primes_counted.items()
#     ]
#
#     for prime_exp_combination in itertools.product(*divisors_exponentiated):
#         yield calc_product(prime_exp_combination)
#
# list_adv = list(get_all_divisors(num))
# list_adv.sort()
# print(list_adv)