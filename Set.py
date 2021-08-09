num1={1,2,3,4,5}     # Curly braces set {}
print(type(num1))
print(num1)

num2={1,2,3,4,5,5}          # it output will be {1,2,3,4,5} cz set has no duplicate value
print(num2)

num3= set([4,5,6])                     # Using Set function
# num3.add(7)
# print(num3)
# num3.remove(6)
# print(num3)
print(num3)
print(6 in num3)
print(6 not in num3)

# set Operations
# Union
print(num1 | num3)                      # using union | operator
print(num1.union(num3))                 # using union() method
# Intersection
print(num1 & num3)                      # Using & operator
print(num1.intersection(num3))          # Using intersection() method
# Difference
print(num1-num3)                        # Using subtraction ( - ) operator
print(num1.difference(num3))            # Using difference() method
print(num1.isdisjoint(num3))            # Return True if two sets have a null intersection
print(num1.issubset(num3))              # Report whether another set contains this set
print(num1.symmetric_difference(num3))  # Remove an element from a set , it must be a member of other set
a=num1^num3
print(a)                                # Remove an element from a set , it must be a member of other set