cars0 = {
    'model':'lacetti',
    'narxi':'13000$',
    'rangi':'oq',
    'yil':'2015-yil'
}
cars1 = {
    'model':'captiva',
    'narxi':'23000$',
    'rangi':'qora',
    'yil':'2005-yil'
}
cars2 = {
    'model':'malibu',
    'narxi':'13000$',
    'rangi':'kulrang',
    'yil':'2010-yil'
}
cars = [cars0, cars1, cars2]
for car in cars:
    print(f"{car['model'].title()} ,"
        f"{car['rangi']} rang,"
        f"{car['yil']} ,"
        f"{car['narxi']}"
    )
############################
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['c#', 'c']
}
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillrini biladi")
    for til in tillar:
        print(til.upper())

