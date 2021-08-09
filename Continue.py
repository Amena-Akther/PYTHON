"""
The continue statement in Python is used to bring the program control to the beginning of the loop.
The continue statement skips the remaining lines of code inside the loop and start with the next iteration.
It is mainly used for a particular condition inside the loop so that we can skip some specific code for a
particular condition.
"""
i = 0
while(i < 10):
   i = i+1
   if(i == 5):
      continue
   print(i)
"""
OUTPUT:: the value 5 is skipped because we have provided the if condition using with continue statement in 
while loop. When it matched with the given condition then control transferred to the beginning of the while loop 
and it skipped the value 5 from the code.
"""
j=2
while j<=20:
    print(j,end=" ")
    j=j+1
    if j == 10:
        continue