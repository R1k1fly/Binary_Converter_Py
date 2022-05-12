def main():
    while True:
        print("""
        !Welcome to the Binary-Decimal converter!
      ____________________________________________
      |                                          |
      | 1 - covert binary number into decimal;   |
      | 2 - convert decimal number into binary.  |
      |__________________________________________|
        """)
        print("Choose which feature you want to use: ")
        your_choice = input("")
        if your_choice == "1":
            print("Enter the binary number: ")
            binary_number = input("")
            binary_length = int(len(binary_number))
            result = 0
            for i in range(int(binary_length)):
                result = int(result) * 2 + int(binary_number[i])

            print(f"\n Your result is {result}.")

        elif your_choice == "2":
            print("Enter the decimal number: ")
            decimal_number = input("")
            result = ""
            while int(decimal_number) != 0:
                b = int(decimal_number) % 2
                decimal_number = int(decimal_number) // 2
                result = str(b) + result
            print( f"\n Your result is {result}.")
        else:
            print("You entered a wrong value!")


if __name__ == '__main__':
    main()
