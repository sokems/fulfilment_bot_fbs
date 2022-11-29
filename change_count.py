import json

def change_count_id(id, count_item):
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    for i in range(len(list_items)):
        if list_items[i]["id"] == id:
            list_items[i]["Количество"] = count_item
            break
    with open('items.json', 'w', encoding='utf-8') as file_2:
        json.dump(list_items, file_2, ensure_ascii=False)