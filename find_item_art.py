import json

def show_item(art, ul, mp):
    res_str = ''
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    if mp == 'OZON':
        for item in list_items:
            if (art in (item['Артикул OZON'])) and (ul in (item['ИП'])):
                res_str += f'ID товара: {item["id"]}\nНаименование товара: {item["Название"]}' \
                           f'\nНаименование ИП: {item["ИП"]}\nНазвание Магазина в OZON: {item["Название Магазина в OZON"]}' \
                           f'\nКоличество на складе: {item["Количество"]}\nАртикул WB: {item["Артикул WB"]}' \
                           f'\nАртикул OZON: {item["Артикул OZON"]}\nЦвет: {item["Цвет"]}' \
                           f'\nРазмер: {item["Размер"]}\nВо что упаковываем: {item["Упаковка"]}' \
                           f'\nЧто в подарок: {item["Подарок"]}\nКомментарий: {item["Комментарий"]}' \
                           f'\nМесто на складе: {item["Место"]}\n————————————————————\n'
    elif mp == 'WB':
        for item in list_items:
            if (art in (item['Артикул WB'])) and (ul in (item['ИП'])):
                res_str += f'ID товара: {item["id"]}\nНаименование товара: {item["Название"]}' \
                           f'\nНаименование ИП: {item["ИП"]}\nНазвание Магазина в OZON: {item["Название Магазина в OZON"]}' \
                           f'\nКоличество на складе: {item["Количество"]}\nАртикул WB: {item["Артикул WB"]}' \
                           f'\nАртикул OZON: {item["Артикул OZON"]}\nЦвет: {item["Цвет"]}' \
                           f'\nРазмер: {item["Размер"]}\nВо что упаковываем: {item["Упаковка"]}' \
                           f'\nЧто в подарок: {item["Подарок"]}\nКомментарий: {item["Комментарий"]}' \
                           f'\nМесто на складе: {item["Место"]}\n————————————————————\n'
    if res_str == '':
        res_str = 'Товаров с таким актикулом не найдено'
    return res_str

def how_id_item(art, ul, mp):
    id_item = ''
    with open('items.json', 'r', encoding='utf-8') as file:
        list_items = json.load(file)
    if mp == 'OZON':
        for item in list_items:
            if (art in (item['Артикул OZON'])) and (ul in (item['ИП'])):
                id_item = item['id']
    elif mp == 'WB':
        for item in list_items:
            if (art in (item['Артикул WB'])) and (ul in (item['ИП'])):
                id_item = item['id']
    return id_item