#!/usr/bin/env python
# coding: utf-8

# In[6]:


# divisible by 7 and multiple of 5, between 1500 and 2700
nl = []
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# In[9]:


for i in range(1500,2701):

    if i%7==0 and i%5==0:

        print("  ",i)


# In[11]:


# This program adds two numbers
num1 = 1500
num2 = 2700
sum = float(1500) + float(2700)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[18]:


# maximum of two numbers
a = 1500
b = 2700
print('maximum number of [1500,2700] is =',(max(a,b)))


# In[25]:


# Python Program for factorial of a number

n = 55
print("Factorial of,num,is", factorial(n))


# In[26]:


# Python3 program to find simple interest
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)
    return si


# In[27]:


simple_interest(1500, 2700, 3900)


# In[28]:


# Python3 program to find compound
def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


# In[29]:


compound_interest(100000, 9.2, 8)


# In[40]:


# Python program to check if the number is an Armstrong number
   
n = int(input("Enter a number: "))

#initialize the sum

s = 0

t = n

while t > 0:

   digit = t % 10

   s += digit ** 3

   t //= 10

if n == s:

   print(n,"is an Armstrong number")

else:

   print(n,"is not an Armstrong number")


# In[42]:


n = int(input("Enter a number: "))

#initialize the sum

s = 0

t = n

while t > 0:

   digit = t % 10

   s += digit ** 3

   t //= 10

if n == s:

   print(n,"is an Armstrong number")

else:

   print(n,"is not an Armstrong number")


# In[46]:


# Python program to find Area of a circle
def findArea(r):
    PI = 3.14
    return PI * (r*r);
print("Area of circle = %.6f" % findArea(6))


# In[48]:


# Python program to display all the prime numbers within an interval

lower = 1500
upper = 2700

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[56]:


# Program to check if a number is prime or not

num = 97

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
       print(num,"is not a prime number")


# In[ ]:




