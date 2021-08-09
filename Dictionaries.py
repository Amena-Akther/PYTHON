d1={}
print(type(d1))

StudentId={  "101" :  "Biology",
             "102" : "Physics",
             "103" : "Chemistry",
             "104" : {"1":"Bangla","2":"English","3":"Religion"}}
print(StudentId)
print(StudentId["102"])
print(StudentId["104"])
print(StudentId["104"]["3"])
StudentId["105"]="Math"
print(StudentId)
del StudentId["105"]
print(StudentId)

# Important Dict function

print(StudentId.get("103"))
print(StudentId.get("107","Not a valid key"))
print(StudentId.get("101","Not a valid key"))
StudentId.update({"106":"HM"})
print(StudentId)
print(StudentId.keys())
print(StudentId.values())

# Create a dictionary and take input from the user and return the meaning of the word from the dictionary

Dict = {"ignore":"refuse to take notice of or acknowledge",
        "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions",
        "prejudice":"preconceived opinion that is not based on reason or actual experience"}
print("Enter the Word :")
Data1 = input()
print(Data1, "means :-", Dict[Data1])