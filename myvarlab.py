import os
#под менюшку сбора статистики
#Для каждого типа файлов должны подсчитываться: количество файлов этого типа,
# общая занимаемая память,
# папки, в которых лежат файлы данного типа с количеством файлов данного типа в папке.
# После завершения подсчета статистики программа сохраняет результаты в файл.

path = input()

def obhodfile(path,level=1):
        print('Level=', level, 'Con: ', os.listdir(path))
        for i in os.listdir(path):
                if os.path.isdir(path+'\\'+i):
                        print(path+'\\'+i)
                        obhodfile(path+'\\'+i, level+1)
                        print(len(path))
obhodfile(path)







#print(os.listdir(path))
#for i in os.listdir(path):
       # os.path.isdir(path)
        #if i == True:
               # print(i)


