mehmonlar = ['ali', 'vali', 'hasan', 'husan', 'olim']
for mehmon in mehmonlar:
    print('Salom', mehmon)
    print('Hayr', mehmon)

mehmonlar = ['ali', 'vali', 'hasan', 'husan', 'olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon} sizni 10kuni nahorgi oshga taklif etamiz")
    print("hurmat bilan bahromovlr oilasi")

sonlar = list(range(0,11))
for son in sonlar:
    print(f"{son}ning kvadrati {son**2} ga teng")

sonlar = list(range(11))
sonlar_kvadrati =[] 
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("5ta eng yaqin do'stlaringiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-Dostlaringizni ismini kiriting"))
print(dostlar)
