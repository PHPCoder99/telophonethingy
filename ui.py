from logger import input_data, print_data

def interface():
    print("hello! this a telephone thing that im writing for homework.")
    print("add data (a)")
    print("view data (v)")
    print("or (q) to quit")
    command = input("enter command: ")

    while command not in ["a", "v", "q"]:
        print("command not found")
        command = input("enter command: ")

    if command == "a":
        input_data()
    elif command == "v":
        print_data()
    else:
        return
