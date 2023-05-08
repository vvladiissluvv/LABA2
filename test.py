import os


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
#C:\test rec
def obhodfile(path, level=1):
        #print('Level=', level, 'Con: ', os.listdir(path))
        for i in os.listdir(path):
            if os.path.isdir(path + '\\' + i):
                print(path + '\\' + i)
                print(os.listdir(path + '\\' + i))
                obhodfile(path + '\\' + i, level + 1)

def afafefeawfse():
    pass

def start_work():
    print('''MENU
    1. Сбор статистики из определённой папки
    2. Вывод статистики
    3. Какая-то функция, пока не придумали.''')

    user_ansver = input("Привет, ты находишься в главном меню. Напиши 1, 2 или 3 для выбора необходимой функции: ")
    ansver = check_ansver(user_ansver)

    if ansver == "1":
        fpath = input("Введите путь до папки: ")
        qq = check_path(fpath)
        obhodfile(qq)
        exit()
        #Написать функцию обхода заданной папки (Получает на вход path, рекурсивно проходит по нему и сохраняет информацию)
        #Написать 
        
    
    elif ansver == "2":
        print("Не работает!")
        exit()

    elif ansver == "3":
        print("Не работает!")
        exit()


start_work()

