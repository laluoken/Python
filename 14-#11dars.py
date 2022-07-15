son = 50
if son<0:
    print("musbat son")
else:
    print("manfiy son")
# yangi projekt
yosh = int(input("Yoshingiz nechida"))
if yosh<=4:
    print("sizga kirish tekin")
elif yosh<=12:
    print("Sizga kirish 5000 som")  
elif yosh<=20:
    print("Sizga kirish 8000 som")
else:
    print("sizga kirish 10000 som")

# yangi projekt
kun = input("bugun kun nima")   
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print("bugun dam olish kuni")
else:
    print("bugu ish kuni")

# yangi projekt
kun = input("bugun kun nima?")
harorat = float(input("havo harorati qanday"))

if kun.lower()== 'yakshanba' and harorat>=30:
    print("cho'milgani kettik")
elif kun.lower()== 'yakshanba' and harorat<=30:
    print("hamma uyda qolsin")

# yangi projekt
osh = 15000
non = True
salat = False

if non and salat:
    osh = osh + 10000
elif non or salat:
    osh = osh + 5000
print(f"jami {osh} so'm")

# yangi projekt
ovqat = 10000
choy = True
salat = False
non = True
kompot = True
assorti =False

if choy:
    print("mijoz choy oldi")
    ovqat = ovqat + 3000
if salat:
    print("mijhoz salat oldi")
    ovqat = ovqat + 1000
if non:
    print("mijhoz non oldi")
    ovqat = ovqat + 7000
if kompot:
    print("mijhoz kompot oldi")
    ovqat = ovqat + 5000
if assorti:
    print("mijhoz assorti oldi")
    ovqat = ovqat + 2000

print(f"umumiy summa {ovqat} bo'ldi")

radiklar = ["mirjahon", "shohjahon", "aziz", "javlon"]

dust = input("Siz do'stlarim ichida bormisiz\n Ismingiz>>>")
if dust.lower() in radiklar:
    print("Ha Siz yuredasiz")
else:
    print("Idi nahhuy yuqal bettan pasholeeee")
