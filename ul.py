import json

def show_list_ul():
    list_ul = []
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    for item in list_items:
        if item["ИП"] not in list_ul:
            list_ul.append(item["ИП"])
    return list_ul

def show_ul(message):
    res_str = ''
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    for item in list_items:
        if message in (item['ИП']):
            res_str += f'\nНаименование ИП: {item["ИП"]}\nНазвание Магазина в OZON: {item["Название Магазина в OZON"]}\n\n'
            break
    for item in list_items:
        if message in (item['ИП']):
            res_str += f'ID товара: {item["id"]}\nНаименование товара: {item["Название"]}' \
                       f'\nКоличество на складе: {item["Количество"]}\nАртикул WB: {item["Артикул WB"]}' \
                       f'\nАртикул OZON: {item["Артикул OZON"]}\n' \
                       f'\nМесто на складе: {item["Место"]}\n————————————————————\n'
    if res_str == '':
        res_str = 'Таких ИП не найдено'
    return res_str
