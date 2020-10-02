##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
a=""
b=""
c=0
while "admin"!= a or "12345"!=b:
    c=c+1
    a=input("username ").strip()
    b=input("password ").strip()
    if "admin"!= a or "12345"!=b:
        print("Access denied")
    if c==3:
        break
    if "admin"== a and "12345"==b:
        print("Access granted")
