def calculator():
    print("🧮 Welcome to the Python Calculator!")

    while True:
        # Ask for numbers
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Please enter valid numbers!")
            continue

        # Ask for operation
        print("\nChoose an operation:")
        print("1 ➕ Addition (+)")
        print("2 ➖ Subtraction (-)")
        print("3 ✖️ Multiplication (*)")
        print("4 ➗ Division (/)")
        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice == "1" or choice == "+":
            result = num1 + num2
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif choice == "2" or choice == "-":
            result = num1 - num2
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif choice == "3" or choice == "*":
            result = num1 * num2
            print(f"✅ Result: {num1} × {num2} = {result}")
        elif choice == "4" or choice == "/":
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed!")
                continue
            result = num1 / num2
            print(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            print("❌ Invalid choice! Please select a valid operation.")
            continue

        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n👋 Thanks for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()
