#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Veri Yapıları ve Objeler

# ## String ve Integer

# In[29]:



name = "Alican"
surname = "Akca"
age = 19
print(name , surname, age)


# # f String

# In[29]:




name = "Alican"
surname = "Akca"
age = 19 
message = f"İsmim {name} {surname} , {str(age)}  yaşındayım."
message2 = "İsmim {0} {1} , {2}  yaşındayım.".format(name,surname,age)
print(message)
print(message2)


# # % String

# In[20]:



name = "Alican"
surname = "Akca"
age = 19 
message = "İsmim %s %s , %s yaşındayım." % (name,surname,age)


# In[46]:


name = "Alican"
surname = "Akca"
age = 19 

# name, surname, age = "alican","akca",19

message = f"İsmim {name} {surname} , {str(age)}  yaşındayım."

print(message.lower())
print(message.upper())
print(message.title())
print(message.capitalize())

result = message.split(" ")
#print(result)
#print(type(result))

result = message.replace(".","...")
#print(message)
#print(result)
#print(type(result))

result = message.index(".")
#print(result)
#print(type(result))


# # Boolean

# In[ ]:



message = f"İsmim {name} {surname} , {str(age)}  yaşındayım."

result = message.isalpha() #isdigit
print(type(result))
print(result)


# # Float

# In[52]:




fakePi = 22/7

print(fakePi)
print(type(fakePi))
print("The fakePi is {f:1.3}".format(f=fakePi))


# # Complex

# In[ ]:



number = complex(1,1)
print(number)
print(type(number))


# # Lists

# In[4]:




epicMessage = "Hello World!".split()
#print(epicMessage)

epicMessage.append("Merhaba")
epicMessage.append("Dünyaaaa!")                   
#print(epicMessage)

epicMessage[3] = "Dünya!"
#print(epicMessage)

epicMessage.remove("Hello")
#print(epicMessage)

epicMessage.pop(0)
#print(epicMessage)

#print(len(epicMessage))
epicMessage.clear()
#print(len(epicMessage))

result = "Mars" in epicMessage
#print(result)

epicList = [1,"bir",True,3.14, 1+1j]
#print(type(epicList[2]))

epicList2 = ["50", 40,False, 2.71, 1-1j]
#print(epicList + epicList2)

numbers = [1,3,5,9,40,8,2,7,40]

numbers.sort()
#print(numbers)

numbers.reverse()
#print(numbers)

#print(numbers.count(7)) # 1 var, 0 yok


# # Tuple
# 

# In[16]:



list = [araba, 3.14, "yüz"]
tuple = (3, 'iki', 2)

print(type(list))
print(type(tuple))

tuple = ('araba','gemi','10') + tuple
print(tuple)

#print(tuple.count('araba'))
#print(tuple.index('10'))

#tuple.append("mehmet")
#tuple.remove("ayşe")


# # Dictionary

# In[23]:


plaka = {"Izmir" : 35 , "İstanbul" : 34 , "Ankara" : 666, "Antalya" : 7}

print(plaka["Ankara"])
plaka["Ankara"] = 6

#plaka.pop("Ankara")

print(plaka["Ankara"])


# In[ ]:


name = input("Adınız: ")
surname = input("Soyadınız: ")
postCode = input("Posta Kodunuz: ")

users = {"ad": name,
        "soyad" : surname,
        "posta kodu" : postCode
        }


# # Set ve Frozenset

# In[34]:


meyveler = {"armut" , "elma"}

meyveler.add("muz")

meyveler.update(["çilek",'muz'])

meyveler.remove('muz')

print(meyveler)

meyveler = frozenset(meyveler)
#meyveler.add('nar')
#meyveler.remove('elma')


# # Bytes

# In[38]:


epicByte = 0b11111111
print(epicByte)

print(f"{epicByte:#b} , {epicByte} 'ın karşılığıdır.'")


# In[ ]:




