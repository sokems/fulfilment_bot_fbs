import json

def show_box(message):
    res_str = ''
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    for item in list_items:
        if message in (item['Место']):
            res_str += f'ID товара: {item["id"]}\nНаименование товара: {item["Название"]}' \
                       f'\nНаименование ИП: {item["ИП"]}\nНазвание Магазина в OZON: {item["Название Магазина в OZON"]}' \
                       f'\nАртикул WB: {item["Артикул WB"]}' \
                       f'\nАртикул OZON: {item["Артикул OZON"]}\nЦвет: {item["Цвет"]}' \
                       f'\nРазмер: {item["Размер"]}' \
                       f'\nЧто в подарок: {item["Подарок"]}\nКомментарий: {item["Комментарий"]}' \
                       f'\n————————————————————\n'
    if res_str == '':
        res_str = 'Таких коробок не найдено'
    return res_str