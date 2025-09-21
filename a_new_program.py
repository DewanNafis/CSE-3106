def calculator(a, b):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = input("Enter operation (+, -, *, /): ")
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
def noting():
    print("this funtion will be deleted soon")

def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("GitHub"))
    print(sum(5, 10))

if __name__ == "__main__":
    main()