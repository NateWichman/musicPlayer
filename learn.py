import random
import sys
import os


print("Hello World")

#comment

'''
Multiline Comment
'''

name = "Thing"

print(name, " is a thing")

quote = "\"quotes are possible\""

multi_line_quote = '''this is a string
this is the same string'''

print("%s %s %s" % ('doing this shit like c', quote, multi_line_quote))

print("No newline: ", end="")
print("See this is the same line :D")

print('\n' * 5)
print("just printed five new lines")


grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
        'Bananas']

print('First Item,', grocery_list[0])

grocery_list[0] = 'not juice'

print('First Item: ', grocery_list[0])

#prints from 1 to 3 but not element 3
print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick up kids', 'cash check']

to_do_list = [other_events, grocery_list]

print(to_do_list)
