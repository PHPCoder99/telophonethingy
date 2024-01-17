from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    fmrt = int(input(f"which format to use?\n\n1: \n{name} \n{surname} \n{phone} \n{address} \n\n2: \n{name};{surname};{phone};{address}\nChoose a format: "))
    while fmrt != 1 and fmrt != 2:
        print("incorrect input")
        fmrt = int(input("enter a format"))

    if fmrt == 1:
        with open("data_first_format.csv", "a", encoding="utf-8") as f:
            f.write(f"\n\n{name}\n{surname}\n{phone}\n{address}")
    elif fmrt == 2:
        with open("data_second_format.csv", "a", encoding="utf-8") as f:
            f.write(f"\n\n{name};{surname};{phone};{address}")


def print_data():
    print("arright first file time")

    with open("data_first_format.csv", "r", encoding="utf-8") as f:
        data1 = f.readlines()
        data1list = []
        j = 0
        for i in range(len(data1)):
            if data1[i] == "\n" or i == len(data1) - 1:
                data1list.append(''.join(data1[j:i+1]))
                j = i
        print("".join(data1list))

    print("arright second file time")

    with open("data_second_format.csv", "r", encoding="utf-8") as f:
        data2 = f.readlines()
        print("".join(data2))


# slices? pfft, im better than that. c:
def edit_data():
    fmrt = int(input(
        f"which format to use? (1/2): "))
    while fmrt != 1 and fmrt != 2:
        print("incorrect input")
        fmrt = int(input("enter a format"))

    if fmrt == 1:
        with open("data_first_format.csv", "r", encoding="utf-8") as f:
            data1 = f.read()
            data1 = data1.split("\n\n")
            for i in range(len(data1)):
                print(i, "-", end=" ")
                print(data1[i])
        entry = int(input("which entry to modify (enter id): "))
        while entry < 0 or entry > len(data1)-1:
            entry = int(input("incorrect input, try again, enter id: "))
        print("enter new data: ")
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

        data1[entry] = f"{name}\n{surname}\n{phone}\n{address}"
        with open("data_first_format.csv", "w", encoding="utf-8") as f:
            f.write("\n\n".join(data1))
    elif fmrt == 2:
        with open("data_second_format.csv", "r", encoding="utf-8") as f:
            data2 = f.read()
            data2 = data2.split("\n\n")
            for i in range(len(data2)):
                print(i, "-", end=" ")
                print(data2[i])
        entry = int(input("which entry to modify (enter id): "))
        while entry < 0 or entry > len(data2) - 1:
            entry = int(input("incorrect input, try again, enter id: "))
        print("enter new data: ")
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

        data2[entry] = f"{name};{surname};{phone};{address}"
        with open("data_second_format.csv", "w", encoding="utf-8") as f:
            f.write("\n\n".join(data2))


def delete_data():
    fmrt = int(input(
        f"which format to use? (1/2): "))
    while fmrt != 1 and fmrt != 2:
        print("incorrect input")
        fmrt = int(input("enter a format"))

    if fmrt == 1:
        with open("data_first_format.csv", "r", encoding="utf-8") as f:
            data1 = f.read()
            data1 = data1.split("\n\n")
            for i in range(len(data1)):
                print(i, "-", end=" ")
                print(data1[i])
        entry = int(input("which entry to delete (enter id): "))
        while entry < 0 or entry > len(data1)-1:
            entry = int(input("incorrect input, try again, enter id: "))

        del data1[entry]

        with open("data_first_format.csv", "w", encoding="utf-8") as f:
            f.write("\n\n".join(data1))
    elif fmrt == 2:
        with open("data_second_format.csv", "r", encoding="utf-8") as f:
            data2 = f.read()
            data2 = data2.split("\n\n")
            for i in range(len(data2)):
                print(i, "-", end=" ")
                print(data2[i])
        entry = int(input("which entry to delete (enter id): "))
        while entry < 0 or entry > len(data2)-1:
            entry = int(input("incorrect input, try again, enter id: "))

        del data2[entry]

        with open("data_second_format.csv", "w", encoding="utf-8") as f:
            f.write("\n\n".join(data2))
