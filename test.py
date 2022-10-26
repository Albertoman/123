import argparse, os, json, tempfile # Вызов библиотек
 
parser = argparse.ArgumentParser() # создание переменной, которая вызывает библиатеку и метод argparse
parser.add_argument("--key", help=' random text') # создание аргумента --key
parser.add_argument("--val", help='random_text')  # создание аргумента --val
args = parser.parse_args() # переменная вызывающая аргументы
 
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data') # создание файла storage.data

if os.path.isfile(storage_path): #если файл storage.data существует идем дальше
    if args.val: # если значение есть
        with open(str(storage_path), "r") as f: # открытие файла storage.data для чтения
            m = json.load(f) # загрузка в формате json в режиме для чтения
            if args.key in m: # если аргумент key внутри файла
                m[args.key] = m[args.key] + [args.val] # прибавляем значение к аргументу key
            else: 
                m.update({args.key: [args.val]}) # обновить ключ и значение
        with open(str(storage_path), "w") as f: # открытие файла storage.data для записи
            json.dump(m, f) # преобразование в формат json
    else:
        try: 
            with open(str(storage_path), "r") as f: # открытие файла storage.data для записи
                m = json.load(f) # преобразование в формат json в режиме для чтения
                if m[args.key] == None: # если аргумент key не найден
                    print(None) # Выводится  None
                if len(m[args.key]) > 1: # если длина аргументов key больше одного
                    print(', '.join(m.get(args.key))) # выводятся через ', ' все арументы key
                else:
                    print(*m.get(args.key)) # запросить ключ
        except:
            print(None) # Выводится None
else:
    d = {} # d = пустой словарь
    with open(str(storage_path), "w") as f: # Открытие файла storage.data для записи
        if args.val: # если значение есть
            d = {args.key: [args.val]} # d = словарь с ключем и значением
            json.dump(d, f) # преобразование в формат json
        else: 
            d = {args.key: None} # если аргумент key не найден
            print(None) # Выводится None
