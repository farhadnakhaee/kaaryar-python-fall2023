def some_function():
    print("Executing some function...")

    # a loop with if-else statements
    for i in range(5):
        if i % 2 == 0:
            print(f"Step {i}: Performing even iteration.")
        else:
            print(f"Step {i}: Performing odd iteration.")

    # a conditional statement
    user_input = input("Enter 'yes' or 'no': ")
    if user_input.lower() == 'yes':
        print("User entered 'yes', proceeding with the next steps.")
    elif user_input.lower() == 'no':
        print("User entered 'no', skipping some steps.")
    # else:
    #     print("Invalid input. Defaulting to the next steps.")

    print("Print statement at the end.")

if __name__ == "__main__":
    print("Starting the program...")
    some_function()
    print("Program finished.")
