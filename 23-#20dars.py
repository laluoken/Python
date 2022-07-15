def toliq_ism_yasa(ism ="",familya=""):
    """Toliq ism qaytaruvchi functsiya"""
    toliq_ism = f"{ism} {familya}"
    print(toliq_ism)
    return toliq_ism
toliq_ism_yasa("olim", "hasanov")

####################
talaba1 = toliq_ism_yasa("olim","hakimov")
talaba2 = toliq_ism_yasa("hasan","husanov")
print(f"{talaba1} darsga kechikib keldi")
print(f"{talaba2} darsga umuman kelmadi")
####################
def toliq_ism_yasa(ism='',familya='', otasini_ismi=''):
    """toliq ism qaytaruvchi functisya"""
    if otasini_ismi:
        toliq_ism = f"{ism}{otasini_ismi} {familya}"
    else:
        toliq_ism = f"{ism} {familya}"
    return toliq_ism.title()

talaba1 = toliq_ism_yasa("olim", "qoziyev")
talaba2 = toliq_ism_yasa("olim", "hasanov", "odilovich")
#########################
def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'karobka':karobka,
        'yil':yili,
        'narh':narhi
    }
    return avto

print("Saytimizdagi avtolar ro'yhatini shakllantiramiz")
avtolar = []

while True:
    print("\n Quyidagi malumotlarni kiriting" ,end = "")
    kompaniya = input('ishlab chiqaruvchi:')
    model = input("modeli:")
    rangi = input("rangi:")
    karobka = input('Karobka:')
    yil = input("yili:")
    narhi = input("narhi:")
    avtolar.append(avto_info(kompaniya,model,rangi,karobka,yil,narhi))

    javob = input("Yana avto qo'shasizmi yes/no:")
    if javob == 'no':
        break

print("\n Salonimizdagi avtolar:")
for avto in avtolar:
    if avto ['narh']:
        narh = avto['narh']
    else:
        narh = "nomalum"

    print(f"{avto['rangi'].title()} {avto['model'].title()},karobka {karobka} narh{narh} ")


avto1 = avto_info('gm', 'nexia', 'oq','avtomat',2018)
avto2 = avto_info('gm', 'tico', 'yashil','mexanic',2008,15000)
avtolar =[avto1,avto2]
print("online bozorda bor mashinalar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "nomalum"
    print(f"{avto['rangi']} {avto['model']}. narhi:{narh}")

###########################
def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min +=  1
    return sonlar

print(oraliq(0,10))
print(oraliq(10,21))

