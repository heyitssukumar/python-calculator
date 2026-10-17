def Calculator():
    while True:
        print(f"{'='*20}\n   Calculator \n{'='*20}")
        print("Welcome to the calculator program!")
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please try again!")
            continue
        operator = input("Enter operator (+, -, *, /, %): ")
        num2 = input("Enter second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please try again!")
            continue
        h = input("Do you want to calculate with the previous result? (yes/no): ")
        if operator == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} = {result}")
        elif operator == '-':

            result = num1 - num2
            print(f"The result of {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} = {result}")
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                print(f"The result of {num1} / {num2} = {result}")
        elif operator == '%':
            try:
                result = num1 % num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue

            else:
                print(f"The result of {num1} % {num2} = {result}")
        else:
            print("Invalid operator. Please try again.")
            continue
        if h.lower() == 'yes':
            while True:
                previous_result = result
                operator2 = input("Enter operator (+, -, *, /, %, exit): ")
                operator2 = operator2.lower()
                if operator2  in ['+', '-', '*', '/', '%', 'exit']:
                    if operator2 == 'exit':
                        break
                    else:
                        num3 = input("Enter another number to continue calculation: ")
                        try:
                            num3 = float(num3)
                        except ValueError:
                            print("Invalid input. Please try again!")
                            continue
                        if operator2 == '+':
                            result += num3
                            print(f"The result of previous result {previous_result} + {num3} = {result}")
                        elif operator2 == '-':
                            result -= num3
                            print(f"The result of previous result {previous_result} - {num3} = {result}")
                        elif operator2 == '*':
                                result *= num3
                                print(f"The result of previous result {previous_result} * {num3} = {result}")
                        elif operator2 == '/':
                            try:
                                result /= num3
                            except ZeroDivisionError:
                                print("Error: Division by zero is not allowed.")
                                continue
                            else:
                                print(f"The result of previous result {previous_result} / {num3} = {result}")
                        elif operator2 == '%':
                            try:
                                result %= num3
                            except ZeroDivisionError:
                                print("Error: Division by zero is not allowed.")
                                continue
                            else:
                                print(f"The result of previous result {previous_result} % {num3} = {result}")
                
                else:
                    print("Invalid operator. Please enter a valid operator!")
                    continue            
        elif h.lower() == 'no':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") 
            continue
        if operator2 == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
            


Calculator()