list1 = [10, 20, 30, 40, 50]          # List
list2 = ("A", "B", "C", "D", "E")     # Tuple
for item in list2:
    print(item)
list3=[["A", 3], ["B", 5], ["C", 7], ["D", 9]]  #List of List
for i, Age in list3:
    print(i, "age is", Age )
"""
Dict1= dict(list3)   # typecasting list to Dictionary
print(Dict1)
"""
# Program to print the sum of the given list.
Num = [10,30,23,43,65,12]
sum = 0
for i in Num:
    sum = sum+i
print("The sum is:",sum)
#  Program to print numbers in sequence.
for i in range(10):
    print(i,end = ' ')

# Program to print table of given number.
n = int(input("\nEnter the number : "))
for i in range(1, 11):
    c = n*i
    print(n, "*", i, "=", c)
# Program to print even number using step size in range().
n = int(input("Enter the number :"))
for i in range(2,n,2):            # range(start,stop,step size)
    print(i)
# program to make a list  then check whether it is a number or not, if number then check it is >6 then print it.
items = [int, float, "JUHI", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
