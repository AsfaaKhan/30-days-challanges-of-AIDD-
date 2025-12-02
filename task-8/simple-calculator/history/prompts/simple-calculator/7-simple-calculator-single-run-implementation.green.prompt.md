---
ID: 7
TITLE: Simple Calculator Single Run Implementation
STAGE: green
DATE_ISO: 2025-12-02
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: simple-calculator
BRANCH: main
USER: user
COMMAND: /sp.implement
LABELS: ["implementation", "code-update"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - calculator.py
TESTS_YAML:
  - Manual tests (single run scenarios)
---
### PROMPT TEXT
```
/sp.implement
Here is the full implementation code:

# Simple CLI Calculator using Python (Single Run)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("=== Simple Calculator ===")

num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ")
num2 = input("Enter second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except:
    print("Invalid input! Please enter numbers only.")
    exit()

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid Operator!"

print("Result:", result)
```
### RESPONSE TEXT
Updated `calculator.py` with the new single-run implementation. All previous tasks marked as complete. Created PHR for the Simple Calculator single-run implementation.
