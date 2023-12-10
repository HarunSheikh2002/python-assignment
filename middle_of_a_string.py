# Write a Python function to insert a string in the middle of a string


s1 = input("enter string :-")
s2 = input("enter 2nd string :-")

s3 = s1[:2] + s2 + s1[-2:]

print(s3)