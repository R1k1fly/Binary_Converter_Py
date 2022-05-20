import colorama
import binary



def main():
    while True:
        print(colorama.Fore.LIGHTCYAN_EX + """
        !Welcome to the Binary-Decimal converter!""" + colorama.Style.RESET_ALL + colorama.Fore.LIGHTYELLOW_EX + """
      ____________________________________________
      |                                          |
      | 1 - covert binary number into decimal;   |
      | 2 - convert decimal number into binary.  |
      | 3 - add one binary number to another     |
      | 4 - subtract one binary number from      |
      |     another                              |
      | 5 - negative binary number converter     |
      | 6 - exit                                 |
      |__________________________________________|
        """ + colorama.Style.RESET_ALL)

        your_choice = input(colorama.Fore.LIGHTYELLOW_EX + "Choose which feature you want to use: ")

        if your_choice == "1":
            binary_number = input("Enter the binary number: ")
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT
                + f"\n Your result is {binary.binary_decimal(binary_number)}."
                + colorama.Style.RESET_ALL)

        elif your_choice == "2":
            decimal_number = input("Enter the decimal number: ")
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT
                + f"\n Your result is {binary.decimal_binary(decimal_number)}."
                + colorama.Style.RESET_ALL)

        elif your_choice == "3":
            binary_number_1 = input("Enter the first binary number: ")
            binary_number_2 = input("Enter the second binary number: ")
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT +
                f"\n Your result is {binary.binary_addition(binary_number_1, binary_number_2)}."
                + colorama.Style.RESET_ALL)

        elif your_choice == "4":
            binary_number_1 = input("Enter the first binary number: ")
            binary_number_2 = input("Enter the second binary number: ")
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT +
                f"\n Your result is {binary.subtract_binary(binary_number_1, binary_number_2)}."
                + colorama.Style.RESET_ALL)

        elif your_choice == "5":
            binary_number = input("Enter the binary number: ")
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT +
                f"""\n Your result is {binary.negative_binary(binary_number)}."""
                + colorama.Style.RESET_ALL)

        elif your_choice == "6":
            print(colorama.Fore.LIGHTYELLOW_EX + "Thank you for using this program. It was made by Zhabrovets Andrii.")
            break

        else:
            print(colorama.Fore.LIGHTRED_EX + "You entered a wrong value!")


if __name__ == '__main__':
    main()
