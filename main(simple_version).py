def binary_decimal(binary_number):
    binary_length = int(len(binary_number))
    result = 0
    print("Now we multiply our result by 2 and add the number of the lap.")
    for i in range(int(binary_length)):
        result = int(result) * 2 + int(binary_number[i])

    return result


def decimal_binary(decimal_number):
    result = ""
    while int(decimal_number) != 0:
        b = int(decimal_number) % 2
        decimal_number = int(decimal_number) // 2
        result = str(b) + result
    return result


def binary_addition(binary_number_1, binary_number_2):
    # global result
    binary_length_1 = len(binary_number_1)
    binary_length_2 = len(binary_number_2)
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

        elif int(a) % 2 != 0:
            addition = 0
            if int(a) != 1:
                addition = 1
            current_number = "1"
            result = current_number + result

    if addition == 1:
        print("Addition: 1")
        result = "1" + result
        return result
    else:
        return result


def negative_binary(binary_number):
    binary_length = int(len(binary_number))
    result = ""
    for i in range(int(binary_length) - 1, - 1, -1):
        if binary_number[i] == "1":
            result = "0" + result
        elif binary_number[i] == "0":
            result = "1" + result
    return binary_addition(result, "1")


def subtract_binary(binary_number_1, binary_number_2):
    return binary_addition(binary_number_1, negative_binary(binary_number_2))



def main():
    while True:
        print("""
       !Welcome to the Binary-Decimal converter!
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
        """)

        your_choice = input("Choose which feature you want to use: ")

        if your_choice == "1":
            binary_number = input("Enter the binary number: ")
            print(f"\n Your result is {binary_decimal(binary_number)}.")

        elif your_choice == "2":
            decimal_number = input("Enter the decimal number: ")
            print(f"\n Your result is {decimal_binary(decimal_number)}.")

        elif your_choice == "3":
            binary_number_1 = input("Enter the first binary number: ")
            binary_number_2 = input("Enter the second binary number: ")
            print(f"\n Your result is {binary_addition(binary_number_1, binary_number_2)}.")

        elif your_choice == "4":
            binary_number_1 = input("Enter the first binary number: ")
            binary_number_2 = input("Enter the second binary number: ")
            print(f"\n Your result is {subtract_binary(binary_number_1, binary_number_2)}.")

        elif your_choice == "5":
            binary_number = input("Enter the binary number: ")
            print(f"""\n Your result is {negative_binary(binary_number)}.""")

        elif your_choice == "6":
            print("Thank you for using this program. It was made by Zhabrovets Andrii.")
            break

        else:
            print("You entered a wrong value!")


if __name__ == '__main__':
    main()
