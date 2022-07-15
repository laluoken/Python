# https://unicode-table.com/ru/279F/
# unicode ning asosiy sayti

matn = "men yangi 📱 oldim"
# String bn nimalar qilsak buladi

ism = 'ahmad'
print('mening ismim' " " + ism)

ism = 'ahmad'
familya = 'qayumov'
print(ism + familya)
print(ism + ' ' + familya)

# f-string bn matnlarni qo'llash
ism = 'ahmad'
familya = 'qayumov'
ism_sharif = f"{ism} {familya}"
print(ism_sharif)

ism = 'Brad'
familya = 'Pit'
print(f"Salom mening ismin {ism}. familyam{familya}!")
# Maxsus belgilar

print('hello world')
print('hello \tworld')
print('hello world')
ism = 'ali'
print(ism.upper())
print(ism.title())
print(ism.capitalize())

meva = "     olma      "
print("Men" + meva.lstrip() + "yaxshi ko'raman")
print("Men" + meva.rstrip() + "yaxshi ko'raman")
print("Men" + meva.strip() + "yaxshi ko'raman")

# inputlar bn ishlash
ism = input('ismingizni nima? ')
print('Assalomu aluykum' + " " + ism)

ism = input('ismingizni nima? \n>>>')
print('Assalomu aluykum ' + ism.title())



