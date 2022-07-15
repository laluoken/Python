def salom_ber():
    """Salom beruvchi function"""
    print("Assalomu aleykum")

salom_ber
####################
def salom_ber(ism):
    """Foydalanuvchidan ismini qabul qilib unga salom beradi"""
    print(f"Assalomu aleykum hurmatli {ism.title()}")

salom_ber('hasan')
###################
def yosh_hisobla(ism,tugilgan_yil):
    """Foydalanuvchini yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

yosh_hisobla('olim',2005)