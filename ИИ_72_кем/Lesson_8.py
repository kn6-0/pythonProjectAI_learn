import sys

users = {}

def print_data(data):
    if data == {}:
        print("[INFO] Пользователей нет")
    else:
        for user in data:
            temp = ''
            for key in data[user]:
                temp += f'{key} - {data[user][key]}\n'
            print(f'Пользователь: {user}\nИнформация:\n{temp}')

def menu():
    inp = input(f"Система пользователей. Выберите действия:\n"
          f"1 - просмотр базы данных\n"
          f"2 - добавить пользователя\n"
          f"3 - удалить пользователя\n"
          f"0 - выход\n"
          f"--> ")
    try:
        if inp == '1':
            print_data(users)
        elif inp == '2':
            n_usr_name = input("Введите имя нового пользователя: ")
            n_usr_phone = input("Введите номер телефона нового пользователя: ")
            n_usr_email = input("Введите email нового пользователя: ")
            n_usr_pin = input("Введите пин-код нового пользователя: ")
            new_data = {n_usr_name: {'phone':n_usr_phone,
                     'email':n_usr_email,
                     'pin_code':n_usr_pin},
            }
            users.update(new_data)
            print(f'[INFO] Успешно добавлен пользователь "{n_usr_name}"')
        elif inp == '3':
            d = input('Введите имя пользователя, которого хотите удалить: ')
            try:
                users.pop(d)
                print(f'[INFO] Успешно пользователь "{d}"')
            except:
                print("[ERROR] Попытка удалить несуществующего пользователя")
        elif inp == '0':
            sys.exit()
        elif inp == '':
            return
        else:
            print("[ERROR] Неизвестная команда")
    except Exception as e:
        print(f'[ERROR] {e}')

while True:
    menu()
