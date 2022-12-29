letters = "аоиеёэыуюя"

text = input("Введите текст: ")
vowels = [char for char in text if char in letters]
print("Список гласных букв:", vowels)
print("Длина списка:", len(vowels))
