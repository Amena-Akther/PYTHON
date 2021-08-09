var1= "54 "
var2=" 32"
print(var1 + var2)
print(int (var1) + int (var2))
print(10*int (var1) + int (var2))
print(10* str (int (var1) + int (var2)) )
#print(10 * "Hello world\n")

"""
num1=input("Enter First Number:")
num2=input("Enter Second Number:")
sum=int(num1)+int(num2)
print(sum)
print("The Sum is:",sum)
"""
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
result=num1+num2
print("The Sum is:",result)
result=num1-num2
print("The subtract is:",result)
result=num1*num2
print("The multiply is:",result)
result=num1/num2
print("The division is:",result)