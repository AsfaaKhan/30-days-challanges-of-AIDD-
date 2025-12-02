---
ID: 9
TITLE: Simple Calculator Rich-Questionary UI Implementation
STAGE: green
DATE_ISO: 2025-12-02
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: simple-calculator
BRANCH: main
USER: user
COMMAND: /sp.implement
LABELS: ["implementation", "ui-update", "rich", "questionary"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - calculator.py
TESTS_YAML:
  - Manual tests (Rich/Questionary UI scenarios)
---
### PROMPT TEXT
```
/sp.implement
Here is the improved CLI Calculator with Rich & Questionary UI:

from rich.console import Console
from rich.panel import Panel
import questionary

console = Console()

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

console.print(Panel.fit("🧮 [bold yellow]Rich CLI Calculator[/bold yellow] ✨\n(Type 'Exit' to quit)", style="bold green"))

while True:
    num1 = questionary.text("Enter first number: ").ask()
    if num1.lower() == "exit":
        break

    operator = questionary.select(
        "Choose an operator",
        choices=["+", "-", "*", "/", "Exit"],
    ).ask()

    if operator == "Exit":
        break

    num2 = questionary.text("Enter second number: ").ask()
    if num2.lower() == "exit":
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
    except Exception:
        console.print("[bold red]❌ Invalid Input! Enter numbers only.[/bold red]")
        continue

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

    console.print(Panel(f"🎯 Result: [bold white]{result}[/bold white]", style="bold blue"))

console.print("\n👋 [bold green]Thanks for using Rich Calculator! Goodbye![/bold green]")
```
### RESPONSE TEXT
Updated `calculator.py` with the Rich & Questionary UI. Created PHR for this implementation.
