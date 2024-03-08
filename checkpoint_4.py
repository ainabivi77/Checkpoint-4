#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list = ['mis', 'frutas', 'del', 'cesto']
tuple = ('manzana', 'banana', 'naranja', 'uva', 'pera')
float = 2.4
integer = 46

from decimal import Decimal
mi_decimal = Decimal(2.4)

dictionary = {'ab': 12, 'bc': 23, 'cd': 34}

#Exercise 2: Round your float up.

import math

float = 2.40

resultado = math.ceil(float)
print(resultado)


#Exercise 3: Get the square root of your float.


square_root = math.sqrt(float)
print(square_root)

#Exercise 4: Select the first element from your dictionary.

print(dictionary['ab'])

#Exercise 5: Select the second element from your tuple.

second_elemnt = tuple[1]
print(second_elemnt)

#Exercise 6: Add an element to the end of your list.

list.append('verde')
print(list)

#Exercise 7: Replace the first element in your list.

list[0] = 'tus'
print(list)

#Exercise 8: Sort your list alphabetically.
list.sort()
print(list)

#Exercise 9: Use reassignment to add an element to your tuple.

tuple += ('sandía',)

print(tuple)