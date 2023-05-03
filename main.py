import os
import json


# функция для получения размера файла в удобном формате
def get_file_size(file_path):
    size = os.path.getsize(file_path)
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size > 1024 and index < len(suffixes) - 1:
        size /= 1024
        index += 1
    return '{:.2f}{}'.format(size, suffixes[index])


# получение пути к папке от пользователя
folder_path = input("Введите путь к папке: ")

# словарь для хранения статистики
statistics = {}

# обход всех файлов в папке и подпапках
for root, dirs, files in os.walk(folder_path):
    for file in files:
        extension = os.path.splitext(file)[-1].lower()

        # добавление нового типа файлов в словарь
        if extension not in statistics:
            statistics[extension] = {'count': 0, 'size': 0, 'folders': {}}

        # обновление статистики для текущего типа файлов
        statistics[extension]['count'] += 1
        file_path = os.path.join(root, file)
        statistics[extension]['size'] += os.path.getsize(file_path)

        # обновление списка папок для текущего типа файлов
        folder = os.path.dirname(file_path)
        if folder not in statistics[extension]['folders']:
            statistics[extension]['folders'][folder] = 0
        statistics[extension]['folders'][folder] += 1

# сохранение результатов в файл
with open('statistics.json', 'w') as f:
    json.dump(statistics, f)

# вывод результатов в консоль с возможностью фильтрации
command = input("Хотите вывести результаты на экран? (Y/n) ")
if command.lower() == 'y':
    with open('statistics.json', 'r') as f:
        statistics = json.load(f)
    filter = input("Введите расширения файлов через запятую (например .txt,.docx): ")
    filter = [f.lower() for f in filter.split(',') if f]
    for extension, data in statistics.items():
        if not filter or extension in filter:
            print("Расширение: {}".format(extension))
            print("Количество файлов: {}".format(data['count']))
            print("Занимаемая память: {}".format(get_file_size(data['size'])))
            print("Количество папок: {}".format(len(data['folders'])))
            print("Папки, в которых лежат файлы данного типа:")
            for folder, count in sorted(data['folders'].items(), key=lambda x: x[1], reverse=True):
                print("\t{} ({})".format(folder, count))
            print()