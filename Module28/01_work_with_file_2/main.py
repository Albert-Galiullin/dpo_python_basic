class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            print('Файл не найден, создаем новый')
            self.file = open(self.filename, "w", encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
           print(exc_type, ' - Файл открыт в режиме ReadOnly, запись не удалась')
           return True



with File("example.txt", "r") as file:
    file.write("Всем привет!")

