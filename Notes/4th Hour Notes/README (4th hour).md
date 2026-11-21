
<!-- Hour 4 -->

#Example 01
import random
<!-- gives a random number from given limit, last number not included -->
>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
6
>>> random.randint(1, 10)
7
>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
7
#Example 02
>>> 11 = ['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(11)
'lemon'
>>> random.choice(l1)
'ginger'
>>> random.choice(11)
'ginger'
>>> random.choice(l1)
'masala'
>>> random.shuffle(11)
>>> 11
['mint', 'masala', 'ginger', 'lemon']
>>> random.shuffle(11)
>>> 11
['mint', 'ginger', 'lemon', 'masala']

#Example 03
>>> 0.1 +0.1 +0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
<!-- we have to write Decimal before decimal number to get the right answer -->
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

#Example 04
>>> from fractions import Fraction
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)
<!-- this 2 upon 7 -->

#Example 05
>>> setone = {1, 2, 3, 4}
<!-- intersection (common) -->
>>> setone & {1, 3}
{1, 3}
<!-- union (all unique values) -->
>>> setone | {1, 3}
{1, 2, 3, 4}
>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()
>>> type({})
<!-- <class 'dict'>   empty paranthesis nai mila nalke (set()) mila kiunke empty paranthesis dictonary hotay hain, empty set is always denoted like this-->


<!-- printing specific element -->
>>> name = "Anas"
>>> first_char = name[0]
>>> print(first_char)
>>> A

<!-- print a specific word from string -->
>>> name
>>> Muhd Anas
>>> slice_name = name[0:4]
>>>print(slice_name)
>>> Muhd

#Example 06
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[ :7]
'0123456'
<!-- for skipping, the third number represents it, if 2 it means 1 number will be skipped -->
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'

<!-- lower and upper case -->
>>> name
'Muhd Anas'
>>> print(name.lower())
>>> muhd anas
>>> print(name.upper())
>>> MUHD ANAS
>>> name
'Muhd Anas'
<!-- name doesnt change becuz string is immutable-->

>>> name = "   Muhd Anas  "
>>>name
'  Muhd Anas  '
>>> print (name.strip())
Muhd Anas
<!-- strip is used to remove the extra spaces, extremely useful in web development -->

>>>print(name.replace("Muhd", "Muhammad Anas"))
Muhammad Anas
>>>name
'Muhd Anas'

<!-- convert string to list -->
>>> cars = "Merce, Audi, BMW"
>>> print(cars.split(", "))
>>> ['Merce', 'Audi', 'BMW']

>>> name = "Toyota Car"
>>> print(name.find("Car"))
7 
>>> print(name.find("car"))
-1   , when returns -1 it means it was not found

#Example 07
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
<!-- {} they are called placeholders and we can add variables in these -->
>>> order
'I ordered {} cups of {} chai'
>>> print (order.format (quantity, chai_type))
I ordered 2 cups of Masala chai

#Example 08
>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety) )
Lemon Masala Ginger
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety) )
Lemon, Masala, Ginger 