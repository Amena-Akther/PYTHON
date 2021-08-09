Subjects=["C" , "C++" , "OS" , "PYTHON" , "TOC" , "GRAPHICS" , "MATH"]
print(Subjects)
print(type(Subjects))

print(Subjects[3])             # it will number 3 index
# Subjects.reverse()
# print(Subjects)
# Subjects.sort()
# print(Subjects)
print(len(Subjects))
print("GRAPHICS"in Subjects)
print("GRAPHICS"not in Subjects)
print("NM"not in Subjects)
print(Subjects + ["C#"])     # List Concatenation using + operator
print(Subjects * 2)          # List repitation using * operator

# List Slicing
print(Subjects[0:])
print(Subjects[0:7])
print(Subjects[:7])
print(Subjects[:])
print(Subjects[2:])
print(Subjects[:-1])
print(Subjects[::2])             # In List [0(by default):len(by default):2(it will skip one after one index)

# Subjects.append("JAVA")        # It will add java in end of the list
# print(Subjects)
# Subjects.insert(2,"SECURITY")  # It will insert 'security' in number 2 index
# print(Subjects)
# Subjects.remove("OS")
# print(Subjects)
# Subjects.pop()                   # It will pop/delete last element of list
# print(Subjects)
# Subjects.clear()
# print(Subjects)
Subjects1=Subjects.copy()
print(Subjects1)
pos=Subjects.index("TOC")
print(pos)