# a = int(input("sonni kiriting: "))
#
# temp = 0
#
# for x in str(a):
#     print(x)
#     temp += int(x)
# print(temp)

# Ex2
# a = int(input('Sonni kiriting: '))
# if a > 2:
#     for i in range(2,a+1):
#         # print("I soni: {}".format(i))
#         for j in range(2, i):
#             if i%j == 0 and i != j:
#                 # print(j)
#                 print("Murakkab son: {}".format(i))
#                 break
# else:
#     print('Soning 2dan kichik yoki teng')



# a = int(input('Son kiriting: '))
#
# fact_a = 1
#
# for x in range(1, a+1):
#     fact_a *= x
#
# print(fact_a)

# a = int(input('Son kiriting: '))
# reverse_a = str(a)[::-1]
# teskarisi = ''


# a = int(input('Son kiriting: '))
# temp = 11
#
# for i in range(1, a+1):
#     for j in range(1, temp):
#         print("{0}*{1}={2}".format(i,j,i*j))
#     print('\n')

a = int(input('Son kiriting: '))

f0 = 0
f1 = 1
temp = 0

for x in range(a+1):
    print(f0)
    temp = f0 + f1 #3
    f0 = f1 #1
    f1 = temp #2

dil_izhori = "Jonim senga fido bo'lsin O'zbekistonim. Yiroqlarda sog'inching, sevging meni o'rtar ona Vatanim"
#
# for x in dil_izhori.split():
#     if x[0] == 's':
#         print(x)

# for x in dil_izhori.split():
#     if len(x)%2 == 0:
#         print(x)
#         print(len(x))

# a = int(input("sonni kiriting: "))


