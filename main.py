#range(start, end, step)

# sonlar = list(range(1, 10))
# print(sonlar)

# sonlar2 = list(range(2, 11, 2))
# print(sonlar2)

# sonlar2 = list(range(10, 0, -1))
# print(sonlar2)

# for i in range(0, 10):
#     print('Salom', i)

# daraja = []
# for i in range(1, 11):
#     sq = i ** 2
#     daraja.append(sq)
# print(daraja)

# print('='*10)
# first option

# print('=' * 10)
# print('WIUT BIS')
# print('=' * 10)

#2nd option

# print("==========\n{}\n==========".format("WIUT BIS"))


# daraja = [son for son in range(1, 10)]
# print(daraja)

# toq_sonlar = []
# for i in range(1, 11, 2):
#         toq_sonlar.append(i)
# print(toq_sonlar)

# just_sonlar = []
# for i in range(2, 11, 2):
#         just_sonlar.append(i)
# print(just_sonlar)

# toq_sonlar = [son for son in range(1, 11, 2)]
# juft_sonlar = [son for son in range(2, 11, 2)]
# print(juft_sonlar)


# sum(), max(), min()

# sonlar = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]
#
# print(sum(sonlar))
# print(max(sonlar))
# print(min(sonlar))

# royhatlarni qirqish
# list[start, end, step]


# mevalar = ['olma', 'anor', 'behi', 'anjir', 'shaftoli', 'banan', 'apelsin', 'mandarin']
# # mevalar2 = mevalar[:]
# # mevalar2.append('Kiwi')
# # print(mevalar)
# # print(mevalar2)
#
# # print(mevalar[::])
# # print(mevalar[::2])
# # print(mevalar[1::2])
# # print(mevalar[::-1]) #ongdan capga qarab yuradi
# # print(mevalar[5:])
# # print(mevalar[:5])
# print(mevalar[-2:0:-1])
#
#
# year = 2021
# module_name = "Computer Science Fundamentls"
# print(type(year))
# print(type(module_name))

#------------------------------------------------------------------------------------------


#2 nd month 6th class

#T heme class
# print(type('as'))
#egzemplyar // namuna // example



# class User:
#     name = 'Abror'
#     lastname = 'Abrorov'
#     age = 45
#
#
# user1 = User
# user2 = User
# user3 = User
#
# user3.name = 'Toxir'
#
# print(user1.name)
# print(user2.name)
# this is called izoh or comment // commenting

#--------------------------------------------------------
# __init__() metodi

class User:
    def __init__(self, name, lastname, age, work=None):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.work = work
        self.get_user_info()

    def get_user_info(self):
        print(f"Foydalanuvci ismi: {self.name}, yoshi: {self.age}")

    def get_user_work(self):
        if self.work:
            message = f"Foydalanuvci {self.work} bo'lib ishlaydi!"

        else:
            message: "Ish joyi anketada korsatilgan"
        print(message)

    def __str__(self):
        return f"Foydalanuvchi ismi: {self.name} {self.lastname, yoshi: {self.age}}"

user1 = User('Abror', 'Abrorov', 45, 'konduktor')
user2 = User('Toxir', 'Toxirov', 32)
print(user1.__repr__())
print(user2)


# print(user1.name)
# print(user2.name)
# user1.get_user_info()
# user2.get_user_info()

# print(user1.get_user_work())
# print(dir(user1)) // metodlarni bilb olsa boladi









