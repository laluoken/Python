from cmath import sqrt
import math

uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

###########
kvadrat = lambda x,y : x ** y 
print(kvadrat(3 , 2))

###########
def daraja(n):
    return lambda x : x** n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga teng  "
      f"kubi {kub(3)} ga teng")
##########
sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar) 
###############
import random as r

sonlar = r.sample(range(100), 10) 
######################
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x % 2 == 0

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
#####################

mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
harf = "o"
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
##############

mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
print(mevalar2)

list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar))