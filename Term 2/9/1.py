n = input("ENter your number: ")

s = 0
count = 0
while n != "0":
    if n.isdigit():
        # print(f"I got: {n}")
        s += int(n)
        count += 1   # count = count + 1
        print(f"SUM: {s}, COUNT: {count}")
    else:
        print("Pls enter number")
    n = input("ENter your number: ")

avg = s / count
print(f"Average: {avg}")