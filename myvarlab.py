import os


path = input("Введите путь к папке: ")

def obxod_file(path):
    print(os.listdir(path))
obxod_file(path)

