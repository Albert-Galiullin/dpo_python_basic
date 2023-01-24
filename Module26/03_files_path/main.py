# a = os.walk("C:\\", topdown=True, onerror=None, followlinks=False)
# for root, dirs, files in a:
#     for filename in files:
#         print(filename)


import os

def search_path(home, search):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(home):
        for cur_dir in dirnames:
            if cur_dir == search:
                yield os.path.join(dirpath, cur_dir)
            else:
                file_list.append(os.path.join(dirpath, cur_dir)) # В списке сгенерированы пути всех встреченных файлов.
                # На печать выводить не стал из-за засорения экрана.

# def gen_files_path(home, search):
#     result = search_path(home, search)
#     file_list = []
#     if isinstance(result, str):
#         with os.scandir(result) as files:
#             for file_name in files:
#                 if not file_name.name.startswith('.') and file_name.is_file():
#                     file_list.append(file_name.name)
#     return file_list
#
#
# print('\n'.join(gen_files_path('C:\\', 'Windows')))

direct = search_path(home = 'C:\\', search = 'Skillbox')

print('Запрошенная директория присутствует в следующих путях: ')
for i_dir in direct:
    print(i_dir)


