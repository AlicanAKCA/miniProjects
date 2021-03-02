#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Fonksiyonlar 

# In[6]:


def toplama(*sayılar):
    
    toplam = 0
    print(type(sayılar))
    
    for sayı in sayılar:
        toplam = toplam + sayı
    return toplam
    
print(toplama(1,2,3,4,5,6,7,8,9))


# In[3]:


def ehliyet(yas,isim):
    if (yas <18):
        print(f"{isim} {yas} yaşında olduğundan ehliyet alamaz. Alabilmesine {18 - yas} yıl var.")
    else: 
        print(f"{isim}, ehliyet alabilir.")
    return yas,isim

ehliyet(int(input()),input())


# In[4]:


def epicFunction(*args, **kwargs):
    print(args)
    print(kwargs)

epicFunction(1, 2, 3, 4, 5, 6, 7, key1 = 'value 1', key2 = 'value 2')


# In[14]:


kareAl =  lambda sayı: sayı ** 2
print(kareAl(2))


# In[16]:


çiftmi = lambda sayı: sayı%2==0
print(çiftmi(10))


# In[ ]:




