n = input("ENter your number: ")

while n != "0":
    if n.isdigit():
        print(f"I got: {n}")
    else:
        print("Pls enter number")
    n = input("ENter your number: ")