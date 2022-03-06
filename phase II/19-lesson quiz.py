"""
Quiz
"""

"""
1. filter() ishlatgan holda quyidagi listdan faqat manfiy sonlarni ajrating
"""
lst1 = [12, -1, 9, 8, -0.5, -0.2, -100]
lst2=[]
print(lst2)

"""
2.  filter(), list() va .lower() larni ishlatgan holda berilgan stringdan unli harflarni ajrating
"""
str1="Qishqi 2022-yilgi Olimpiya o'yinlari Xitoyning Pekin shahrida bo'lib o'tmoqda"
lst=[]
print(lst)

"""
3. Quyida berilgan klassga "miqdor" degan atribut bering( __init__ konstruktorida ) va u orqali 
    self.miqdor o'zgaruvchisiga qiymat joriy qiling. Shu klass yordamida 2ta misollar(obyekt) yarating
"""


class Samalyot:
    model = None
    davlat = 0

    def __init__(self, nomi, davlat):
        self.nomi = nomi
        self.kelib_chiqishi = davlat


first_item = None
second_item = None

total = None
print(total)

"""
4. Yaratilgan obyektga qarab osha klassni yarating
"""
np2005 = Nobel("Tinchlik", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)