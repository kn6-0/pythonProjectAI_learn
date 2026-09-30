import sys

def convert_bytes():
    units = {
        "1": (1, "byte"),
        "2": (1024, "kb"),
        "3": (1024 ** 2, "mb"),
        "4": (1024 ** 3, "gb"),
        "5": (1024 ** 4, "tb"),
    }
    user_choice_1 = input(f'please enter chosen value for input \n'
                            f'1 - bytes\n'
                            f'2 - Kb\n'
                            f'3 - mb\n'
                            f'4 - GB\n'
                            f'5 - TB\n'
                            f'0 - exit\n'
                            f'>>> ')
    if user_choice_1 in units:
        divider1 , unit_name1 = units[user_choice_1]
    elif user_choice_1 == "0":
        print("Exit")
        sys.exit()
    else:
        print("Error, check your data")
        sys.exit()

    try:
        user_count = float(input("enter count: "))
    except ValueError:
        print("Error enter correct valid")
        return

    bytes_count = user_count * divider1

    user_choice_2 = input(f'please enter chosen value for output \n'
                            f'1 - bytes\n'
                            f'2 - Kb\n'
                            f'3 - mb\n'
                            f'4 - GB\n'
                            f'5 - TB\n'
                            f'0 - exit\n'
                            f'>>> ')
    if user_choice_2 in units:
        divider2 , unit_name2 = units[user_choice_2]
        res = bytes_count / divider2
        print(f'result: {user_count}{unit_name1} = {round(res, 4)}{unit_name2}')
    elif user_choice_2 == "0":
        print("Exit")
        sys.exit()
    else:
        print("Error, check your data")
        sys.exit()

convert_bytes()
