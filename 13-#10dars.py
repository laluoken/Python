ism = ['olim', 'mirja', 'elmur', 'toxic']
for nom in ism:
    print(f"Hurmatli {nom} sizni darsga taklif qilamiz")

avtolar = ['cobalt', 'matiz', 'spark', 'nexia', 'bmw']

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

meva = ['uzum', 'olma', 'gilos', 'behi', "o'rik"]
for hhh in meva:
    if hhh == 'olma':
        print(hhh.upper())
    else:
        print(hhh.title())

ism = input('ismingiz nima \n>>>')
if ism.lower() != 'ali':
    print(f"Uzr, {ism.title()} biz Alini kutyabmiz")
else:
    print("Salom, Ali")

javob = float(input("12x6 nechchiga teng \n>>>"))
if  javob!=72:
    print("javobingiz xato")
else:
    print("Javob to'g'ri")

yosh = int(input("yoshingiz nechida\n>>>"))
if yosh == 18:
    print("Siz bizga to'g'ri kelasiz")
else:
    print("Yuqal bettan hali yoshsan")

login = input('yangi login tanlang\n>>>')
if len(login) <=5:
    print("login  5 harfdan kop bolishi shart")
else:
    print("login muvaffaqqiyatli qabul qilindi")

yil = int(input("Tug'lgan yilingizni kiriting"))
if 2020-yil<18:
    print(f"Yoshingiz {2020-yil} da ekan")
    print("Kirish mumkin emas")
else:
    print(f"Yoshingiz {2020-yil} da ekan")
    print("Xush kelibsiz")

yil = int(input("Yoshingizni kiriting>>>"))
if yil>65: print("Siz COVID-19 guruhida ekansiz")
else: print("Siz COVID-19  guruhida emassiz")

x,y = 25, 50
print("x>y") if x>y else print("x<y")