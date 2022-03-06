"""
Encapsulation/Kapsuladek Himoyalash


_a >> protected member/ himoylangan azo
__a >> private member/ shaxsiy azo

"""
#
# class Asos:
#     def __init__(self):
#
#         # Himoylangan a'zo
#         self._a = 2
# #
# #
# class Voris(Asos):
#     def __init__(self):
#
#         Asos.__init__(self)
#         print("Asos classning himoyalangan azosini chaqirayabmiz: ", self._a)
#
#         # Himoylangan o'zgaruvchini modifikatsiylash:
#         self._a = 3
#         print("Modifikatsiylangan o'zgaruvchini classdan tashqarida: ", self._a)
#
#
# obj1 = Voris()
# obj2 = Asos()
# #
# print("obj1ning himoyalangan azosiga ulanish: ", obj1._a)
# print("obj2ning himoyalangan azosiga ulanish: ", obj2._a)


# class Counter:
#     def __init__(self):
#         self.current = 0
#
#     def increment(self):
#         self.current += 1
#
#     def value(self):
#         return self.current
#
#     def reset(self):
#         self.current = 0
# #
# #
# counter = Counter()

#
# counter.increment()
# counter.increment()
# counter.increment()
# #
# print(counter.value())


# counter.increment()
# counter.increment()
# counter.current = -999
# #
# print(counter.value())


# class Counter:
#     def __init__(self):
#         self._current = 0
#
#     def increment(self):
#         self._current += 1
#
#     def value(self):
#         return self._current
#
#     def reset(self):
#         self._current = 0
# #
# counter = Counter()
# print(counter._current)


# name mangling
class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


class Smth(Counter):
    def __init__(self):
        Counter.__init__(self)

    def get_private(self):
        print(self.__current)


counter = Counter()
counter1 = Smth()
counter1.get_private()
# print(counter.__current)
# counter.__current = 15
# print(counter.__current)
print(counter._Counter__current)






