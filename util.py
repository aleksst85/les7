import json



def game_space(questions):
    """Создаем и модифицируем  игровое пространство"""
    for category_name, category_questions in questions.items():
        print(category_name.ljust(17), end="")
        for price, question_data in category_questions.items():
            asked = question_data['asked']
            if not asked:
                print(str(price).ljust(5), end="")
            else:
                print("   ".ljust(5), end="")
        print()


#   мой вариант
#        price_list = []
#        for i in questions[quest]:
#            for j in questions[quest][i]:
#               position = questions[quest][i]['asked']
#            if not position:
#                price_list.append(i)
#            else:
#                price_list.append("...")
#        print(f"{quest}{(15-len(quest))*' '}{'   '.join(price_list)}")


def parse_input(quest_num):
    category, count = quest_num.split(" ")
    return category, count


def load_json(patch):
    with open(patch, 'r') as file:
        data_json = file.read()
    questions = json.loads(data_json)
    return questions
