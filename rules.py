def know(answer):
    return answer=="n"


def display_rules():
    print("\n1. Выбор слова: Игра случайным образом генерирует слово из РУССКИХ или АНГЛИЙСКИХ букв (средней сложности),")
    print("которое надо будет угадать.\n")

    print("2. Отгадывание букв: Игрок предлагает букву, которую он считает, что содержится в слове.") 
    print("*если буква присутствует в слове, она добавляется на соответствующее место(а) в слове.\n")

    print("3. Рисование виселицы: Если предложенная буква не содержится в слове, рисуется часть виселицы.") 
    print("*каждая ошибка добавляет новую часть к виселице\n")

    print("4. Количество попыток: Количество попыток ограничивается количеством частей виселицы")
    print("*у вас 5 попыток\n")

    print("5. Конец игры: Игра заканчивается, когда слово угадано или когда виселица полностью нарисована.\n")
    print("Удачной игры!")

def greeting():
    print("\n\n ________________________")
    print("/     ИГРА ВИСЕЛИЦА     /")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n")

