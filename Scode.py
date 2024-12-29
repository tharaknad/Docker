print("********* Welcome to Basic Calculator **********")
print("Enter First value: ")
A = int(input())
print("Enter Second value: ")
B = int(input())

# Perform calculations
Add = A + B
Sub = A - B
Mul = A * B

if A <= 0 and B <= 0:
    print("Please check both values (should be greater than zero).")
else:
    print(f"Addition of both values will be: {Add}")
    print(f"Subtraction of both values will be: {Sub}")
    print(f"Multiplication of both values will be: {Mul}")

    # Handle division separately to avoid division by zero
    if B != 0:
        Div = A / B
        print(f"Division of both values will be: {Div}")
    else:
        print("Division cannot be performed (Second value is zero).")
