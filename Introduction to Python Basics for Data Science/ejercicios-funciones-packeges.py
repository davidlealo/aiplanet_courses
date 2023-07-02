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

