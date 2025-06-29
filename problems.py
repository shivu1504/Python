#Practice from beginner to advanced

#🧠 Beginner Level Problems
#1.Write a Python program to swap two variables.
a="helloe"
b="world"
print(a,b)
a,b=b,a
print(a,b)

#2.Write a program to check if a number is even or odd.
while True:
    n = int(input("Enter a number: "))

    if n < 0:
        print("The entered number is negative")
    elif n % 2 == 0:
        print("The entered number is even")
    else:
        print("The entered number is odd")

    choice = input("Do you want to check another number? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you! Exiting the program.")
        break

#3.Print the multiplication table of a number.
n=int(input("Enter number which multiplication you want:"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}",end=" ")
j=1
print()
while(j<11):
    print(f"{n}X{j}={n*j}",end=" ")
    j+=1

#4.Find the largest of three numbers.
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if(a>b and a>c):
    print(f"{a} is greatest among [{a},{b},{c}]")
elif(b>c):
    print(f"{b} is greatest among [{a},{b},{c}]")
else:
    print(f"{c} is greatest among [{a},{b},{c}]")

#5.Check if a year is a leap year.

year=int(input("Enter a year:"))
if(year%4==0):
    if(year % 100!=0) or (year%400==0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

#6.Count the number of vowels in a string.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")

#7.Write a function to return the factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


#8.Reverse a given string.
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

#9.Check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


#10.Print Fibonacci series up to n terms.
# Input
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#⚙️ Intermediate Level Problems
#1.Return the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Example
n = int(input("Enter n: "))
print(f"{n}th Fibonacci number is:", fibonacci(n))

#2.Check whether a string is a palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#3.Find the second largest number in a list.
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("Second largest doesn't exist")
else:
    print("Second largest number is:", unique_numbers[-2])

#4.Count the frequency of each character in a string.
string = input("Enter a string: ")
freq = {}

for char in string:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:")
for k, v in freq.items():
    print(f"{k}: {v}")

#5.Remove duplicates from a list without using set().
lst = [int(x) for x in input("Enter numbers: ").split()]
unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List without duplicates:", unique)

#6.Create a simple calculator using functions.
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Undefined"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", subtract(x, y))
elif op == '*':
    print("Result:", multiply(x, y))
elif op == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operator")

#7.Count uppercase and lowercase letters in a string.
string = input("Enter a string: ")
upper = lower = 0

for char in string:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#8.Merge two dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:", merged)

#9.Find common elements in two lists.
list1 = [int(x) for x in input("Enter first list: ").split()]
list2 = [int(x) for x in input("Enter second list: ").split()]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)

#10.Recursively find the sum of digits until a single digit remains.
def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(sum(int(d) for d in str(n)))

num = int(input("Enter a number: "))
print("Single digit sum is:", sum_digits(num))


#🚀 Advanced Level Problems
#1.Create a class for a bank account with deposit/withdraw methods.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")

# Example
acc = BankAccount("Shiv", 1000)
acc.deposit(500)
acc.withdraw(300)

#2.Count lines, words, and characters in a text file.
with open("sample.txt", "r") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
chars = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)

#3.Define a Rectangle class with area and perimeter methods.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Example
r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

#4.Implement a text-based Tic-Tac-Toe game.
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

board = [[" " for _ in range(3)] for _ in range(3)]
turn = "X"

for move in range(9):
    print_board(board)
    row = int(input(f"{turn}'s turn - Enter row (0-2): "))
    col = int(input(f"{turn}'s turn - Enter column (0-2): "))
    if board[row][col] == " ":
        board[row][col] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"{turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Cell already taken. Try again.")
else:
    print_board(board)
    print("It's a draw!")

#5.Create a contact book using dictionary and functions.
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def view_contacts():
    for name, number in contacts.items():
        print(name, ":", number)

def search_contact(name):
    print("Found:", contacts.get(name, "Not Found"))

# Example usage
add_contact("Ravi", "9876543210")
add_contact("Shiv", "9123456789")
view_contacts()
search_contact("Ravi")

#6.Implement binary search.
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Example
lst = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search(lst, 7))

#7.Write a decorator to log function arguments and results.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

add(5, 3)

#8.Overload the + operator for a Point(x, y) class.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print("Sum:", p3)

#9.Solve Tower of Hanoi using recursion.
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)

tower_of_hanoi(3, 'A', 'B', 'C')

#10.Simulate student data using OOP and save to a JSON file.
import json

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def to_dict(self):
        return {"name": self.name, "roll": self.roll, "marks": self.marks}

# Create students
students = [
    Student("Amit", 101, 87),
    Student("Riya", 102, 93),
    Student("Rahul", 103, 78)
]

# Save to JSON
with open("students.json", "w") as f:
    json.dump([s.to_dict() for s in students], f, indent=4)

print("Student data saved to students.json")

