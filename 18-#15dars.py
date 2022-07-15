talaba = {
    'ism':'Shahobiddin',
    'familya':'bahromov',
    'yosh':16,
    'sinf':10
}

print(talaba.items())

for kalit,qiymat in talaba.items():
    print(f"kalit:{kalit}")
    print(f"qiymat:{qiymat}\n")

##################
telefon = {
    'shoh':'iphone XR',
    'dosya':'iphone 11',
    'teacher':'12 pro max',
    'afsuski_uzim':'A02'
    }
for k,q in telefon.items():
    print(f"{k}ning telefoni {q}")

#####################
narxlar = {
    'olma':7900,
    'uzum': 5800,
    'banan':10000,
    'gilos':5000
    }
print("do'konda mahsulotlar")
for mahsulot in narxlar.keys():
    print(f"Do'konda {mahsulot}  bor")

bozorlik = ("banan", "uzum", "olma", "gilos")
for mahsulot in  narxlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {narxlar[mahsulot]}")
for buyum in bozorlik:
    if buyum not in narxlar:
        print(f"Iltimos do'koningizga {buyum} ham olib keling ") 

# Sets ro'yhat turi
sets = {'olma', 'gilos', 'olma', 'uzum', 'gilos', 'nok'}
print(sets)
