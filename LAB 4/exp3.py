import random


def squid_game():
    game_status = 1
    my_score = 10
    computer_score = 10
    print('Squid Game')
    introduction = """Правила гри Squid Game:
        У тебе є 10 камінців і у мене також 10. Тобі потрібно загадати число від 1 до 10,
        а я у свою чергу повинна відгадити чи твоє число парне чи ні.
        Якщо я відгадала,я забираю число твоїх загаданих камінців.
        Гра продовжується поки число камінців у кожного не дорівнює 0.
        Після кожного загаданого числа ти отримуватимеш фітбек:
        -Я відгадала.
        -Я не відгадала.
        -У тебе не має так багато камінців(якщо ти ввів число > 10.
        -Ти виграв.
        -Ти програв. 
        Також після кожного раунду тобі буде висвічуватись кількість твоїх камінців.
        """
    print('Введіть ваш нік:')
    user_input = input(">>> ")
    print(f"{user_input}, Вітаю у грі Squid Game.")
    print(introduction)

    def design():
        x = "****"
        return x * 10

    while game_status != 0:
        while my_score > 0 or computer_score > 0:
            print("Введіть кількість камінців, яку ти візьмеш: ")
            my_stones = int(input(">>> "))
            if my_stones <= my_score > 0 and type(my_stones) == int:
                computer_answer = random.randint(1, 2)
                if computer_answer == 1:
                    print("Я думаю, що у тебе непарна кількість")
                else:
                    print("Я думаю, що у тебе парна кількість")
                if (my_stones % 2 == 0 and computer_answer == 2) or \
                        (my_stones % 2 != 0 and computer_answer == 1):
                    my_score = my_score - my_stones
                    computer_score = computer_score + my_stones
                    if my_score < 0:
                        my_score = 0
                        computer_score = 20
                    elif my_score > 20:
                        my_score = 20
                        computer_score = 0
                    print("Я відгадала. У у тебе залишилось", my_score,
                          "шт. А у мене ", computer_score, "шт")
                    print(design())
                    if my_score <= 1:
                        print("Ти програв")
                        game_status = 0
                        break
                    elif computer_score <= 1:
                        print("Ти виграв")

                        # game_status = 0
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
                    print(">>> Я не відгадала. У тебе залишилось",
                          my_score, "шт. А у мене ", computer_score, "шт")
                    print(design())
                    if my_score <= 1:
                        print(">>> Ти програв")
                        # game_status = 0
                        break
                    elif computer_score == 0:
                        print(">>>  Ти виграв")
                        # game_status = 0
                        break
            elif my_stones > my_score:
                print("У тебе не має так багато камінців")
            elif my_stones <= 0 or my_stones == "":
                print("Ти повинен взяти хоча б один камінець")
            else:
                print("Ти ввів не число!")
        break

    print(f"{user_input},Goodbye!")
    