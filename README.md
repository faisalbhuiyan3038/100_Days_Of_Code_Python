# Notes from this course categorized by Day

P.S - You can use the Thonny IDE to visualize each step a python code takes while executing. Useful for debugging.

<h2>Table of Contents</h2>

- [Day 4](#day4)
- [Day 5](#day5)
- [Day 6](#day6)

<a name="day4"></a>
<h3>Day 4</h3>
To take an input in python:
```python
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
```

Python uses the Mersenne Twister pseudorandom number generator to generate random numbers.

To use random module, you need to import it first.

```python
import random
```

To generate a random integer numbers in the range of 1 to 10, including 1 and 10:
```python
random.randint(1,10)
```

What is a module?

It is basically reusable code made by the community that we can use to create programs.

To generate random floating point numbers from 0.0 to 1.0. Note: It doesn't include 1 but goes very close to 1.
```python
random_float = random.random()

# to generate float numbers from 0 to, say, 5, just multiply it by 5
random_float*5
# this generates rand nums from 0.00000... - 4.9999999...
```

<h4>Python Lists</h4>
It's used for storing multiple related data together. It is also used to store the order for the items. It can store mixed data types.

```python
fruits = ["Cherry","Apple","Pear"]
```

To count from the end of the list, you use negative indexing:

```python
fruits = ["Cherry","Apple","Pear"]
print(fruits[-1])
# will print Pear

#to add items to end of list
fruits.append("new_fruit")

#to add multiple items 
fruits.extend("new_fruit","new_fruit1")
```

str.split can be used to split the input by a specific divider:
```python
str.split(",")
```

Nested Lists:
```python
fruits = ["Strawberries","Nectarines"]
vegetables = ["spinach","cabbage"]

dirty_dozen = [fruits,vegetables]
```


<a name="day5"></a>
<h3>Day 5</h3>
```python
for fruit in fruits:
```
A loop executes a block of statement multiple times.

Learned that python does not support increment operators like i++. Instead you gotta do this:
```python
count += 1
```

The python round function is used to round a given number to a whole number, or to a specified number of decimal places.
```python
rounded_num = round(25.4)
#rounds to whole number
rounded_num = round(25.4235,3)
#rounds to 3 dp
```

f strings can combine string and variables while printing.
```python
print(f"This will print {num}")
```

for loops can be run in a range of numbers in python.
```python
for number in range(0,10):
    print(number)
#includes 0 and 10: equivalent as below
for number in range(10):
```

you can also make for loops skip a number of steps for every interval.
```python
for number in range(1,10,3):
    print(number)
#first step is 1 then 4 and so on
```

To convert a list to a string, we can use str.join function:
```python
my_list = ['a','b','c']
my_string = ''.join(my_list)
```

To pick a random item from a list, we can use random module:
```python
my_list = ['a','v','d']
random_char = random.choice(my_list)
```

To randomize the items in a list, we can use random module:
```python
my_list = ['a','v','d']
random.shuffle(my_list)
```

<a name="day6"></a>

To create functions in python:
```python
def my_function():
    print("Hello")
```

reeborg's world website for playing games with python code:
<a href="https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json"></a>

In official python documentation, it recommends using spaces over tabs for indentation.
To make it clear, 4 spaces is 1 indent.

A while loop in simple terms: the loop that will keep on going while a certain condition is true. Once it becomes false, the loop breaks.