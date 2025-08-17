def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result = result * i
        return result

sample_value = int(input("Enter a number: "))

print(f"Factorial of {sample_value} is {factorial(sample_value)}")



