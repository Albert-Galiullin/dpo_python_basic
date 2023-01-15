import os.path
def find_object(object):
    d = 0
    dirs = []
    for i_elem in os.listdir(object):
        path = os.path.join(object, i_elem)
        if os.path.isdir(path):
            d += 1
            result = find_object(path)
            dirs.append(result)
    dirs.append(d)
    return sum(dirs)

def find_object2(object):
    f = 0
    fils = []
    for i_elem in os.listdir(object):
        path = os.path.join(object, i_elem)
        if os.path.isfile(path):
            f += 1
        elif os.path.isdir(path):
            result = find_object2(path)
            fils.append(result)
    fils.append(f)
    return sum(fils)

def size_dir(object):
    f = 0
    fils = []
    for i_elem in os.listdir(object):
        path = os.path.join(object, i_elem)
        if os.path.isfile(path):
            f += os.path.getsize(path)
        elif os.path.isdir(path):
            result = find_object2(path)
            fils.append(result)
    fils.append(f)
    return sum(fils)



path_dir = 'C:\dpo_python_basic\Module22'

print(path_dir)
c = size_dir(path_dir)/1024
print('Размер каталога (в Кб): ',c)
a = find_object(path_dir)
print('Количество подкаталогов:',a)
b = find_object2(path_dir)
print('Количество файлов:',b)

