#!/usr/bin/env python
# coding: utf-8

# In[1]:


2014**14


# In[2]:


2014.0**14


# In[3]:


7 //3


# In[4]:


int(-1.6)


# In[5]:


float(10**2)


# In[6]:


9**19 - int(float(9**19))


# In[7]:


2014.0**14 - 2014**14


# In[8]:


int(float(9**19))


# In[9]:


9**19


# In[10]:


type(7.0)


# In[11]:


ffg = 'Name: {x} Nick: {y}'
values = input('Как ваше имя?')
values2 = input('Ваш ник:')
print(ffg.format(x=values, y=values2))


# In[2]:


Z = input('С помощью этой программы вы сможете перевести часы в минуты')
X = int(input('Введите часы: '))
Y = int(input('Введите минуты: '))
print(X*60 + Y)


# In[3]:


Y = input('Эта программа переводит минуты в часы) Хотите продолжить?')
X = int(input('Введите кол-во минут: '))
print(X // 60)
print(X % 60)


# In[6]:


X = int(input('Сколько минут вы хотите спать? ')) # кол-во минут нужно спать
H = int(input('Который сейчас час? '))
M = int(input('Укажите так-же минуты: '))
H *= 60
z = H + M
y = z + X
print(y // 60)
print(y % 60)


# In[15]:


a = 3
a *= 4


# In[16]:


480/60


# In[21]:


a, b = True, False
((a and b) or ((not a) and (not b)))


# In[23]:


x = 5
y = 10
y > (x * x) or y >= (2 * x) and x < y


# In[24]:


10>25 or 10 >= 10 and 5 < 10 


# In[25]:


a = True
b = False
a and b or not a and not b


# In[36]:


A = int(input('Рекомендация по сну min: '))
B = int(input('Рекомендация по сну max: '))
H = int(input('Щас Аня спит: '))
if B >= H >= A:
    print('Это нормально')
elif B <= H >= A:
    print('Пересып')
else:
    print('Недосып')


# In[40]:


16 % 4 == 0 and 16 % 100 != 0


# In[44]:


x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('Високосный')
else:
    print('Обычный')


# In[48]:


'abc' > 'ab'


# In[49]:


'ac' > 'abc'


# In[50]:


"123" + "42"


# In[67]:


# Прощадь треугольника(формула Герона)
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)


# In[62]:


9**2


# In[63]:


81**0.5


# In[ ]:


(-15,12] (14,17) (19,+8))


# In[79]:


x = int(input())
my_float = float('+inf')
(-15 < x <= 12) or (14 < x < 17) or (19 < x < my_float)


# In[1]:


x = int(input())
my_float = float('+inf')
z = (-15 < x <= 12) or (14 < x < 17) or (19 <= x < my_float)
print(z)


# In[65]:


x1 = float(input())
x2 = float(input())
x3 = input()
if x3 =='mod' and x2 > 0:
    z = x1 % x2
elif x3 == 'pow':
    z = x1 ** x2
elif x3 == 'div' and x2 > 0:
    z = x1 // x2
elif x3 == '+':
    z = x1 + x2
elif x3 == '-':
    z = x1 - x2    
elif x3 == '*':
    z = x1 * x2
elif x3 == '/' and x2 > 0:    
    z = x1 / x2
elif x2 == 0:
    z = "Деление на 0!"
print(z)


# In[13]:


get_ipython().run_line_magic('pinfo2', 'pow')


# In[14]:


pow(10,2)


# In[30]:


divmod(20,3)


# In[68]:


figura = input()
if figura == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
elif figura == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
elif figura == 'круг':
    r = float(input())
    S = 3.14 * (r**2)
print(S)


# In[2]:


a = int(input())
b = int(input())
c = int(input())
if c <= b <= a:
    z1 = a
    z2 = c
    z3 = b
elif b <= c <= a:
    z1 = a
    z2 = b
    z3 = c
elif a <= c <= b:
    z1 = b
    z2 = a
    z3 = c
elif c <= a <= b:
    z1 = b
    z2 = c
    z3 = a
elif b <= a <= c:
    z1 = c
    z2 = b
    z3 = a
elif a <= b <= c:
    z1 = c
    z2 = a
    z3 = b
print(z1)
print(z2)
print(z3)


# In[ ]:


# Программа помогающая роботу правильно произносить кол-во студентов.

rech_robota = '{n} программист{k}'
n = int(input())
if n == 0 or n % 10 == 0 or 5 <= n <=20:
    print(rech_robota.format(n=n, k='ов'))
elif n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
    print(rech_robota.format(n=n, k='ов'))
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(rech_robota.format(n=n, k='а'))
elif n % 10 == 1 or n == 1:
    print(rech_robota.format(n=n, k=''))
else:
    print(rech_robota.format(n=n, k='ов'))


# In[75]:


text = "123456"
l = len(text) + 1 
part_1 = text[0:l//2]
part_2 = text[l//2:]
print (part_1)
print (part_2)


# In[83]:


x = input()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
x4 = int(x[3])
x5 = int(x[4])
x6 = int(x[5])
z1 = x1 + x2 + x3
z2 = x4 + x5 + x6
if z1 == z2:
    print('Счастливый')
else:
    print('Обычный')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




