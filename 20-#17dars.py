ism = input("Ismingiz nima?\n>>>")
savol = f"salom  {ism.title()}.Yoshingiz nechida\n>>>"
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingiz nechi metr\n>>>")
height = float(height)

####################
son = 1
while son<= 5:
    print(son, end=' ')
    son = son + 1
print('Dastur tugadi')

###################
print("Kiritilga sonni kvadratini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting"
savol += " Daturni to'xtatish uchun'exit' deb yozib qoldiring"
qiymat= ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print('Dastur tugadi')
####################
print("Kiritilga sonni kvadratini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting"
savol += " Daturni to'xtatish uchun'exit' deb yozib qoldiring"
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat))
print("Dastur tugadi")

#################
print("Kiritilga sonni kvadratini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting"
savol += " Daturni to'xtatish uchun'exit' deb yozib qoldiring"
while True :
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat))

#################
son = 0
while son <10:
    son +=1
    if son%2!=0:
        continue
    else:
        print(son)