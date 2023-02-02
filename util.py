import json
def game_space(questions):
    """Создаем и модифицируем  игровое пространство"""
    for quest in questions:
        price_list = []
        for i in questions[quest]:
            for j in questions[quest][i]:
               position = questions[quest][i]['asked']
            if not position:
                price_list.append(i)
            else:
                price_list.append("...")
        print(f"{quest}{(15-len(quest))*' '}{'   '.join(price_list)}")


def parse_input(quest_num):
    category, count = quest_num.split(" ")
    return category, count

def load_json(patch):
    with open(patch, 'r') as file:
        data_json = file.read()
    questions = json.loads(data_json)
    return questions