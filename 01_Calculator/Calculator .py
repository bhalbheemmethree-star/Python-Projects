
History = []

choice = "Y"

while choice == "Y":
    print("==============================")
    print("        CALCULATOR            ")
    print("==============================")
    print("1. Perform Calculation")
    print("2. View History")
    print("3. Clear History")
    print("4. edit history")
    print("5. Exit")
    print("==============================")

    menu = int(input("choose an option:"))

    if menu == 1:

        x = float(input("Enter first number: "))
        operation = input("Enter operation: ")
        y = float(input("Enter second number: "))

        if (operation == "+"):
            result = x+y
            result_text = f"{x} + {y} = {result}"
            History.append(result_text)
            print(f"{x} + {y} = {result}")

        elif (operation == "-"):
            result = x-y
            result_text = f"{x} - {y} = {result}"
            History.append(result_text)
            print(f"{x} - {y} = {result}")

        elif (operation == "*"):
            result = x*y
            result_text = f"{x} * {y} = {result}"
            History.append(result_text)
            print(f"{x} * {y} = {result}")

        elif (operation == "/"):
            if y == 0:
                print("Cannot divisible by zero")
            else:
                result = x/y
                result_text = f"{x} / {y} = {result}"
                History.append(result_text)
                print(f"{x} / {y} = {result}")

        elif (operation == "%"):
            if y == 0:
                print("cannot divisible by zero")
            else:
                result = x%y
                result_text = f"{x} % {y} = {result}"
                History.append(result_text)
                print(f"{x} % {y} = {result}")

        elif (operation == "//"):
            if y == 0:
                print("cannot divisible by zero")
            else:
                result = x//y
                result_text = f"{x} // {y} = {result}"
                History.append(result_text)
                print(f"{x} // {y} = {result}")

        elif (operation == "**"):
            result = x**y
            result_text = f"{x} ** {y} = {result}"
            History.append(result_text)
            print(f"{x} ** {y} = {result}")

        else:
            print("invalid operator")

    elif menu == 2:
        print("\n===== CALCULATION HISTORY =====")

        if len(History) == 0:
            print("No calculations yet.")
        else:
            for item in History:
                print(item)

    elif menu == 3:
        History.clear()
        print("History cleared Successfully!")


    elif menu == 4:

        if len(History) == 0:
            print("No calculations yet to edit ")
        else:
            print("\n===== EDIT CALCULATION HISTORY =====")
            for index, item in enumerate(History, start = 1):
                print(f"{index}. {item}")
            
  
            History_number = int(input("Enter the history number to edit: "))

            if 1 <= History_number <= len(History):
                x = float(input("Enter new first number: "))
                operation = input("Enter new operation: ")
                y = float(input("Enter new second number: "))


                if operation == "+":
                    result = x + y
                elif operation == "-":
                    result = x - y
                elif operation == "*":
                    result = x * y
                elif operation == "/" and y != 0:
                    result = x / y
                elif operation == "%" and y != 0:
                    result = x % y
                elif operation == "//" and y != 0:
                    result = x // y
                elif operation == "**":
                    result = x ** y
                else:
                    result = None
                    print("Invalid operator or division by zero.")

                if result is not None:
                    updated_entry = f"{x} {operation} {y} = {result}"
                    History[History_number - 1] = updated_entry
                    print("History updated successfully!")
                else:
                    print("History was not updated because the entry was empty.")
            else:
                print("Invalid history number.")

    elif menu == 5:
        break

    else:
        print("Invalid menu choice")



    choice = input("Do you want another calculation? (Y/N): ").upper()

print("THANK YOU FOR USING CALCULATOR")




