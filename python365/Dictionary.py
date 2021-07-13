'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

# =============================================================================
# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }
# user_input= input('enter the country ')
# print('Type Cancel to stop')
# while user_input!= 'Cancel':
#     
#     user_input= user_input.lower()
#     user_input=user_input.title()
#     if user_input in capitals:
#         print(f'The Capital of {user_input} is {capitals[user_input]}')
#     else:
#         print('data not available')
#     user_input= input('enter the country ')
# =============================================================================

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence 
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}    
'''
# =============================================================================
# a=0
# b=1
# n=12
# d={}
# for i in range(1,n+1):
#     
#     d[i]=a
#     a,b=b,a+b
# print(d)
# =============================================================================
'''
Question 3
Create a dictionary to represent the open, high, low, close share price data 
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
# =============================================================================
# com=['Python DS','PythonSoft','Pythazon','Pybook']
# val=['open', 'high', 'low', 'close']
# prices=[[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
# #c_p=dict(zip(com,prices))
# d={}
# for i in range(len(val)):
#     d[com[i]]=dict(zip(val,prices[i]))
# print(d)
# ============================================================================
# =============================================================================
# import datetime as dt
# today=dt.date.today()
# holi =dt.date(2021, 6, 29)
# delt=holi-today
# =============================================================================
'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should 
be random numbers created from the random module. Can you draw a bar graph of 
the results?
'''
#1st Method
# =============================================================================
# import random
# d={}
# alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',\
#        'U','V','W','X','Y','Z']
# for a in range(len(alpha)):
#     d[alpha[a]]=random.randint(1, 20)
# d=d.items()
# print(d)
# x,y=zip(*d)
# import matplotlib.pyplot as plt
# plt.bar(x,y)
# =============================================================================
#2nd Method
import random
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d={}
for letter in a:
    d[letter]=random.randint(1, 26)
#d=d.items()
print(d)
x,y=zip(*d.items())
import matplotlib.pyplot as plt
plt.bar(x,y)


    