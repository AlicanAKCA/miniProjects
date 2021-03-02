#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Operatörler

# In[1]:


a = 2

#a += 5
#a -= 5
#a *= 5       
#a /= 5
#a %= 5
#a //= 5
a **= 5

print(a)


# In[5]:


sayılar = 1,2,3,4,5,6 #tuple
a,b,*c = sayılar

print(f"a: {a} b: {b} c:{c}")
print(type(a) , type(c))
print(c[0])


# In[8]:


a,b = 1,-1

sonuc = (a==b)
sonuc = (a<=b)
sonuc = (a<b)
sonuc = (a!=b)


# In[11]:


sonuc = (True == 1)
sonuc = (False + True + 10)

print(type(sonuc))
print(sonuc)


# In[15]:


x = int(input())
sonuc = 1 < x <3

print(sonuc)


# In[17]:


x = int(input())
sonuc = (x<10) or (x>3)
print(sonuc)


# In[18]:


x = int(input())
sonuc = not(x<1)
print(sonuc)


# In[20]:


print(int(input()) is not int(input()))


# In[23]:


x = ["araba","gemi"]
print("gemi" in x)


# In[ ]:




