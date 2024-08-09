import pyautogui as py
name = 'Nikita '
def hello():
    print("Hello ", name)

def proverka (a, b, c ):
    if a != 2 and b != 2 or c != 2:
     return a * b * c
    else:
        print("some not correct")
        py.alert("Для вывода информации ", "title", button="Okay ")
        year = py.prompt("Сколько вам лет?", "Ваш возраст")
        print("Вам", year, "лет сейчас.")
        py.confirm("What your sex?", "Yea?", ("Man", "Woman"))
        py.password("Enter your password", "pasword title")

# import random as ran
#
# import time
#
# print('        Game \n\'Guess the number\'')
#
#
# try:
#     while True:
#         print("Введите С какого числа будете угадывать )")
#         a = int(input("С числа: "))
#         print("Введите ПО какое число будете угадывать )")
#         b = int(input("По число: "))
#
#         Random_num = ran.randint(a, b)
#         User_num = int(input('Put yoyr number: '))
#         if Random_num == User_num:
#             print('You have guessed')
#             print(f'Я загадала {Random_num}')
#             Play_again = input('Do you want play again?')
#             if Play_again == 'yes' or Play_again == 'да' or Play_again == 'lf':
#                 while True:
#                     print("Введите С какого числа будете угадывать )")
#                     a = int(input("С числа: "))
#                     print("Введите ПО какое число будете угадывать )")
#                     b = int(input("По число: "))
#
#                     Random_num = ran.randint(a, b)
#                     User_num = int(input('Put yoyr number: '))
#                     if Random_num == User_num:
#                         print('You have guessed')
#                         print(f'Я загадала {Random_num}')
#                         Play_again = input('Do you want play again?')              #I don't think
#                         if Play_again == 'yes' or Play_again == 'да' or Play_again == 'lf':
#                             while True:
#                                 print("Введите С какого числа будете угадывать )")
#                                 a = int(input("С числа: "))
#                                 print("Введите ПО какое число будете угадывать )")
#                                 b = int(input("По число: "))
#
#                                 Random_num = ran.randint(a, b)
#                                 User_num = int(input('Put yoyr number: '))
#                                 if Random_num == User_num:
#                                     print('You have guessed')
#                                     print(f'Я загадала {Random_num}')
#                                 elif Random_num != User_num:
#                                     print('You haven`t guessed')
#                                     print(f'I riddled {Random_num}')
#                         elif Play_again == 'no' or Play_again == 'нет':
#                             break                                                # it's needed, but I'll leave it at that.
#                     elif Random_num != User_num:
#                         print('You haven`t guessed')
#                         print(f'I riddled {Random_num}')
#             elif Play_again == 'no' or Play_again == 'нет':
#                 break
#         elif Random_num != User_num:
#             print('You haven`t guessed')
#             print(f'I riddled {Random_num}')
#             Play_again = input('Do you want play again?')
#             if Play_again == 'yes' or Play_again == 'да':
#                 while True:
#                     print("Введите С какого числа будете угадывать )")
#                     a = int(input("С числа: "))
#                     print("Введите ПО какое число будете угадывать )")
#                     b = int(input("По число: "))
#
#                     Random_num = ran.randint(a, b)
#                     User_num = int(input('Put yoyr number: '))
#                     if Random_num == User_num:
#                         print('You have guessed')
#                         print(f'I riddled {Random_num}')
#                     elif Random_num != User_num:
#                         print('You haven`t guessed')
#                         print(f'I riddled {Random_num}')
#             elif Play_again == 'no' or Play_again == 'нет':
#                 break
# except ValueError:
#     print('There is a mistake')
#     time.sleep(0.5)
#     print('Please reapite a program')
# import pyautogui
# print(pyautogui.position())