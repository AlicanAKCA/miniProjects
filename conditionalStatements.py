#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Koşul İfadeleri

# In[2]:


username = input()
password = input()

if (username == "admin"):
    if (password == "admin"):
        print("Merhaba!")
    else:
        print("Yanlış şifre girildi.")
else:
    print("Yanlış kullanıcı adı girildi.")
    


# In[3]:


sayı = int(input('Sayı girin: '))
if sayı > 0:
    print('Sayınız pozitif')
elif sayı < 0:
    print('Sayınız negatif')


# In[5]:


x = input()
y = input()
if (x !=y):
    print("Kelimeler aynı değil")
else:
    print("Kelimeler aynı")


# In[ ]:




