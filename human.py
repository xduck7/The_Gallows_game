import random as rn

class Player:
    health = 0
    lang = ""
    def select_language(lang):
        if lang == "RU":
            return ["яблоко", "стол", "книга", 
                    "дом", "солнце", "окно", 
                    "вода", "музыка", "город", 
                    "цветок", "ночь", "звезда", 
                    "ребенок", "дорога", "воздух", 
                    "снег", "телефон", "зима", 
                    "лето", "весна", "осень", 
                    "чашка", "человек", "гитара", 
                    "зеркало", "трава", "гора", 
                    "море", "птица", "рыба", "кот", 
                    "собака", "компьютер", "улица", 
                    "парк", "цвет", "печь", "семья", 
                    "время", "красота", "здоровье", 
                    "еда", "счастье", "игра", "кресло", 
                    "фотоаппарат", "акула", "алгоритм",
                    "школа", "мечта", "краска", 
                    "ноутбук", "волос", "планета",
                    "мышь", "птичка", "газета", 
                    "замок", "космос", "свеча", 
                    "фильм", "ключ", "деньги", "корабль", 
                    "песок", "зонт", "платье", "волна", 
                    "сумка", "лист", "песня", "комната", 
                    "звук", "ящик", "мозг", "парень", 
                    "сестра", "пианино", "парень", 
                    "река", "корень", "сказка", 
                    "бумага", "носок", "свадьба", 
                    "кукла", "фрукт", "танец", 
                    "горшок", "зерно", "масло", 
                    "чувство", "праздник", "стул", 
                    "палец", "билет", "тень"]
        else:
            return ["apple", "table", "book", 
                     "house", "sun", "window", 
                     "water", "music", "city", 
                     "flower", "night", "star", 
                     "child", "road", "air", "snow", 
                     "phone", "winter", "summer", 
                     "spring", "autumn", "cup", "person", 
                     "guitar", "mirror", "grass", 
                     "mountain", "sea", "bird", 
                     "fish", "cat", "dog", "computer", 
                     "street", "park", "color", "stove", 
                     "family", "time", "beauty", 
                     "health", "food", "happiness", 
                     "game", "chair", "camera","school", 
                     "dream", "paint", "laptop", "hair", 
                     "planet", "mouse", "birdie", 
                     "newspaper", "castle", "cosmos", 
                     "candle", "film", "key", "money", 
                     "ship", "sand", "umbrella", 
                     "dress", "wave", "bag", "leaf", 
                     "song", "room", "sound", "box", 
                     "brain", "guy", "sister", "piano", 
                     "river", "root", "tale", "paper", 
                     "sock", "wedding", "doll", "fruit", 
                     "dance", "pot", "grain", "oil", 
                     "feeling", "holiday", "chair", 
                     "finger", "ticket", "shadow"]
    dictionary = select_language(lang)
    word = dictionary[rn.randint(0, len(dictionary)-1)]

    def isLife(self):
        return self.health > 0
    
    def need_help(self):
        return self.health < 3
    
    def help(self,health, displayed_word):
        ans = input("Желаете использовать подсказку? y / n ")
        if (ans == "y"):
            id = rn.randint(0, len(displayed_word))
            displayed_word[id] = self.word[id]

    
    def __init__(self, lang):
        self.health = 5
        self.lang = lang

        


