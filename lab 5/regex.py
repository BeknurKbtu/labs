# ex 1
import re
txt = input()
x = re.search(r"a + b*", txt)
if x:
    print(txt)
else:
    print("Do not match")

# ex 2
import re
txt = input()
x = re.search(r'a + b{2,3}', txt)
if x:
    print(txt)
else:
    print("Does not match")

# ex 3
import re
txt = input()
x = re.search(r'[a-z]+_a[a-z]+', txt)
if x:
    print(x.group())
else:
    print('Not found')

#ex4
import re

txt = input("Enter a string: ")
x = re.search(r"[A-Z][a-z]+", txt)

if x:
    print(x.group())
else:
    print("Not found")

#ex5
import re


txt = input('Write your string: ')

x = re.search(r'a[a-z]*b', txt)

if x:
    print(x.group())
else:
    print('Not found')

#ex6
import re

txt = input("Enter ")

x = re.sub(r"[ ,.]", "|", txt)

print(x)

#ex7
txt = input("Enter word in snake case type: ")

x = ''.join(word.title() for word in txt.split('_'))

print(x)

#ex8
import re

txt = input()

x = re.split(r'(?<=[a-z)(?=[A-Z])', txt)

print(x)

#ex9
import re

txt = input()

x = re.sub(r"([A-Z])", r' \1 ', txt)

print(x)

#ex10
import re

name = input()

x = re.sub('_','', name.title())

print(x)