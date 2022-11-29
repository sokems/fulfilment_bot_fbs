import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import add_delete
import find_item_art
import ul
import boxes
import change_count
import edit_items
import json

API = '5793710878:AAEOgRsMq6tm0jmWd8sUcAjprU_FT-NHQok'
bot = telebot.TeleBot(API)

filter_dict = {"id": "","Фото": "","Название": "", "ИП": "", "Название Магазина в OZON": "",
  "Количество": "", "Артикул WB": "", "Артикул OZON": "","Цвет": "",
  "Размер": "", "Упаковка": "", "Подарок": "", "Комментарий": "", "Место": ""}
new_item = {}
add_item = False
add_set_1 = False
add_set_2 = False
add_set_3 = False
add_set_4 = False
add_set_5 = False
add_set_6 = False
add_set_7 = False
add_set_8 = False
add_set_9 = False
add_set_10 = False
add_set_11 = False
add_set_12 = False
add_set_13 = False
find_item = False
ost_ul = False
what_in_box = False
count_item = False
change_count_item = False
id_item = 0
new_item = {}
find_item_ul = False
choose_ul = ''
mp = False
choose_mp = ''
edit_item = False
all_edit_item = False
choose_id = ''
choose_pr = ''
edit_pr = False
del_item = False
del_item_sure = False

# def find_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 3
#     markup.add(InlineKeyboardButton(" ", callback_data="/gyms"),
#                InlineKeyboardButton(" ", callback_data="/exercises"),
#                InlineKeyboardButton(" ", callback_data="/add_training"))
#     return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Добавить новый товар')
    btn2 = types.KeyboardButton('Поиск товара по артикулу')
    btn3 = types.KeyboardButton('Отобразить остатки по ЮЛ')
    btn4 = types.KeyboardButton('Что в коробке?')
    btn5 = types.KeyboardButton('Редактировать товар')
    btn6 = types.KeyboardButton('Изменить количество товара')
    btn7 = types.KeyboardButton('Удалить товар')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    global add_set_1
    global new_item
    if add_set_1:
        bot.send_message(message.chat.id, 'Название товара:')
        add_set_1 = False
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = f'pic/' + str(new_item['id']) + '.jpg'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, 'Фото сохранено')
        except Exception as e:
            bot.reply_to(message, e)


@bot.message_handler(content_types='text')
def text_message(message):
    global add_item
    global add_set_1
    global add_set_2
    global add_set_3
    global add_set_4
    global add_set_5
    global add_set_6
    global add_set_7
    global add_set_8
    global add_set_9
    global add_set_10
    global add_set_11
    global add_set_12
    global add_set_13
    global filter_dict
    global new_item
    global find_item
    global ost_ul
    global what_in_box
    global count_item
    global change_count_item
    global id_item
    global new_item
    global find_item_ul
    global choose_ul
    global mp
    global choose_mp
    global edit_item
    global all_edit_item
    global choose_id
    global choose_pr
    global edit_pr
    global del_item
    global del_item_sure

    if message.text == 'Добавить новый товар':
        add_item = True
        add_set_1 = True
        add_set_2 = True
        add_set_3 = True
        add_set_4 = True
        add_set_5 = True
        add_set_6 = True
        add_set_7 = True
        add_set_8 = True
        add_set_9 = True
        add_set_10 = True
        add_set_11 = True
        add_set_12 = True
        add_set_13 = True
        new_item = add_delete.new_dict_item(filter_dict)
        bot.send_message(message.chat.id, 'Отправьте фото товара')

    elif message.text == 'Редактировать товар':
        bot.send_message(message.chat.id, 'Введите ID товара:')
        edit_item = True

    elif message.text == 'Главное меню':
        all_edit_item = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Добавить новый товар')
        btn2 = types.KeyboardButton('Поиск товара по артикулу')
        btn3 = types.KeyboardButton('Отобразить остатки по ЮЛ')
        btn4 = types.KeyboardButton('Что в коробке?')
        btn5 = types.KeyboardButton('Редактировать товар')
        btn6 = types.KeyboardButton('Изменить количество товара')
        btn7 = types.KeyboardButton('Удалить товар')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text="Главное меню", reply_markup=markup)

    elif edit_item:
        choose_id = message.text
        edit_item = False
        all_edit_item = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Название')
        btn2 = types.KeyboardButton('Наименование ИП')
        btn3 = types.KeyboardButton('Название Магазина в OZON')
        btn4 = types.KeyboardButton('Артикул WB')
        btn5 = types.KeyboardButton('Артикул OZON')
        btn6 = types.KeyboardButton('Цвет')
        btn7 = types.KeyboardButton('Размер')
        btn8 = types.KeyboardButton('Упаковка')
        btn9 = types.KeyboardButton('Подарок')
        btn10 = types.KeyboardButton('Комментарий')
        btn11 = types.KeyboardButton('Место')
        btn12 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.chat.id, text="Что вы хотите отредактировать?", reply_markup=markup)

    elif message.text == 'Удалить товар':
        del_item = True
        bot.send_message(message.chat.id, 'Введите ID товара, который хотите удалить:')

    elif del_item:
        del_item = False
        del_item_sure = True
        choose_id = message.text
        bot.send_message(message.chat.id, f'Вы уверены, что хотите удалить товар с ID: {choose_id}? (да/нет)')

    elif del_item_sure:
        if message.text.upper() == 'ДА':
            bot.send_message(message.chat.id, add_delete.item_delete(choose_id))
            del_item_sure = False
        elif message.text.upper() == 'НЕТ':
            del_item_sure = False
            bot.send_message(message.chat.id, 'Неккоректно введен ID товара')
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton('Добавить новый товар')
            btn2 = types.KeyboardButton('Поиск товара по артикулу')
            btn3 = types.KeyboardButton('Отобразить остатки по ЮЛ')
            btn4 = types.KeyboardButton('Что в коробке?')
            btn5 = types.KeyboardButton('Редактировать товар')
            btn6 = types.KeyboardButton('Изменить количество товара')
            btn7 = types.KeyboardButton('Удалить товар')
            markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(message.chat.id, text="Возврат в главное меню", reply_markup=markup2)
        else:
            bot.send_message(message.chat.id, f'Вы уверены, что хотите удалить товар с ID: {choose_id}? (да/нет)')

    elif all_edit_item:
        all_edit_item = False
        choose_pr = message.text
        edit_pr = True
        bot.send_message(message.chat.id, 'Введите новое значение параметра:')

    elif edit_pr:
        edit_pr = False
        try:
            bot.send_message(message.chat.id, edit_items.edit_item_pr(choose_id, choose_pr, message.text))
        except:
            bot.send_message(message.chat.id, 'Неккоректно введен ID товара')
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Добавить новый товар')
        btn2 = types.KeyboardButton('Поиск товара по артикулу')
        btn3 = types.KeyboardButton('Отобразить остатки по ЮЛ')
        btn4 = types.KeyboardButton('Что в коробке?')
        btn5 = types.KeyboardButton('Редактировать товар')
        btn6 = types.KeyboardButton('Изменить количество товара')
        btn7 = types.KeyboardButton('Удалить товар')
        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text="Возврат в главное меню", reply_markup=markup2)

    elif message.text == 'Поиск товара по артикулу':
        bot.send_message(message.chat.id, "Выберите ИП")
        find_item_ul = True
        # list_ul = ul.show_list_ul()
        # mes = 'Список ЮЛ:'
        # keyboard = types.InlineKeyboardMarkup()
        # keyboard.row_width = 5
        #
        # for u in list_ul:
        #     keyboard.add(types.InlineKeyboardButton(u, callback_data='start'))
        #
        # bot.send_message(message.chat.id, mes, reply_markup=keyboard)
        list_ul = ul.show_list_ul()
        bot.send_message(message.chat.id, '\n'.join(list_ul))


    elif find_item_ul:
        choose_ul = message.text.title()
        bot.send_message(message.chat.id, "OZON или WB?")
        mp = True
        find_item_ul = False

    elif mp:
        choose_mp = message.text.upper()
        if choose_mp != 'OZON' and choose_mp != 'WB':
            bot.send_message(message.chat.id, "Некорректное имя маркетплейса")
        else:
            bot.send_message(message.chat.id, "Введите артикул товара:")
            find_item = True
            mp = False

    elif message.text == 'Что в коробке?':
        bot.send_message(message.chat.id, "Введите номер коробки:")
        what_in_box = True

    elif message.text == 'Изменить количество товара':
        bot.send_message(message.chat.id, "Введите ID товара:")
        count_item = True

    elif count_item:
        id_item = int(message.text)
        bot.send_message(message.chat.id, "Введите количество данного товара:")
        count_item = False
        change_count_item = True

    elif change_count_item:
        change_count.change_count_id(id_item, message.text)
        bot.send_message(message.chat.id, "Количество успешно изменено!")
        change_count_item = False

    elif what_in_box:
        box = message.text.upper()
        bot.send_message(message.chat.id, boxes.show_box(box))
        what_in_box = False

    elif find_item:
        id_pic = find_item_art.how_id_item(message.text, choose_ul, choose_mp)
        if id_pic == '':
            bot.send_message(message.chat.id, 'Такого товара нет!')
            find_item = False
            choose_ul = ''
            choose_mp = ''
        else:
            name_pic = f'pic/{id_pic}.jpg'
            pic = open(name_pic, 'rb')
            bot.send_photo(message.chat.id, pic)
            bot.send_message(message.chat.id, find_item_art.show_item(message.text, choose_ul, choose_mp))
            find_item = False
            choose_ul = ''
            choose_mp = ''

    elif message.text == 'Отобразить остатки по ЮЛ':
        bot.send_message(message.chat.id, "Список ИП:")
        list_ul = ul.show_list_ul()
        bot.send_message(message.chat.id, '\n'.join(list_ul))
        bot.send_message(message.chat.id, "По какому ИП Вы хотите посмотреть остатки?")
        ost_ul = True

    elif ost_ul:
        bot.send_message(message.chat.id, ul.show_ul(message.text))
        ost_ul = False

    elif add_item:
        if add_set_2:
            new_item['Название'] = message.text.capitalize()
            bot.send_message(message.chat.id, 'Наименование ИП:')
            add_set_2 = False

        elif add_set_3:
            new_item['ИП'] = message.text.title()
            bot.send_message(message.chat.id, 'Название Магазина в OZON:')
            add_set_3 = False

        elif add_set_4:
            new_item['Название Магазина в OZON'] = message.text.upper()
            bot.send_message(message.chat.id, 'Количество на складе:')
            add_set_4 = False

        elif add_set_5:
            new_item['Количество'] = message.text
            bot.send_message(message.chat.id, 'Артикул WB:')
            add_set_5 = False

        elif add_set_6:
            new_item['Артикул WB'] = message.text
            bot.send_message(message.chat.id, 'Артикул OZON:')
            add_set_6 = False

        elif add_set_7:
            new_item['Артикул OZON'] = message.text
            bot.send_message(message.chat.id, 'Цвет:')
            add_set_7 = False

        elif add_set_8:
            new_item['Цвет'] = message.text
            bot.send_message(message.chat.id, 'Размер (не габариты!):')
            add_set_8 = False

        elif add_set_9:
            new_item['Размер'] = message.text
            bot.send_message(message.chat.id, 'Во что упаковываем (стретч-пленку для OZON не указываем):')
            add_set_9 = False

        elif add_set_10:
            new_item['Упаковка'] = message.text
            bot.send_message(message.chat.id, 'Что кладем в подарок:')
            add_set_10 = False

        elif add_set_11:
            new_item['Подарок'] = message.text
            bot.send_message(message.chat.id, 'Комментарий:')
            add_set_11 = False

        elif add_set_12:
            new_item['Комментарий'] = message.text
            bot.send_message(message.chat.id, 'Место на складе (если в нескольких коробках, то указывайте через пробел):')
            add_set_12 = False

        elif add_set_13:
            new_item['Место'] = message.text.upper()
            bot.send_message(message.chat.id, 'Товар добавлен!')
            add_set_13 = False
            add_item = False
            add_delete.add(new_item)
    else:
        bot.send_message(message.chat.id, 'Я Вас не понял(')

bot.polling()