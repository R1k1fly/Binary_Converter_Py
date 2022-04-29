import time
from tqdm import tqdm
import colorama


def main():
    while True:
        print(colorama.Fore.LIGHTCYAN_EX + """
        !Welcome to the Binary-Decimal converter!""" + colorama.Style.RESET_ALL + colorama.Fore.LIGHTYELLOW_EX + """
      ____________________________________________
      |                                          |
      | 1 - covert binary number into decimal;   |
      | 2 - convert decimal number into binary.  |
      | 3 - exit                                 |
      |__________________________________________|
        """ + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTYELLOW_EX + "Choose which feature you want to use: ")
        your_choice = input("")
        if your_choice == "1":
            print("Enter the binary number: ")
            binary_number = input("")
            binary_length = int(len(binary_number))
            result = 0
            wrong = ["1", "0"]
            # print(f"The length of the number is {binary_length}.")
            # if "1" not in str(binary_number):
            #     print(colorama.Fore.LIGHTRED_EX + "\n You entered a wrong value!")
            #     continue
            # elif "0" not in str(binary_number):
            #     print(colorama.Fore.LIGHTRED_EX + "\n You entered a wrong value!")
            #     continue
            for i in range(int(binary_length)):
                result = int(result) * 2 + int(binary_number[i])

            for i in tqdm(range(int(100)), ncols=100):
                time.sleep(0.009)
                pass
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + f"\n Your result is {result}." + colorama.Style.RESET_ALL)

        elif your_choice == "2":
            print("Enter the decimal number: ")
            decimal_number = input("")
            result = ""
            while int(decimal_number) != 0:
                b = int(decimal_number) % 2
                decimal_number = int(decimal_number) // 2
                result = str(b) + result
            for i in tqdm(range(int(100)), ncols=100):
                time.sleep(0.009)
                pass
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + f"\n Your result is {result}." + colorama.Style.RESET_ALL)
        elif your_choice == "3":
            print(colorama.Fore.LIGHTYELLOW_EX + "Thank you for using this program. It was made by Zhabrovets Andrii.")
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + "You entered a wrong value!")


if __name__ == '__main__':
    main()
