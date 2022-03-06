"""
Booleans: True False
# """
# # print('olma'=='olma')
# # print(100>75)
# # print(100<75)


# print(bool("Python"))
# print(bool(9))
# print(bool())


if False:
	print("Noto'g'ri")
else:
	print('Bilmadim')
    

# if 15 > 7:
#     print('15 7sonidan katta')
# else:
#     print('Xato')
    
# if True:
#     print("To'gri")
# else:
#     print('Xato')
    
    
# #funksiyalar ham True yoki False qiymat qaytarishi mumkin
def meningFunk() :
    return True

if meningFunk():
    print("1-qiymat")
else:
    print("2-qiymat")


"""
Operatorlar
"""

'''
Arifmetik operatorlari
Tayinlash/Belgilash(qiymat berish)/Assignment operatorlari
Solishtirish/Comparison operatorlari
Mantiqiy operatorlari
Shaxsiyat/Identity operatorlari
Azolik/Membership operatorlari
Bit boyicha/Bitwise operatorlari
'''

""" Arifmetik operatorlar quyidagilar
+
-
*
/
//
% modulo/modulus
**
"""
# print(19//7)
# # print(19%7)
# # print(3**3)



"""Tayinlash belgilash operatorlari
=       x = 5       x = 5
+=      x += 3      x = x + 3 
-=      x -= 3      x = x - 3
*=      x *= 3      x = x * 3
/=      x /= 3      x = x / 3
%=      x %= 3      x = x % 3
//=     x //= 3     x = x // 3
**=     x **= 3     x = x ** 3
&=      x &= 3      x = x & 3 bitwise
|=      x |= 3      x = x | 3 bitwise
^=      x ^= 3      x = x ^ 3 bitwise

"""


"""Solishtirish operatorlar
>
<
==
!=
>=
<=
"""


"""Mantiqiy operatorlar
and    x < 5 and  x < 10
or     x < 5 or  x < 10
not    not
"""

# a = int(input())
# b = int(input())
a = 125
b = 1/3
print(a**b)



x = 6
if not(x < 5 and  x < 10):
    print('Togri')
else:
    print('Yoq')

