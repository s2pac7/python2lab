def print_data(data):
    #Список
    if type(data) == list:
        pr = 1
        for i in data[1::2]:
            pr *= data[i]

        print("Произведение: ", pr)
        print("Максимальный элемент: ", max(data))
        data.remove(max(data))
        print("Новый лист:", data)

    #Словарь
    if type(data) == dict:
        new_dict = sorted(data.items(), key=lambda x: x[0])
        print("Отсортированный словарь: ", new_dict)

    #Целое число
    if type(data) == int:
        from math import sqrt
        if data > 1:
            for i in range(2, data):
                if data % i == 0:
                    print("Это составное число")
                    break
            else:
                print("Это простое число")
        else:
            print("Число меньше 1")

    #Строка
    if type(data) == str:
        vowels = 0
        consonants = 0
        for char in data:
            if char in "аяуюеёыиАЯУЮЕЁЫИ":
                vowels += 1
            else:
                consonants += 1

        print("Гласные:", vowels)
        print("Согласные:", consonants)



