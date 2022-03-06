# class Car():
#     def __init__(self, model, max_speed, speed_time):
#         self.model = model
#         self.max_speed = max_speed
#         self.speed_time=speed_time
#         # print(my_car.model, my_car.max_speed, my_car.speed_time)
#
#     def car_info(self):
#         print(f"{self.model}'s max speed equal {self.max_speed}, {self.speed_time} seconds is needed for this spead.")
#
# my_car1 = Car("Tucson", 250, 18)
# my_car2 = Car("Gentra", 220, 25)
# my_car3 = Car("Malibu2,turbo", 260, 16)
#
# my_car2.car_info()


# Homework_9
# 1. 🚙 Ulov degan class yarating va u max_tezlik, boshlangich tezlik, tezlanish va ismini o'zgaruvchi argument
# sifatida qabul qilib olsin. a) init method bo'lsin b) boshlangich tezlik berilganda necha sekunda max_tezlikka
# chiqishini aytadigan method yarating.  c) 10ta turli xil obyekt yaratib ularni classning hamma elementlari uchun
# ishlatib koring. 3ta oxirgi obyektni ochiring

# class Machine():
#     def __init__(self, model, max_speed, starting_speed, speed_up):
#         self.model = model
#         self.max_speed = max_speed
#         self.starting_speed = starting_speed
#         self.speed_up = speed_up
#     def time_max(self):
#         time = self.max_speed * self.starting_speed / self.speed_up
#         print(f"For {self.model}, it takes {time} seconds for the max speed.")
#
# my_car1 = Machine("Tucson", 260, 1, 15)
# my_car2 = Machine("Jentra", 220, 1, 18)
# my_car3 = Machine("Malibu2,turbo", 260, 1, 16)
# my_car4 = Machine("Santa-fee", 280, 2, 14)
# my_car5 = Machine("Sonata", 240, 4, 9)
# my_car6 = Machine("Gelik", 280, 1, 8)
# my_car7 = Machine("Gle", 260, 1, 11)
# my_car8 = Machine("Bmw x6", 280, 1, 8)
# my_car9 = Machine("Bmw x7", 280, 1, 7)
# my_car10 = Machine("Tesla", 280, 1, 6)
# my_car1.time_max()
# my_car2.time_max()
# my_car3.time_max()
# my_car4.time_max()
# my_car5.time_max()
# my_car6.time_max()
# my_car7.time_max()
# my_car8.time_max()
# my_car9.time_max()
# my_car10.time_max()


# 2.Doira deb atalgan radiusi: R bo'lgan class yarating va ikkita: osha doiraning yuzini va pirimetrini topadigan methodlar tuzing
# class Circle():
#     def __init__(self, R):
#         self.radius = R
#     def perimetr(self):
#         L = 2 * self.radius * 3.1415
#         print(f"Circle's Perimeter equal for {L}")
#     def area(self):
#         a = 3.1415 * self.radius **2
#         print(f"Circle's Area equal for {a}")
#
# radius = Circle(6)
# radius.area()
# radius.perimetr()

# 3. 🟦Tomonlar a va b bolgan To'rtburchak deb atalgan class yarating.
# Unda yuza va perimetrini topish mumkin bo'lgan methodlar tuzing.
# Shu to'rtburchakka tashqi chizilgan doiraning yuzasini topadigan method yarating
#
# class Rectangle():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def area(self):
#         area_r = self.a * self.b
#         print(f"The area of given rectangle equal for {area_r}")
#     def perimeter(self):
#         perimeter_r = (self.a + self.b) * 2
#         print(f"The perimeter of given rectangle equal for {perimeter_r}")
#     def opisanniy_4ugolnik(self):
#         c = (self.a**2 + self.b**2)**0.5
#         r = c/2
#         area = 2 * 3.1415 * r**2
#         print(f"The area of given rectangle into circle equal for {area}")
# tortburchak = Rectangle(4, 8)
# tortburchak.area()
# tortburchak.perimeter()
# tortburchak.opisanniy_4ugolnik()

class A:
    x = 'Olma'

a1=A()
print(a1.x)

a1.x = 'Nok'
a1.x = 'Gilos'
print(a1.x)
del a1.x
print(a1.x)
del a1.x


















