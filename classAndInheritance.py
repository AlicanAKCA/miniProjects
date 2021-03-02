#!/usr/bin/env python
# coding: utf-8

# # IEU ACM Python'a Giriş - Sınıflar ve Inheritance

# # Class

# In[16]:


class User:
    ip = 'no information'
    # constructor
    def __init__(self, username, password): #self, fonksiyon içindeki username'e ekle demek, yani içinde barındır demektir.
        # attributes
        self.username = username
        self.password = password

u1 = User(str(input()), str(input()))

print(f"Kullanıcı adı: {u1.username}")
print(f"Şifre: {u1.password}")


# # Inheritance

# In[5]:


class Person(): 
       
    # Constructor 
    def __init__(self, fname, lname): 
        self.fname = fname
        self.lname = lname
    
    # To get name 
    def getName(self): 
        return self.fname , self.lname
   
    # To check if this person is an employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
emp1 = Person(str(input()),str(input()))  # An Object of Person 
print(emp1.getName(), emp1.isEmployee()) 

emp2 = Employee(str(input()),str(input())) # An Object of Employee 
print(emp2.getName(), emp2.isEmployee()) 


# In[ ]:




