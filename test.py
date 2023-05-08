import os
import json
from random import randint


def check_path(path:str) -> bool:
    while not (os.path.exists(path) and os.path.isdir(path)):
        path = input("Вы ввели неправильный путь или путь не до папки, проверьте корректность и повторите попытку: ")
        return check_path(path)
    return path

def check_ansver(ansver:str) -> bool:
    while ansver not in ["1", "2", "3"]:
        ansver = input("Введите корректный номер функции!!! ")
        return check_ansver(ansver)
    return ansver

def exit():
    ansver = input("Если вы действительно хотите выйти напишите - Да, иначе нажмите Enter ").lower()
    if ansver == "да":
        return 0
    else:
        start_work()
#/home/chikoni/Загрузки

def obhodfile(path, level=1):
        json_data = {key: os.path.getsize(path + '/' + key) for key in os.listdir(path)}

        if not os.path.exists("./stat/"):
            os.mkdir("./stat/")

        with open("./stat/{}.json".format(randint(0, 100)), "w", encoding='utf8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                obhodfile(path + '/' + i, level + 1)

        join_file()

def join_file():
        curent_file = []
        for fl in os.listdir(f'./stat/'):
            with open('./stat/{}'.format(fl), encoding='utf8') as f:
                jsonText = json.load(f)
                for i in jsonText:
                    curent_file.append(i)

        if not os.path.exists("./finish/"):
            os.mkdir("./finish/")

        with open("./finish/cur_file.json", "w", encoding='utf8') as fh:
            json.dump(curent_file, fh, indent=4, ensure_ascii=False)


def get_stat():
    print("""[MENU STATISTICKS]
        1. Всем типам файлов
        2. Конкретный тип файлов
        3. Всем папкам
        4. Конкретной папке
        """)
    choose_stat = input("Введите номер необходимой функции статистики: ")
    if choose_stat == "1":
        pass
    elif choose_stat == "2":
        pass
    elif choose_stat == "3":
        pass
    elif choose_stat == "4":
        print([])
    exit()

def start_work():
    print('''MENU
    1. Сбор статистики из определённой папки
    2. Вывод статистики
    3. Какая-то функция, пока не придумали.''')

    user_ansver = input("Привет, ты находишься в главном меню. Напиши 1, 2 или 3 для выбора необходимой функции: ")
    ansver = check_ansver(user_ansver)

    if ansver == "1":
        fpath = input("Введите путь до папки: ")
        # qq = check_path(fpath)
        obhodfile(fpath)
        exit()
        #Написать функцию обхода заданной папки (Получает на вход path, рекурсивно проходит по нему и сохраняет информацию)
        #Написать


    elif ansver == "2":
        print("""[MENU STATISTICKS]
        1. Всем типам файлов
        2. Конкретный тип файлов
        3. Всем папкам
        4. Конкретной папке
        """)
        choose_stat = input("Введите номер необходимой функции статистики: ")

        if choose_stat == "1":
            pass
        elif choose_stat == "2":
            pass
        elif choose_stat == "3":
            pass
        elif choose_stat == "4":
            print([])
        exit()

    elif ansver == "3":
        print("Не работает!")
        exit()


# start_work()
obhodfile("/home/chikoni/Загрузки")

