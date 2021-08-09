# The break is a keyword in python which is used to bring the program control out of the loop.

str = "python"
for i in str:
    if i == 'o':
        break
    print(i);
print("Program Terminated")


# break statement with while loop

j=2
while j<=20:
    if j ==10:
        break
    print(j)
    j=j+1
print("Program Terminated")

# Choice of printing table
n=2
while 1:
    i=1;
    while i<=10:
        print("%d X %d = %d"%(n,i,n*i));
        i = i+1;
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))
    if choice == 0:
        break;
    n=n+1


