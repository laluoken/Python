mevalar = ['olma', 'uzum', 'anjir', 'shaftoli']
narhlar = [2500, 5000, 8000, 9850]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []
narhlar.remove(2500)
print(narhlar)
narhlar[1] = narhlar[1] + 2000
print(narhlar)

mevalar.insert(2, 'banan')
print(mevalar)

cars = []
cars.append('lacetti')
cars.append('nexia')
cars.append('cobalt')
cars.append('volga')
print(cars)
del cars[2]
print(cars)

bozorlik = ['un', 'moy', "go'sht", 'moy']
mahsulot = bozorlik.pop('un')
print("Men bozordan", mahsulot, "ni sotib oldim")
print("Boshqa mahsulotlar", bozorlik)
