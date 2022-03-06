students = [
    ["Henrik Coppard", 1757444, 65],
    ["Rik Bettenson", 3354141, 49],
    ["Nanete Kitchen", 4765713, 46],
    ["Caleb Enticott", 2711894, 15],
    ["Bernardo Haddick", 7623018, 65],
    ["Kirk Vauter", 4107306, 25],
    ["Lorenzo Josuweit", 6213355, 55],
    ["Nap Swigg", 4606594, 11],
    ["Roldan Brachell", 2525611, 41],
    ["Vince McLeish", 6386185, 17],
    ["Nadiya Ormston", 5434545, 75],
    ["Anabelle McAuliffe", 7797024, 28],
    ["Cordie Melloi", 6143783, 88],
    ["Tabina Carpmile", 1711459, 80],
    ["Craggy Boxhall", 2050500, 39]
]

def boshlash():
    print("Malumotlar tayyor, dastruni boshlash uchun 'Ha' deb yozing!")
    tanlov = input("Tanlov: ")
    print(tanlov)

    malumot_olish(tanlov)



def malumot_olish(tanlov):
    while str(tanlov).lower() != 'ha':
        # print(tanlov)
        print("Xato ma'lumot kiritdingiz, iltimos boshidan kirgizing!")
        boshlash()

    print('Siz qaysi soha boyicha sortirovka qilasiz?\n1. Ism boyicha\n2. Ball boyicha\n3. Telefon raqam boyicha\n shu raqamlardan birini tanlang:\n')
    s_option = input('Tanlav raqamini kiriting: ')
    # while str(s_option).lower() != '1'or '2' or '3':
    #     s_option = input('Tanlav raqamini kiriting: ')
    option_dispetcher(s_option)


def option_dispetcher(option):
    temp = []
    if option == '1':
        by_name()
    elif option == '2':
        by_mark()
    elif option == '3':
        by_number()

def by_mark():
    students.sort(reverse=True, key=lambda students: students[2])
    for i in students:
        print(i)

def by_name():
    students.sort(key=lambda students: students[0])
    for i in students:
        print(i)

def by_number():
    students.sort(reverse=True, key=lambda students: students[1])
    for i in students:
        print(i)

boshlash()
