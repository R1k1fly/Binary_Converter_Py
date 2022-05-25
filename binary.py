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
        result = "1" + result
        return result
    else:
        return result


def binary_negative(binary_number):
    binary_length = int(len(binary_number))
    result = ""
    for i in range(int(binary_length) - 1, - 1, -1):
        if binary_number[i] == "1":
            result = "0" + result
        elif binary_number[i] == "0":
            result = "1" + result
    return binary_addition(result, "1")


def binary_subtract(binary_number_1, binary_number_2):
    return binary_addition(binary_number_1, binary_negative(binary_number_2))


def binary_multiplication(binary_number_1, binary_number_2):
    binary_length_1 = len(binary_number_1)
    binary_length_2 = len(binary_number_2)
    result = ""
    max_length_m = max(binary_length_1, binary_length_2)
    min_length_m = min(binary_length_1, binary_length_2)
    global min_number_m
    global max_number_m
    global a
    global counter
    counter = 0
    if max_length_m == binary_length_1:
        max_number_m = binary_number_1
        min_number_m = binary_number_2

    elif max_length_m == binary_length_2:
        max_number_m = binary_number_2
        min_number_m = binary_number_1

    dif = max_length_m - min_length_m
    #
    # for i in range(dif):
    #     min_number_m = "0" + str(min_number_m)
    # binary_number_1 = binary_number_1[::-1]
    # binary_number_2 = binary_number_2[::-1]
    # max_number_m = max_number_m[::-1]
    # min_number_m = min_number_m[::-1]
    # min_length_m = str(min_length_m)
    for i in range(min_length_m -1, -1, -1):
        if dif == 0:
            a = int(min_number_m[i]) * int(max_number_m)
            # print(f"a = {int(min_number_m[i])} * {int(max_number_m)}")
        elif dif != 0:
            a = int(binary_number_2[i]) * int(binary_number_1)
            # print(f"a = {int(binary_number_2[i])} * {int(binary_number_1)}")

        if a == 0:
            if i != 0:
                for x in range(min_length_m):
                    a = str(a) + "0"
                for y in range(counter):
                    a = str(a) + "0"
                counter = counter + 1


        elif a != 0:
            for x in range(counter):
                a = str(a) + "0"
            counter = counter + 1

        # print(f"a: {a}")
        # print(f"Adding {result} and {str(a)}")
        result = binary_addition(result, str(a))
    return result
    # print(result)
