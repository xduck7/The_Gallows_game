import random as rn
import human
import painter
import turtle as tr
import rules

def main(language):

    player = human.Player(lang=language)
    help_counter = 0
    #print(player.word) #для отладки


    correct_word = player.word
    displayed_word = ("*|"*len(correct_word)).split("|")

    painter.create_player()
    painter.create_chair()
    while(player.isLife()):
        #print(player.word) #для отладки
        print("".join(displayed_word) + " | Attempts: " + str(player.health))

        if "".join(displayed_word) == player.word:
            print("\nWIN!!!")
            break
        else:
            if player.need_help() and help_counter == 0:
                player.help(player.health, displayed_word)
                help_counter += 1
                continue
            
            entered_letter = input("Введите букву: ").lower()
            #print(entered_letter) #для отладки
            if entered_letter == player.word:
                print("\nWIN!!!")
                break
            elif entered_letter in player.word:
                founded_letter_id = player.word.index(entered_letter)
                displayed_word[founded_letter_id] = entered_letter
            else:
                player.health -= 1
                print("\nТакой буквы нет! \n")
                painter.actions(player.health)


if __name__ == '__main__':
    rules.greeting()
    answer = input("Вы знаете правила? y / n  ")
    if rules.know(answer):
        rules.display_rules()
    language = "RU"
    print(f"\nСейчас установлен {language} язык\n")
    answer = input("Хотите поменять на ENG? y / n  ")
    if rules.know(answer) == False:
        language = "ENG"

    print(f"\nЗапуск {language} версии...\n")
    main(language)