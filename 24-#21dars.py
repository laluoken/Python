def bahola (ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"talaba {ism.title()}ning bahosini kiriting")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['hasan', 'husan', 'olim','vali']
baholar = bahola(talabalar)
print(baholar)