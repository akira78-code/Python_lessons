# #Задача 22
# i = ('M','N')
# n = int(input(f"Введите количество элементов множества {i[0]} : "))
# m = int(input(f"Введите количество элементов множества {i[1]} : "))
#
# def CreateSet (y,j) :
#     print(f"Введите элементы множества {j}")
#     s = []
#     while y > 0 :
#         s.append(int(input()))
#         y-=1
#     return s
#
# S1 = CreateSet(n,i[0])
# S2 = CreateSet(m,i[1])
#
# temp = set.union(set(S1),set(S2))
# result = list(temp)
# result.sort()
# print(result)

#Задача24
# import random
# count_kustov = random.choice(list(range(6,25,3)))
# def urojainost (c) :
#     print(f"Введите урожайность для {c} кустов :")
#     u = []
#     i = 1
#     while c > 0 :
#         u.append(int(input(f"Урожайность {i} куста - ")))
#         c-=1
#         i+=1
#     return u
#
# def MaxKustov(u) :
#     l1 = list(range(0,count_kustov))
#     l2 = list(range(1,count_kustov))
#     l2.append(0)
#     l3 = list(range(2,count_kustov))
#     l3.append(0)
#     l3.append(1)
#     list_result = []
#     for (x,y,z) in zip (l1,l2,l3) :
#         list_result.append(u[x]+u[y]+u[z])
#     list_result.sort()
#     return list_result[count_kustov-1]
# print(MaxKustov(urojainost(count_kustov)))

# Задача 1 необязательная

# num = int(input('Введите цело число : '))
#
# def num_convert (num) ->str :
#     sist = int(input('В какую систему счисления перевести : \n 1. Восьмеричная \n 2. Двоичная \n'))
#     d = {1:8,2:2}
#     io = []
#     while True :
#         io.append(str(num%d[sist]))
#         num = int(num/d[sist])
#         if int(num/d[sist] == 0) :
#             break
#     io.reverse()
#     dv_str = ''.join(io)
#     if d[sist] == 8 :
#         result = '0o'+dv_str
#     else : result = '0b'+dv_str
#     return result
#
# new_num = num_convert(num)
# oct = oct(num) == new_num
# bin = bin(num) == new_num
# print(f'Тест на восьмеричное - {oct}. \nТест на двочиное - {bin}. \nСконвертированное число - {new_num}')

#Задача 2 необязательная

#import re
# n = input("Введите 1 многочлен : ")
# m = input("Введите 2 многочлен : ")
# n = '2x^2 + 4x + 5 + 5x^3 - 3x^2 - 12'
# #m = '5x^3 - 3x^2 - 12 = 0'
# poly_nums_re = re.compile('\d+x\^\d+ [+-] |[+-] \d+x\^\d+')
# print(re.findall(poly_nums_re,n))
# poly_nums_list = re.findall(poly_nums_re,n)
# x_nums_re = re.compile('\d+x [+-] +|[+-] \d+x +|[+-] \d+x$')
# print(re.findall(x_nums_re,n))
# x_nums_list = re.findall(x_nums_re,n)
# i_nums_re = re.compile('[-+] \d+ | \d+ [+-] |^\d+ [-+]|[-+] \d+$')
# print(re.findall(i_nums_re,n))
# i_nums_re_list = re.findall(i_nums_re,n)
#
# def list_to_string(l) :
#     list_string = ''
#     for i in l :
#         list_string+=i
#     return list_string
# #print(list_to_string(poly_nums_list))
# poly_nums_string = list_to_string(poly_nums_list)
#
# def repeat_sum_maker(list,pattern):
#     sum_string = ''
#     for i in list :
#         if i.count(pattern) == 1 :
#             print(i)
#             #sum_string+=list.pop(list.index(i))
#             sum_string +=i
#
#     return sum_string
#
# def repeat_string_polynums(list) :
#     similar_list = []
#     for i in list:
#         degree = re.findall(r'x\^\d+',i)
#         #temp_l = [repeat_sum_maker(list,degree[0])]
#         if similar_list.count(repeat_sum_maker(list,degree[0])) == 1 : pass
#         else : similar_list.append(repeat_sum_maker(list,degree[0]))
#     return similar_list
#
# polynoms_groupping = repeat_string_polynums(poly_nums_list)
#
# def podobie (list) :
#     for i in list :
#         if i.count('+ -') == 1 :
#             i.replace('+ -','-')
#         if i.co
##нифига не получается !

