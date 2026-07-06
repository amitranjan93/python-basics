# def greet(name):
#     print(f"Welcome to Project Phoenix! {name}")

# names = ["Amit","Rahul","Priya"]
# for name in names:
#     greet(name)

# def square(number):
#     return number*number

# for i in range(1,11):
#     print(square(i))

# def isEven(number):
#     return number % 2 == 0
    
# print(isEven(10))

# def factorial(number):
#     if number == 1:
#         return number
#     return number * factorial(number - 1)

# print(factorial(5))

def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"

for i in range(20):
    print(f"{i} is {is_prime(i)}")