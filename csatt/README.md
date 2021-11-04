# csatt
The Concept of Attributes in C #
_________________________________
How is it created?
We can start by defining a simple 'Class'. However, we add Attribute: Attribute to the end of its name so that we can define the attribute. (For example, public string AttExAttribute: Attribute)

I mentioned that we can work with variables. Now a 'Public String'
Let's start with defining. Then, let's say that we will work with the String we created under the Public property of the AttExAttribute item we defined.
...
Adding target and multiple to create attributes
_______________________________________________
Targets allow us to use features such as 'limiting' the Attributes or 'making it specific to a particular element'.
Multi-query enables us to work with another query after typing one query. I will refer to this part with examples.
First, let's add our '[]' (Ctrl + Alt + 8 and Ctrl + Alt + 9) box. With the AttributeUsage (AttributeTargets.Class, AllowMultiple = true) method, we have defined our target display as class and our multi-use feature as true. Let's move on to our example we will use now.
https://miro.medium.com/max/700/1*8CfF7wxF0lr6pSAQWmtkBg.png

Let's create our Student_Affairs class with our class named Student as shown in the figure. I want to introduce the Obsolete attribute in the Student_Affairs class; for dynamically dropping notifications to developers. I will explain how we use it in the next step.
https://miro.medium.com/max/700/1*22A1d_7LoGcdoGi1Mfzd5g.png
Let's add the code in the Main block, Student_Affairs.Reg (student); Let's pay attention to the line that says:
https://miro.medium.com/max/700/1*CnRTeSyeNF8apqRiKVmGIA.png
The obsolete attribute is used in this way. Let's brainstorm a little bit now!

In what situations can we use attributes?
You can leave it as a note that the function you created is an important component of the project. You can make a database connection inside the AttEx attribute and query with the ExString variable and return your notification.
