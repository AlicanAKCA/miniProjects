from matplotlib import pyplot as plt
from random import randint
sayi =0
sayi2=0
toplam = 0
ortalama = 0
atimsayisi = 0
plt.title('')
plt.ylabel('Ortalama')
plt.xlabel('Atım Sayısı')
x = []
y = []
while sayi2 <= 10000:
    sayi = 0
    ortalama = 0
    while sayi<=100:
        toplam += randint(1,6)
        sayi +=1
    atimsayisi += 100
    ortalama = toplam /atimsayisi
    y.append(ortalama)
    x.append(atimsayisi)
    sayi2 += 1
print(x)
print(y)
plt.plot(x,y, color = "red")
plt.show()
