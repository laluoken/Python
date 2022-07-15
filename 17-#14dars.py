car_0  = {'model':'ferrari','qizil':'matiz' }
print(car_0['model'])
print(car_0['qizil'])
######################
en_uz = {'apple':'olma', 'melo':'qovun', 'banan':'banan'} 
print(en_uz['apple'])
############################
mevalar = {'apple':'10000', 'melo':'5000', 'banan':'4500'}
print(f"apple narxi {mevalar['apple']} so'm")
############################
talaba = {'ism':'shahobiddin bahromov', 'yili':2006, 'yosh':16}
print(f"{talaba['ism'].title()}\
  {talaba['yili']} yilda tug'lgan \
  Hozir {talaba['yosh']} yosh")
talaba['kurs'] = 4
talaba['fakulteti'] = 102
print(talaba)
# bo'sh ro'yhat tuzish 
############################
uquv = {}
uquv['ismi'] = 'shahobiddin bahromov'
uquv['yosh'] = 16
uquv['kurs'] = 4
uquv['fakulteti'] = 102
print(f"Talaba {uquv['ismi'].title()} {uquv['yosh']} yoshda {uquv['kurs']} chi kursda o'qiydi {uquv['fakulteti']} chi fakultet ")
# lug'atlarni o'chirish
talaba = {'ism':'shahobiddin bahromov', 'yili':2006, 'yosh':16}
del talaba['ism']
print(talaba)
# ko'p qatorli ro'yhat tuzish
ism = {
    'shoh':'iphone XR',
    'dosya':'iphone 11',
    'teacher':'12 pro max',
    'afsuski_uzim':'A02'
    }
print(ism)
olma = ism.get('gilos','Bunday meva mavjud emas')
print(olma)