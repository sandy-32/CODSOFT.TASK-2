while True:
    print('1: - Addition')
    print('2: - Subtraction')
    print('3: - Multiplication')
    print('4: - Division')
    print('5: - Exit')

    choice = int(input("Choose an operation: "))

    if choice == 5:
        print("Exiting the program.")
        break

    if choice in [1, 2, 3, 4]:
        number1 = int(input('Enter the 1st number: '))
        number2 = int(input('Enter the 2nd number: '))

        if choice == 1:
            result = number1 + number2
        elif choice == 2:
            result = number1 - number2
        elif choice == 3:
            result = number1 * number2
        elif choice == 4:
            if number2 != 0:
                result = number1 / number2
            else:
                result = "Error!"
        
        print('The result is: {}'.format(result))
    else:
        print("Invalid choice.")
