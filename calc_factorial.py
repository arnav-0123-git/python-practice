def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for neg numbers")
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
num = 5
print(f"the factorial of {num} is {calculate_factorial(num)}")