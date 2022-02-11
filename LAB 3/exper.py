import random


def main():
    game_status = 1
    my_score = 10
    computer_score = 10
    print('Squid Game')
    print('___Правила___')
    input('Введіть ваш нік:')

    def design():
        x = "****"
        return x * 10

    def game():
        while game_status != 0:
            while my_score > 0 or computer_score > 0:
                print("Введіть кількість камінців, яку ви візьмете: ")
                my_stones = int(input(">>> "))
                if my_stones <= my_score > 0 and type(my_stones) == int:
                    computer_answer = random.randint(1, 2)
                    if computer_answer == 1:
                        print("Я думаю, що у вас непарна кількість")
                    else:
                        print("Я думаю, що у вас парна кількість")
                    if (my_stones % 2 == 0 and computer_answer == 2) or (my_stones
                                                                         % 2 != 0 and computer_answer == 1):
                        my_score = my_score - my_stones
                        computer_score = computer_score + my_stones
                        if my_score < 0:
                            my_score = 0
                            computer_score = 20
                        elif my_score > 20:
                            my_score = 20
                            computer_score = 0
                        print("Я відгадала. У вас залишилось", my_score,
                              "шт. А у мене ", computer_score, "шт")
                        print(design())
                        if my_score <= 1:
                            print("Ви програли")
                            game_status = 0
                            break
                        elif computer_score <= 1:
                            print("Ви виграли")
                            game_status = 0
                            break
                    else:
                        my_score = my_score + my_stones
                        computer_score = computer_score - my_stones
                        if computer_score < 0:
                            computer_score = 0
                            my_score = 20
                        elif computer_score > 20:
                            computer_score = 20
                            my_score = 0
                        print(">>> Я не відгадала. У вас залишилось",
                              my_score, "шт. А у мене ", computer_score, "шт")
                        print(design())
                        if my_score <= 1:
                            print(">>> Ви програли")
                            game_status = 0
                            break
                        elif computer_score == 0:
                            print(">>> Ви виграли")
                            game_status = 0
                            break
                elif my_stones > my_score:
                    print("У вас не має так багато камінців")
                elif my_stones <= 0 or my_stones == "":
                    print("Ви повинні взяти хоча б один камінець")
                else:
                    print("Ви ввели не число!")
            break
    game()
    response = input("Do you want to continue? (Y or N)")
    while response != "Y" or response != "N" or response != "y"\
            or response != "n":
        response = input("Do you want to continue? (Y or N)")

    print("Goodbye!")


main()
