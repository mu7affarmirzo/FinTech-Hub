# L=[100,200,300,400,500]
# L1=L[2:4]
# print(L1)
# L2=L[1:5]
# print(L2)
# L2.append(L1)
# print(L2)
#
#
# List=[1,6,8,4,5]
# print(List[-4:])
#
# r = lambda q: q * 2
# s = lambda q: q * 3
# x = 2
# x = r(x)
# x = s(x)
# x = r(x)
# print(x)
#
# a = True
# b = False
# c = False
#
# if a or b and c:
#     print("FinTech Innovation Hub")
# else:
#     print("fintech innovation hub")
#
# def my_func(son,str):
#     print(str)
#     return son
#
# a = my_func(True, "A")
# b = my_func(False, "B")
# c = my_func(False, "C")
#
# if not a or b:
#     print(1)
# elif not a or not b and c:
#     print(2)
# elif not a or b or not b and a:
#     print(3)
# else:
#     print(4)
#
# sanoq = 1
# def shuniTop():
#     global sanoq
#
#     for i in (1, 2, 3):
#         # print(sanoq)
#         sanoq += 1
#
#
# shuniTop()
#
# print(sanoq)
#
#
# sanoq = 1
# def shuniTop():
#     return asdasd = 4
#
#     for i in (1, 2, 3):
#         asdasd += 1
#
#
# shuniTop()
# asdasd
#
# print(sanoq)
#
#
#
# sanoqchi = {}
#
# def addToCounter(davlat):
#     if davlat in sanoqchi:
#         sanoqchi[davlat] += 1
#     else:
#         sanoqchi[davlat] = 1
#
#
# addToCounter('Toshkent')
# addToCounter('Andijon')
# addToCounter('Qibray')
#
# print(len(sanoqchi))


# dictionary = {}
# dictionary[1] = 1
# dictionary['1'] = 2
# dictionary[1] += 1
#
# sum = 0
# for k in dictionary:
#     sum += dictionary[k]
#
# print(sum)


def gfg(x, l=[]):
    # print('Before we start {}'.format(l))
    # print(l)
    for i in range(x):
        l.append(i * i)
    print(l)

# print(l)

gfg(2)
gfg(3, [3, 2, 1])

gfg(3)
gfg(4)
gfg(3, [3, 2, 1])
gfg(4)
print(l)

# x = lambda *args: print([i*2 for i in args])
# x(1,5,8,2)
#
# list(map(lambda x: x * 2, range(10)))

# print(list(map(lambda x:x*2, range(10))))


# temp = dict()
# temp['key1'] = {'key1' : 44, 'key2' : 566}
# temp['key2'] = [1, 2, 3, 4]
# for (key, values) in temp.items():
#     print(values, end = "")


# def even(a):
#     new_list = []
#     for i in a:
#         if i % 2 == 0:
#             new_list.append(i)
#     return (new_list)
#
#
# a = [1, 2, 3, 4, 5]
# even(a)
#
# print(list(map(lambda x: x if x % 2 == 0 else None, a)))
# # a = [1,3,34,4,2,41]
#
# print(list(map(lambda i: i%2==0, a)))




# def square(a):
#     new_list = []
#     for i in a:
#         i = i * i
#         new_list.append(i)
#     return (new_list)
#
#
# a = [1, 2, 3, 4, 5]
# square(a)
#
# print(list(map(lambda x:x*x, a)))



# a = "FinTechHub "
# b = 13
# print(a + b)
#
# def my_msg(my_p):
#     print('This is {}'.format(my_p))
#     if my_p > 0:
#         return True
#     else:
#         return False
#
# a = my_msg(1)
# b = my_msg(-10)
# c = my_msg(0)
#
# if a or b and c:
#     print("FinTech Innovation Hub")
# else:
#     print("fintech innovation hub")














