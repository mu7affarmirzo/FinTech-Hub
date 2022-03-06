# def adder_15(a):
#     def adder(b):
#         return a+b
#     return adder
#
# """
# def adder(b):
#     return 15+b
# """
#
# x = adder_15(15)
# """
# x ==>> adder
# def x(b):
#     return 15+b ==>> 75
#
# """
# y = x(60)
# print(y)


def decorator(sdfsdfsdf):
    def wrapper():
        print('Hello')
        sdfsdfsdf()
        print('Bye')
    return wrapper


@decorator(key='Hello')
def my_func():
    print("Bobur")

my_func()

"""
def x():
    print('Hello')
    my_func()
    print('Bye')
"""


"""
fy_func()

==>>

Hello
Bobur
Bye
"""













