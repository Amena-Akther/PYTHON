mystr = "International Islamic University Chittagong"

print(len(mystr))
print(mystr[12])         # It means in whole string it will print 12 index string
print(mystr[0:12])
print(mystr[0:13])
print(mystr[0:43])
# print(mystr[70])    //error
print(mystr[0:70])
print(mystr[0:13:2])     # It means in 1st string it will be print one after one letter/skip one letter
print(mystr[0:])         # Here,after 0: it will empty then it assume whole string len
print(mystr[:20])        # Here,before :20 it will empty then it assume 0 index
print(mystr[:])          # Here,: it will empty then it assume whole string len
print(mystr[::])         # Here,:: it will empty then it assume after 2nd : by default 1 & whole string len
print(mystr[-7:])        # Here,-7 will be the last 7 index of string
print(mystr[-4:-2])
print(mystr[39:41])      # Here,previous line & this line both are same
print(mystr[::-1])       # Here,in 3rd section is negative then it will reverse the whole string
print(mystr[:-14:-3])

# Important String Function
print(mystr.isalnum())                   # Here its output will be false cz in the string there is a space
print(mystr.isalpha())                   # Here its output will be false cz in the string there is a space
print(mystr.endswith("Chittagong"))      # Here its output will be True cz in the string it end with ctg
print(mystr.endswith("Islamic"))         # Here its output will be False cz in the string it end with ctg not islamic
print(mystr.count("t"))                  # Here it will count how much 't'in the whole string
print(mystr.capitalize())                # Here if strings 1st letter in small it will be capital letter
print(mystr.find("University"))          # Here if strings it will find university index
print(mystr.lower())                     # Here it will convert whole strings in lower case
print(mystr.upper())                     # Here it will convert whole strings in upper case
print(mystr.replace("University","In"))  # Here it will replace particular string

