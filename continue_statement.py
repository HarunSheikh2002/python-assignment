"""
continue statement : it will skip the current statement but loop will continue

"""
i = int(input("enter number :-"))

for i in range(10):
    if i == 8:
        continue
    print(i)
