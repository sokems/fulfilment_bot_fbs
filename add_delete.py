import json

def new_dict_item(dict):
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    new_dict = dict
    max = 0
    for item in list_items:
        if item["id"] > max:
            max = item["id"] + 1
            new_dict["id"] = max
        else:
            max += 1
            new_dict["id"] = max
    return new_dict

def add(dict_item):
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    list_items.append(dict_item)
    with open('items.json', 'w', encoding='utf-8') as file_2:
        json.dump(list_items, file_2, ensure_ascii=False)

def item_delete(id_item):
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)

    check = 0
    for i in range(len(list_items)):
        if list_items[i]['id'] == int(id_item):
            del list_items[i]
            check = 1
            break

    with open('items.json', 'w', encoding='utf-8') as file_2:
        json.dump(list_items, file_2, ensure_ascii=False)

    if check == 1:
        return f'Товар с ID: {id_item} удален'
    else:
        return 'Данного ID нет'