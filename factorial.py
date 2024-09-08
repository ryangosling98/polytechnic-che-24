def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a non-negative integer: "))
result = factorial(number)
print("The factorial of", number, "is", result)