#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Döngüler

# # For Döngüsü

# In[6]:


sayılar = [1,2,3,4,5]

for sayı in sayılar:
    print(sayı , "Merhaba")


# In[7]:


xkare = [(0,0),(1,1),(2,4),(3,9)]
for x,y in xkare:
    print(f"Fonksiyon {x} ve {y} noktalarından geçer.")


# In[18]:


print("Pozitif sayı girin: ")
sayi = int(input())

if (sayi<0 ):
    print("Pozitif sayı girin: ")
    sayi = int(input())
    
for i in range(2, sayi):
    if (sayi % i == 0):
        asal = False
        break
if asal:
    print("Sayı asaldır.")
else:
    print("Sayı Asal Değildir.")


# # While Döngüsü

# In[21]:


x = 1
while x<=10:
    print(x)
    x+=1
    


# In[ ]:


print("Pozitif sayı girin: ")
sayi = int(input())
while True:
    if (sayi<0 ):
        print("Pozitif sayı girin: ")
        sayi = int(input())


# In[ ]:




