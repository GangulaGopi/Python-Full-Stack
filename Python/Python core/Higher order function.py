
#1.  Use map() with a lambda to add 5 to every element of the following nested
# list [[1, 2], [3, 4], [5, 6]]

nested = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: list(map(lambda y: y + 5, x)), nested))
print(result)


##2.  Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50.
d = {"apple": 100, "banana": 40, "cherry": 150}
result = dict(filter(lambda item: item[1] > 50, d.items()))
print(result)

##3.  Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.

from functools import reduce
nums = [3, 7, 2, 9, 5]
largest = reduce(lambda a, b: a if a > b else b, nums)
print(largest)

##4.  What happens if the lambda passed to reduce() accepts only one parameter or three parameters? Explain the output or error.
 #Ans :One parameter: reduce() always passes two arguments, so you’ll get a TypeError.

# Three parameters: reduce() only passes two arguments, so again TypeError.

# Correct usage requires exactly two parameters.

#5.  Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.
s = "Hello"
ascii_values = list(map(lambda ch: ord(ch), s))
print(ascii_values)

#6.  Use filter() to remove all vowels from a string and print the final string.

s = "Programming"
vowels = "aeiouAEIOU"
filtered = ''.join(filter(lambda ch: ch not in vowels, s))
print(filtered)

#7.  Use reduce() to concatenate a list of characters into a single string.
#Example input: ['P', 'y', 't', 'h', 'o', 'n']

from functools import reduce
chars = ['P', 'y', 't', 'h', 'o', 'n']
word = reduce(lambda a, b: a + b, chars)
print(word)

#. 8 Given a list of integers, use map() with id() to print the memory address of each element.
#Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

nums = [10, 350, 10, 350, 20]
addresses = list(map(id, nums))
print(addresses)
#9.  Explain the difference between:
##map(str, [1, 2, 3])
#map(lambda x: str(x), [1, 2, 3])
##Which one is faster and why?

#map(str, ...) directly applies the built-in str function → faster because it avoids the overhead of calling a lambda.

#map(lambda x: str(x), ...) wraps str() inside a lambda → slower but functionally identical.


#10.  Given a list of numbers:
#[5, 10, 15, 20, 25, 30]
#Perform the following in a single pipeline:
#• Use map() to square each number
#• Use filter() to keep only numbers divisible by 5
#• Use reduce() to calculate the sum of remaining number

from functools import reduce

nums = [5, 10, 15, 20, 25, 30]
pipeline = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x**2, nums)
    )
)
print(pipeline)

