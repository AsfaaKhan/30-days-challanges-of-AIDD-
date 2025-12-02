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

console.print(Panel.fit("🧮 [bold yellow]Simple CLI Calculator[/bold yellow] ✨\n(Type 'Exit' to quit)", style="bold green"))

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

console.print("\n👋 [bold green]Thanks for using Simple CLI Calculator! Goodbye![/bold green]")