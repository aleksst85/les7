from config import JSON_PATCH
from util import game_space, parse_input, load_json
questions = load_json(JSON_PATCH)
game_space(questions)
number_of_games = 1
score = 0
while number_of_games <= 9:
    try:
        quest_num = input("Введите категорию и стоимость через пробел\n")
        category, count = parse_input(quest_num)
        if not questions[category][count]['asked']:
            print(f"Переведите слово: {questions[category][count]['question']}?")
            ansver = input("Ваш ответ:")
            if ansver.lower() == questions[category][count]['answer']:
                score += int(count)
                print(f"Правильно вы получаете {count} очков. Всего заработано {score} очков.")
                questions[category][count]['asked'] = True
            else:
                score -= int(count)
                print(f'Не правильно правильный ответ {questions[category][count]["answer"]} минус {count} очков. Всего заработано {score} очков')
                questions[category][count]['asked'] = True
            number_of_games += 1
        else:
            print("Вы уже отвечали на этот вопрос!")
        game_space(questions)
    except:
        print('Ошибка. Для завершения введите yes и Enter. Для продолжения игры просто Enter')
        exit = input()
        if exit == 'yes':
            print(f"Спасибо за игру вы заработали {score} очков. ")
            quit()
        else:
            continue
