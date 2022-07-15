def summa(*sonlar):
    """Kiritlgan sonlar yig'indisini hisoblaydi"""
    return sum(sonlar)

print(summa(2))
print(summa(1,2,3,4,5))
print(summa(6,7,8,9))

###############
def avto_info(kompaniya,model, **malumotlar):
    """Avto haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi functsiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("gm","malubu",rang = 'qora', yil=2018)
avto2 = avto_info("gm","nexia",rang = 'oq', yil=2018, narhi = 10000)