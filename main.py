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
      | 3 - add one binary number to another     |
      | 4 - exit                                 |
      |__________________________________________|
        """ + colorama.Style.RESET_ALL)
        your_choice = input(colorama.Fore.LIGHTYELLOW_EX + "Choose which feature you want to use: ")
        if your_choice == "1":
            binary_number = input("Enter the binary number: ")
            binary_length = int(len(binary_number))
            result = 0
            print("Now we multiply our result by 2 and add the number of the lap.")
            for i in range(int(binary_length)):
                print("Lap:" + str(i))

                print(f"{result} * 2 + {binary_number[i]}")
                result = int(result) * 2 + int(binary_number[i])
                time.sleep(1)

            for i in tqdm(range(int(100)), ncols=100):
                time.sleep(0.009)
                pass
            print(
                colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + f"\n Your result is {result}." + colorama.Style.RESET_ALL)

        elif your_choice == "2":
            decimal_number = input("Enter the decimal number: ")
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
            binary_number_1 = input("Enter the first binary number: ")
            binary_length_1 = len(binary_number_1)
            print(f"Binary length 1: {binary_length_1}.")
            binary_number_2 = input("Enter the second binary number: ")
            binary_length_2 = len(binary_number_2)
            print(f"Binary length 2: {binary_length_2}.")
            result = ""
            addition = 0
            max_length = max(binary_length_1, binary_length_2)
            min_length = min(binary_length_1, binary_length_2)

            global min_number
            global max_number
            if max_length == binary_length_1:
                max_number = binary_number_1
                min_number = binary_number_2

            elif max_length == binary_length_2:
                max_number = binary_number_2
                min_number = binary_number_1

            dif = max_length - min_length
            for i in range(dif):
                min_number = "0" + str(min_number)
            print("Max:" + max_number)
            print("Min:" + min_number)
            for i in tqdm(range(int(100)), ncols=100):
                time.sleep(0.009)
                pass
            for i in range(int(max_length) - 1, -1, -1):
                a = int(max_number[i]) + int(min_number[i]) + int(addition)
                # print(f"Binary_1: {binary_number_1[i]}")
                # print(f"Binary_2: {binary_number_2[i]}") 10010
                addition = 0
                if int(a) % 2 == 0:
                    addition = 0
                    if int(a) != 0:
                        addition = 1
                    current_number = "0"
                    result = current_number + result
                    print(f"Addition: {addition}")
                    print(f"Current number: {current_number}")
                    print(f"Result number[{i}]: {result}")
                    time.sleep(0.5)

                elif int(a) % 2 != 0:
                    addition = 0
                    if int(a) != 1:
                        addition = 1
                    current_number = "1"
                    result = current_number + result
                    print(f"Addition: {addition}")
                    print(f"Current number: {current_number}")
                    print(f"Result number[{i}]: {result}")
                    time.sleep(0.5)
            if addition == 1:
                print("Addition: 1")
                result = "1" + result
                print(
                    colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + f"\n Your result is {result}." + colorama.Style.RESET_ALL)
            else:
                print("Addition: 0")
                print(
                    colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + f"\n Your result is {result}." + colorama.Style.RESET_ALL)

        elif your_choice == "4":
            print(colorama.Fore.LIGHTYELLOW_EX + "Thank you for using this program. It was made by Zhabrovets Andrii.")
            break
        else:
            print(colorama.Fore.LIGHTRED_EX + "You entered a wrong value!")


if __name__ == '__main__':
    main()
