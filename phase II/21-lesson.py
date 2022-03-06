# """
# agar funksiyamiz biror narsa qaytarsa(return) yoki unga qandaydir argument/argumentlar berilsa unda
# nima bo'ladi?
# """
#
# #
# # def hello_decorator(func):
# #     def inner1():
# #         print("before Execution")
# #
# #         returned_value = func(*args, **kwargs)
# #         print("after Execution")
# #
# #         return returned_value
# #
# #     return inner1
# #
# #
# # @hello_decorator
# # def sum_two_numbers(a, b):
# #     print("Inside the function")
# #     return a + b
# #
# #
# # a, b = 1, 2
# #
# # print("Sum =", sum_two_numbers(a, b))
#
# """
# tepada ko'rib turganimizdek xatolik yuz beradi
# """
#
# # def hello_decorator(func):
# #     def inner1(*args, **kwargs):
# #         print("before Execution")
# #
# #         returned_value = func(*args, **kwargs)
# #         print("after Execution")
# #
# #         return returned_value
# #
# #     return inner1
# #
# #
# # @hello_decorator
# # def sum_two_numbers(a, b):
# #     print("Inside the function")
# #     return a + b
# #
# #
# # a, b = 1, 2
# #
# # print("Sum =", sum_two_numbers(a, b))
#
# """
# Endi biz bir nechta dekoratorlarni zanjir qilib ishlatmoqchimiz
# Xo'sh unda qanday bo'ladi?
# """
#
#
# # def decor1(func):
# #     def inner():
# #         x = func()
# #         return x * x
# #
# #     return inner
# #
# #
# # def decor(func):
# #     def inner():
# #         x = func()
# #         return 2 * x
# #
# #     return inner
# #
# #
# # @decor1
# # @decor
# # def num():
# #     return 10
# #
# #
# # print(num())
#
#
# """
# Generatorlar
# yield
#
# funksiya yield kalit so'zini ishlatsa u generatorga aylanadi
#
# """
#
# #
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
# def my_func():
#     return 1
#
# #
# #
# # # Driver code to check above generator function
# # for value in simpleGeneratorFun():
# # #     print(value)
#
#
# """
# Quyida fibonacci seriyasi uchun generator yaratilgan
# """
#
#
# def fib(limit):
#
#     a, b = 0, 1
#
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# x = fib(5)
# # print('Hello')
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# # #
# # print(x.next())
# # print(x.next())
# # print(x.next())
# # print(x.next())
# # print(x.next())
#
# """
# # 0 1 1 2 3
# # x.next()
# # x.next()
# # x.next()
# # x.next()
# # x.next()
# """
# #
# #
# # print("\nUsing for in loop")
# # for i in fib(5):
# #     print(i)
#


x = lambda *items: [x+x for x in items]
print(x(1,3,4,5))






