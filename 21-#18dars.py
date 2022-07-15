print("Yaqin do'stlaringiz ro'yhatini tuzamiz")
ismlar = []
n=1
while True:
    savol = f"{n}-do'stlaringiz ismini kiriting"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi (ha/yo'q")
    n+=1
    if takrorlash != 'ha':
        break

print("Do'stlaringiz ro'yhati")
for ism in ismlar:
    print(ism.title())

####################
cars = ['lacetti', 'volvo', 'nexia','volvo',  'matiz', 'volvo', 'tico']
car = 'volvo'
while car in cars:
    cars.remove(car)
print(cars)
####################
talabalar = ['hasan','olim','aziz','shokh']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning bahosini kiriting")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
print("kundalik.com ga barcha baholar yuklandi")
