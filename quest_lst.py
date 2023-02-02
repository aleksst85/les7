import json
questions = {
    "Транспорт":{
        "100":{"question":"plane", "answer":"самолет", "asked":False},
        "200":{"question":"train", "answer":"поезд", "asked":False},
        "300":{"question":"boarding", "answer":"посадка", "asked":False}},
    "Животные":{
        "100":{"question":"dog", "answer":"собака", "asked":False},
        "200":{"question":"shark", "answer":"акула", "asked":False},
        "300":{"question":"sparrow", "answer":"воробей", "asked":False},
        "400":{"question":"sparrow", "answer":"воробей", "asked":False}},
    "Фрукты":{
        "100":{"question":"aplle", "answer":"яблоко", "asked":False},
        "200":{"question":"berry", "answer":"ягода", "asked":False},
        "300":{"question":"vension", "answer":"оленина", "asked":False},
    }
    }
with open('data.json', 'r') as file:
    data_json = f.read()

questions = json.loads(data_json)
print(profile)
