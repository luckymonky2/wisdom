import math

def calculator():
    print("Standard Calculator (Supports +, -, *, /, sin, cos, tan, radical)")
    try:
        while True:
            op = input("Enter operation (+, -, *, /, sin, cos, tan, radical, exit): ").lower()

            if op == "exit":
                print("Exiting the calculator.")
                break

            binary_ops = ["+", "-", "*", "/"]
            unary_ops = ["sin", "cos", "tan", "radical"]

            if op in binary_ops:
                numbers = []
                while True:
                    number = input("Enter number or '=' to calculate: ")
                    if number == "=":
                        if len(numbers) < 2:
                            print("Enter at least 2 numbers.")
                            continue
                        break
                    try:
                        num = float(number)
                        numbers.append(num)
                    except ValueError:
                        print("Enter valid numbers only!")
                        continue

                result = numbers[0]
                for num in numbers[1:]:
                    if op == "+":
                        result += num
                    elif op == "-":
                        result -= num
                    elif op == "*":
                        result *= num
                    elif op == "/":
                        if num == 0:
                            print("Division by zero is not allowed.")
                            break
                        result /= num

                expression = f" {op} ".join(map(str, numbers))
                print(f"{expression} = {result}")

            elif op in unary_ops:
                number = input("Enter number: ")
                try:
                    num = float(number)
                    if op == "sin":
                        result = math.sin(math.radians(num))
                    elif op == "cos":
                        result = math.cos(math.radians(num))
                    elif op == "tan":
                        result = math.tan(math.radians(num))
                    elif op == "radical":
                        if num < 0:
                            print("Cannot take square root of a negative number.")
                            continue
                        result = math.sqrt(num)
                    print(f"{op}({num}) = {result}")
                except ValueError:
                    print("Invalid input for function.")
                    continue

            else:
                print("Please enter a valid operator.")

    except Exception as e:
        print(f"Invalid operation: {e}")

    print("Developed by: Hikmaese $ Hikma")

calculator()
