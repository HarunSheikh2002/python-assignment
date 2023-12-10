name = input("enter name :- ")
length = len(name)

if length <= 3:
    print("(length should be at least 3")
elif name.endswith("ing"):
    print("ly")
else:
    print("ing")

print(name) 

