
class Odam:
    gentra = 'Gentra 1.5'
    malibu = 'Malibu 2 turbo'
    tracker = 'Tracker 2'

    def __init__(self, name, age):
        self.ism = name
        self.yosh = age

    def mashinalar_r(azam_uchun):
        print('Bizdagi mashinalarquyidagilar: \n {}, {}, {}'.format(
            azam_uchun.gentra,
            azam_uchun.malibu,
            azam_uchun.tracker
        ))

    def salomlash(self): #Classni ichidagi funksiyalar methodlar deyiladi
        print('Hello {}'.format(self.ism))
        print('Sening yoshin {}da'.format(self.yosh))

# j_a = Odam("A'zam", 18)
m_b = Odam("Boburbek", 24)
m_b.gentra = 'KIA 5'
del m_b.gentra
m_b.mashinalar_r()
del m_b.gentra
m_b.mashinalar_r()
print(m_b.gentra)

#
# j_a.salomlash()
# m_b.salomlash()


# class MoshinaGM:
#     def __init__(self, model):
#         self.company = "GM"
#         self.model = model
#
#     def salomlash(self):  # Classni ichidagi funksiyalar methodlar deyiladi
#         print('Hello GM')
#         print('BU model nomi {}'.format(self.model))
#
#
# gentra_1_5 = MoshinaGM("Gentra 1.5 legendarniy kotta bollan moshinasi")
# kia_8 = MoshinaGM("Tracker")
#
# gentra_1_5.salomlash()
# kia_8.salomlash()
#
#
#
