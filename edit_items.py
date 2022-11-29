import json

def edit_item_pr(id_item, pr, mes):
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)

    check = 0
    for item in list_items:
        if item['id'] == int(id_item):
            item[str(pr)] = mes
            check = 1

    with open('items.json', 'w', encoding='utf-8') as file_2:
        json.dump(list_items, file_2, ensure_ascii=False)

    if check == 1:
        return 'Информация успешно изменена'
    else:
        return 'Данного товара нет'

