"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_data(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


my_data(name='Ruslan', surname='Ishmakov', year=1993, city='Noginsk', email='email', phone='0000')

