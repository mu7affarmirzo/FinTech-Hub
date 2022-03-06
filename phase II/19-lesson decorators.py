"""
Python dasturlash tilida funksiyalar xuddi argument singari boshqa funksiylar yo klasslarga berish/yuborish mumkin

funksiyani biror bir o'zgaruvchida saqlashimiz ham mumkin

funksiya ichida funksiyani qaytarish(return) qilsa bo'ladi

funksiyalarni list, hash va boshqa data strukturalarda saqlashimiz mumkin
"""


# def baqir(text):
#     return text.upper()
# #
# #
# print(baqir('Qalesan'))
# #
# baland_gapir = baqir
# #
# print(baland_gapir('Qalesan'))




# def baqir(text):
#     return text.upper()
#
#
# def pichirla(text):
#     return text.lower()
#
#
# def salomlash(func):
#     # storing the function in a variable
#     yozuv = """Salom, men boshqa funsiya orqali yaratildim"""
#     salomlashish = func(yozuv)
#     # salomlashish = func
#     print(salomlashish)
#
#
# salomlash(baqir)
# salomlash(pichirla)

#
# def qoshuvchi_yaratuvchi(x):
#     def qoshuvchi(y):
#         return x + y
#
#     return qoshuvchi
#
#
# qosh_15 = qoshuvchi_yaratuvchi(15)
#
# print(qosh_15(10))


# kopaytir = qoshuvchi(15, 12)
#
# print(kopaytir(7))


def decorator(func):

    def ichki_funksiya():
        print("Salom, bu funksiya ishlashidan avval")

        func()

        print("Bu funksiya ishlagandan kegin")

    return ichki_funksiya


def asl_funksiya():
    print("Asl funksiyaning ichi")
#
#
# ishlatiladigan_funksiya = decorator(asl_funksiya)
# #
# ishlatiladigan_funksiya()

# @decorator
# def my_func():
#     print("Hello")
#
# my_func()

import time
import math
#
#
def calculate_time(func):

    def inner1(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1
#
#
@calculate_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

#
#
factorial(10)


