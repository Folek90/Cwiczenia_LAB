character_name = 'john'
character_age = '55'

print('There once was a man named ' + character_name + ', ')
print('he was ' + character_age + ' years old.')

character_name = 'Mike'
character_age = '58'

print('He really liked the name ' + character_name +', ', type(character_name)) 


# \n przenosi do nowej linijki
print('Osobne\nZdanie')

# \"teskt"  nadaje cudzysłów w tekscie.

print('tekst \"w cudzyslowie"') 


phrase = "PITERSKY FOLUSNIAK"
print(phrase)

print(phrase + ' IS COOL')

print(phrase.upper().isupper())

print(len(phrase))

print(phrase[0:8])

print(phrase.index('T'))

print(255)

my_num = 7
print(str(my_num) + ' is my favorite numer')

print(round(4.51))

print(pow(4, 3))

from math import *

print(sqrt(7))
'''
name = input('Enter your name: ')
age = input('Enter your age: ')
Country = input('And where are you from? ')
print('Hello '+ name + ', you are ' + age +' and you living in ' +Country+ ' so I see that\n it is country where Ziobro przesladuje Stonoge, is it right?')
'''
print('==========================================================')
'''
num1 = input("Please, enter a number: ")
num2 = input("Please, enter another number: ")
result = int(num1) + int(num2)
print(result)
'''
print('==========================================================')

num1 = input("Please, enter a number: ")
num2 = input("Please, enter another one number: ")
result = float(num1) / float(num2)
print(result)
