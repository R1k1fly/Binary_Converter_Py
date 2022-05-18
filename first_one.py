def first_one():
    while True:
        global position
        number = input("Enter binary number: ")
        length = len(number)
        for i in range(length -1, -1, -1):
            if number[i] == "1":
                position = i

        print("First position: " + str(position))

if __name__ == "__main__":
    first_one()