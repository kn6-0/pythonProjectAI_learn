import math as m
import sys

try:
    alph_power = int(input("Введите мощность алфавита для пароля: "))
    pass_length = int(input("Введите фиксированную длину пароля: "))
    users = int(input("Введите количество пользователей в системе: "))
except:
    print("Ошибка номер 1, вероятно введены невалидные данные")
    sys.exit()

try:
    bits_per_symbol = round(m.log(alph_power, 2))
    if bits_per_symbol == 0:
        bits_per_symbol = 1
    bits_per_password = bits_per_symbol*pass_length
    bits_in_system = bits_per_password*users

    kb_in_system = round(bits_in_system/8/1024, 2)

    print(f"Все пароли системы занимают {kb_in_system} килобайт. Пользователей в системе: {users}, длина пароля: {pass_length}, мощность алфавита пароля: {alph_power}.")
except:
    print("Ошибка номер 2, вероятно введены невалидные данные")
    sys.exit()
