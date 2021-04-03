u = "POULSTAR"
p = "1234"
wrong_time = 0

username = input("Enter username: ")
password = input("Enter password: ")
wrong_time = wrong_time + 1

while wrong_time < 3:
    if username.upper() == u and password == p:
        print("Logged in")
        break
    else:
        print("Enter correct username and password: ", wrong_time)
        username = input("Enter username: ")
        password = input("Enter password: ")
        wrong_time = wrong_time + 1
if wrong_time == 3:
    print("You must wait for 5 minutes")












'''
n = input("ENter your number: ")

while n != "0":
    if n.isdigit():
        print(f"I got: {n}")
    else:
        print("Pls enter number")
    n = input("ENter your number: ")
'''