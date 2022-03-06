# class Base:
#     def __init__(self,name,age,number, faculty):
#         self.name = name
#         self.age = age
#         self.number = number
#
#
# class Student(Base):
#     def __init__(self,name,age,number, faculty):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.faculty = faculty
#
#
# class Teacher:
#     def __init__(self,name,age,number, subject):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.subject = subject

















# class Talaba:
#
#     # Ibtido
#     def __init__(self):
#         print('Talaba qoshildi')
#
#     # Destruktorni chaqirish
#     def __del__(self):
#         print("Destruktor chaqirildi")
# #
# #
# # obj = Talaba()
# def obj_yaratish():
#     print('Obyekt yaratish...')
#     obj = Talaba()
#     print('funksiya tugadi...')
#     return obj
# #
# #
# print('obj_yaratish() funksiya chaqirilmoqda...')
# obj = obj_yaratish()
# print('Dastur tugadi...')


"""
INHERITANCE/VORISLIK
"""

# class A:
#     def __init__(self):
#         self.a = 13
#
#     print('Hello A')
#
#
# class B(A):
#     print('Hello B')
#
# obj1 = B()
# print(obj1.a)


class Odam:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# x = Odam("Jahongir", "Aliev")
# x.printname()
#
#
# class Talaba(Odam):
#     pass
#
# y = Talaba("Valijon", "Shamsiev")
# y.printname()
# class Talaba(Odam):
#     def __init__(self, id): #Agar parentning __init__i chaqirilmasa, undagi o'zgaruvchilarni ishlatib bolmaydi
#         print(id)
# y = Talaba(17)
# y.printname()

# class Talaba(Odam):
#     def __init__(self, fname, lname):
#         Odam.__init__(self, fname, lname)
# y = Talaba("A'zam","Jo'rayev")
# y.printname()
class Talaba(Odam):
    def __init__(self, fname, lname, year):
        Odam.__init__(self, fname, lname)
        self.bitiruv_yili = year
    def salom(self):
        print('Salom {}'.format(self.firstname))



y = Talaba("Valijon", "Shamsiev",2015)
x = Odam("Valijon", "Shamsiev")
print(y.firstname)
print(y.bitiruv_yili)
# # y = Talaba("Valijon", "Shamsiev", 2015)
# y.printname()
# # y.salom()


"""
KO'P QAVATLI VORISLIK va BOSHQA TURDAGI VORISLIKLAR
"""


# class Asos(object): #object barcha klasslarning asosi hisoblanadi
#
#     # Konstruktor
#     def __init__(self, name):
#         self.name = name
#
#     # ism olish
#     def getName(self):
#         return self.name
#
#
# class Farzand(Asos):
#
#     # Constructor
#     def __init__(self, name, age):
#         Asos.__init__(self, name)
#         # super().__init__(self, name)
#         self.age = age
#
#     # yosh olish
#     def getAge(self):
#         return self.age
#
#
# class Nevara(Farzand):
#
#     # Constructor
#     def __init__(self, name, age, address):
#         Farzand.__init__(self, name, age)
#         # super().__init__(self, name, age)
#         self.address = address
#
#     # address olish
#     def getAddress(self):
#         return self.address
#
#
# g = Nevara("Nurmuhammad", 22, "Toshkent")
# print(g.getName(), g.getAge(), g.getAddress())


# class C(object):
#     def __init__(self):
#         self.c = 21
#
#         # d shaxsiy o'zgaruvchi
#         self.__d = 42
#
#
# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)
#
#
# object1 = D()
# print(object1.d)


# class Ona:
#     mothername = ""
#
#     def mother(self):
#         print(self.mothername)
#
#
# class Ota:
#     fathername = ""
#
#     def father(self):
#         print(self.fathername)
#
#
# class Farzand(Ona, Ota):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
#
#
# s1 = Farzand()
# s1.fathername = "Abdulloh"
# s1.mothername = "Omina"
# s1.parents()

















