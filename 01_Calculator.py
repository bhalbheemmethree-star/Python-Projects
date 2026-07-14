

History = []

choice = "Y"

while choice == "Y":
    print("==============================")
    print("      PYTHON CALCULATOR       ")
    print("==============================")
    print("1. Perform Calculation")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")
    print("==============================")

    menu = int(input("choose an option:"))

    if menu == 1:


        x = float(input("Enter First number :"))
        operation = input("Enter Operation:")
        y = float(input("Enter Second number :"))

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
        break

    else:
        print("Invalid menu choice")

    choice = input("Do you want another calculation? (Y/N): ").upper()

print("\nThank you for using  Calculator!")



