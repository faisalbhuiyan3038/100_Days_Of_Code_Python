# Notes from this course categorized by Day

<h2>Table of Contents</h2>

- [Day 4](#day4)


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