import os

def get_start_directory(home):

    if home is None:
        return os.getcwd()
    if os.path.isdir(home):
        return home
    else:
        print('Указанная вами папка не найдена.')
        return False


def get_file_list(home):

    for r, d, f in os.walk(home):
        for file in f:
            if file.endswith(".py"):
                yield os.path.join(r, file)


line_counter = 0
directory = get_start_directory('c:\\dpo_python_basic\Module25')
if isinstance(directory, str):
    file_list = list(get_file_list(directory))
    if len(file_list) > 0:
        for file in file_list:
            try:
                cur_file = open(file, "r")
                local_count = 0
                for line in cur_file:
                    # Откидываем пустые строки и комментарии
                    if line != '\n' or not line.startswith('"') or not line.startswith('#'):
                        local_count += 1
                print(f'{cur_file.name} - {local_count} строки')
                line_counter += local_count
                cur_file.close()
            except:
                continue
        print("=====================================")
        print("Всего строк  - ", line_counter)
