'''
Consider the given two list of numbers. 
L1 = [10, 20, 30, 25, 32, 45, 50] and L2 = [80, 70, 78, 55, 62]. 
Write a Python program that will add all the numbers present in 
L1 and assign the sum to a variable S1, similarly, add all the 
numbers present in L2 and assign the sum to a variable S2. 
Select the correct value of (S1 - S2).

'''
l1 = [10, 20, 30, 25, 32, 45, 50]
l2 = [80, 70, 78, 55, 62]

sum_l1 = sum(l1)
sum_l2 = sum(l2)

first_question = (sum_l1 - sum_l2)
print( first_question ) # -133

'''
Difference between Functions and Methods

You might have a question bugging you: 
“Why on Earth do we have both functions and methods, when they practically do the same thing?”

Firstly, let's start with the obvious. There is a clear difference in the syntax:

· A function looks like this: function(something)
· And a method looks like this: something.method()

Namely: a method always belongs to an object 
(e.g., in the x.index(2) method, .index() needed the x object to be applicable), 
while a function doesn’t necessarily depend on a Python object.

All methods are functions, but not all functions are methods!

If this makes no sense to you (yet), don’t you worry. 
I promise, the idea will grow on you as you use Python 
more and more – especially when you start to define your own functions and methods.

'''