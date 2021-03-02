#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Hata Yönetimi

# In[3]:


print(a) #=> NameError


# In[4]:


int('a22') #=> ValueError


# In[6]:


print(0/0) #=> ZeroDivisionError


# In[2]:


print('denem'e) #=> SyntaxError


# In[13]:


while True:
    try:
        sayı = float(input())
        break
    except ValueError:
        print("Sayı girmelisiniz.")
        continue


# In[4]:


import re

sifre = str(input())

def parolaKontrol(sifre): # !Aa1 sifre>8
    if len(sifre) <8:
        raise Exception("Şifreniz en az 8 karakter olmalıdır.")
    elif not re.search("[_@$.!$#½&]", sifre):
        raise Exception("Şifreniz en az 1 özel karakter içermelidir.")
    elif re.search("\s",sifre):
        raise Exception("Şifrenizde boşluk bulunmamalıdır.")
    elif not re.search("[0-9]", sifre):
        raise Exception("Şifreniz en az 1 rakam içermelidir.")
    elif not re.search("[A-Z]", sifre):
        raise Exception("Şifreniz en az 1 büyük harf içermelidir.")
    elif not re.search("[a-z]", sifre):
        raise Exception("Şifreniz en az 1 küçük harf içermelidir.")

parolaKontrol(sifre)


# In[ ]:





# In[ ]:




