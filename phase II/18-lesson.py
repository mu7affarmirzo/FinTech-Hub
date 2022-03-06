"""
Build-in Functions

"""

"""
map() berilgan listning har bir elementini berilgan funksiya ichida ishlatib beradi 
"""
# def sanoqchi(a):
#     return (a+1)
# #
# a = map(sanoqchi, [1,3,5,7])
# print(list(a))



"""
filter() iteratsiya qilish mumkin bolgan obyektdan keraksizlarini chiqazish yuborish
"""

# ages = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def sanoqchi(a):
#     return (a+1)
#
# def myFunc(x):
#     if x % 2 == 0:
#         return x
#     else:
#         pass
# #
# juftlar = filter(sanoqchi, ages)
# juftlar1 = map(myFunc, ages)
# #
# print(list(juftlar))
# print(list(juftlar1))
# for x in juftlar:
#   print(x)

"""
zip() ikkita list yoki iteratsiyalash mumkin bolgan obyektlarni juftlaydi
"""

# s1 = [1,2,3,4]
# s2 = [9,8,7,6]
#
# d1 = {1:'A', 2: 'B'}
# d2 = {3:"C", 4: "D"}
# #
# d3 = zip(d1,d2)
# print(list(d3))
#
#
# d3 = zip(d1.values(),d2.values())
# print(list(d3))
#
# d3 = zip(d1.keys(),d2.values())
# print(list(d3))
"""
enumerate() berilgan iteratsiyalash mumkin bolgan obyekt elementlarini raqamlaydi
"""

# names = ["Muzaffarmirzo", "Bobur", "Nurmuhammad", "A'zam"]
# d1 = {1:'A', 2: 'B'}
# names = enumerate(names)
# names = enumerate(d1.values())
# print(list(names))

"""
all() iteratsiylash mumkin bolgan obyektning hamma elementlari True bolsa True qaytaradi bo'lmasa False
"""
# mylist = [True, True, True]
# x = all(mylist)
#
# mydict = {0:"hello", 1:"World"}
# x = all(mydict)
# print(x)
"""
any() Iterabledagi birorta element True bolsa True qaytaradi
"""
# mylist = [1,3,4,9,6,2,43]
# x = any(mylist)
# print(x)

# import time
# # start = time.time()
#
# a = int(input(""))
# start = time.time()
# w = 0
# b = 2 * a
#
# if a == 0:
#     print(w)
# elif a == 1:
#     w = 1
# elif a == 2:
#     w = 1
# else:
#     for i in range(a+1, b):
#         for j in range(2, i//2+1):
#             if i % j == 0 and j!=i:
#                 break
#             elif j==(i//2):
#                 print(i)
#                 w += 1
#
#
# print(w)
# end = time.time()
# print("The time of execution of above program is :", end-start)
