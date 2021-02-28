'''
Q] You are given a list of tuples with each tuple having three elements of the format (a,b,c) where a,b and c are positive integers. 
Create a lambda function that takes three arguments a, b and c and returns the output (a+b)2 +c. 
Use this lambda function on the list of tuples with the Python built in map function to generate a new list of answers of lambda expression.
'''


# Program :

# To take input from the user
values = input("Input three comma seprated numbers : ")
list1 = values.split(",")
tuple1 = tuple(list1)
print('Tuple : ',tuple1)

a = int(tuple1[0])
b = int(tuple1[1])
c = int(tuple1[2])


# Lambda Function
lf = lambda a,b,c : (((a+b)*2)+c)
print("Answer :" ,lf(a, b, c))
