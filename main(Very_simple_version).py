def main():
    while True:
        your_choice = input("Choose which feature you want to use: ")

        if your_choice == "1":
            binary_number = input("Enter the binary number: ")
            binary_length = int(len(binary_number))
            result = 0
            for i in range(int(binary_length)):
                result = int(result) * 2 + int(binary_number[i])

            print(f"\n Your result is {result}.")


        elif your_choice == "2":
            decimal_number = input("Enter the decimal number: ")
            result = ""
            while int(decimal_number) != 0:
                b = int(decimal_number) % 2
                decimal_number = int(decimal_number) // 2
                result = str(b) + result
            print( f"\n Your result is {result}.")


        elif your_choice == "3":
            binary_number_1 = input("Enter the first binary number: ")
            binary_length_1 = len(binary_number_1)
            binary_number_2 = input("Enter the second binary number: ")
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
                addition = 0
                if int(a) % 2 == 0:
                    if int(a) != 0:
                        addition = 1
                    current_number = "0"
                    result = current_number + result
                elif int(a) % 2 != 0:
                    if int(a) != 1:
                        addition = 1
                    current_number = "1"
                    result = current_number + result

            if addition == 1:
                result = "1" + result
                print(f"\n Your result is {result}.")
            else:
                print(f"\n Your result is {result}.")



if __name__ == '__main__':
    main()
