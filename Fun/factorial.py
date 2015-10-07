def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i - 1)
print(factorial(int(input("Number: "))))
input("Enter to Kill")
