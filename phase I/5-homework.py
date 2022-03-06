# a = 'orol'
# if a == a[::-1]:
#     print('Togri')
# else:
#     print('notogri')



# def buPalindrom(yozuv):
#     chap_taraf = 0
#     ong_taraf = len(yozuv)-1
#
#     while ong_taraf >= chap_taraf:
#         if yozuv[chap_taraf] != yozuv[ong_taraf]:
#             return False
#
#         chap_taraf   += 1
#         ong_taraf    -= 1
#
#     return True
#
#
# print(buPalindrom('alla'))


def pascal_uchburchagi(n):
    uchburchak_qatori = [1]
    y = [0]
    temp = []

    for i in range(max(n, 0)):
        # print(uchburchak_qatori+y)
        print(uchburchak_qatori)
        # c = 0
        # for l,r in zip(uchburchak_qatori+y, y+uchburchak_qatori):
        #     uchburchak_qatori[c] = (l+r)
        #     c += 1

        uchburchak_qatori=[l+r for l,r in zip(uchburchak_qatori+y, y+uchburchak_qatori)]


    return n>=1

pascal_uchburchagi(6)


# def square_natural(n):
#     for i in range(1,n):
#         if not i*i > n:
#             print(i**2)
#
# square_natural(100)


# def fibonacci_of(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)
#
#
# print([fibonacci_of(n) for n in range(15)])


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")