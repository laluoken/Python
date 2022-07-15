import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        if taxmin<tasodifiy_son:
            print("Men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring!")
        elif taxmin>tasodifiy_son:
             print("Men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring!")
        else:
            break
    return taxminlar
    print(f"Tabriklaymiz! {taxminlar} taxmin bilan topdingiz")


########
def sontop_pc(x=10):
    input(f"1 dan {x} gach son o'ylan va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} taxmin bilan topdim")
    return taxminlar

############
def play(x=10):
    while True:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang")
        yana = int(input("yana o'ynaysizmi? ha(1)/yo'q(0)"))
        if yana != 1:
            break
play()