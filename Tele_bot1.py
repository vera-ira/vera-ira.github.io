# ПЕРВЫЕ ШАГИ РАБОТЫ С БОТОМ
#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import constants1
import os
import random
import urllib.request as urllib2
import xlrd
from xlwt import Workbook
import json
import fsm_telebot
from fsm_telebot.storage.memory import MemoryStorage
from langdetect import detect
from telebot import types



storage = MemoryStorage()
bot = fsm_telebot.TeleBot(constants1.token, storage=storage)
#bot = telebot.TeleBot(constants1.token)
choic_dict={}

bot.send_message(115496560, 'Бот перезагрузился')

words_verb = xlrd.open_workbook('./Pealim_FINAL1.xlsx')
list = words_verb.sheet_by_index(0)
#bot.send_message(115496560, 'второй текст')

# ниже посмотрим, как работает ручное обновление.
#upd = bot.get_updates() # все обновления закидываем сюда
#print(upd)
#last_upd=upd[-1] # последнее обновление в списке берем
#message_from_user = last_upd.message # достаем сообщение из последнего обновления
#print(message_from_user)



def log (message,answer):
    print('\n ---------')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от:",message.from_user.first_name, ', id:', str(message.from_user.id))
    print("Текст сообщения:",message.text)
    print("Текст ответа:",answer)

def alert_new_user(message):
    from datetime import datetime
    if str(message.from_user.id) != str(115496560):
        alert_for_admin = str("В гостях у нашего бота неизвестный пользователь.\nuser.first_name: "+message.from_user.first_name+".\nid: "+str(message.from_user.id)+"\nДата/время: "+str(datetime.now())+"\n\nТекст запроса от user: "+str(message.text))
        bot.send_message(115496560, alert_for_admin)

    #mes_to_me=str("\nСообщение от: "+ message.from_user.first_name+" ID: "+str(message.from_user.id)+"\nТекст: "+ message.text)
    #bot.send_message(message.chat.id, mes_to_me)
    #bot.send_message(message.chat.id, "туту текст....", reply_markup=key)


    #print("Сообщение от {0} {1}. {id={2} \n Текст - {3}".format(message.from_user.first_name,
     #                                                           message.from_user.last_name,
      #                                                          str(message.from_user.id),
       #

def send_table(message, row, kind_of_table):
    row = int(row)
    def part2(colum,row):
        print('Вошли в def part2')
        i = ''
        if '~' in list.row(row)[colum + 1].value:
            i = (list.row(row)[colum + 1].value + ' {_' + list.row(row)[colum + 2].value + '_}')
        else:
            i = (' {_' + list.row(row)[colum + 2].value + '_}')
        ii = ''
        if list.row(row)[colum + 3].value != '':
            if '~' in list.row(row)[colum + 4].value:
                ii = ('; ' + list.row(row)[colum + 3].value + list.row(row)[colum + 4].value + ' {_' + list.row(row)[colum + 5].value + '_}')
            else:
                ii = ('; ' + list.row(row)[colum + 3].value + ' {_' + list.row(row)[colum + 5].value + '_}')
        return i + ii
    I = '*אֲנִי*'
    YOU_M = '*אַתָּה*'
    YOU_W = '*אַתְּ*'
    HE = '*הוּא*'
    SHE = '*הִיא*'
    WE = '*אֲנַחְנוּ*'
    YOU_MM = '*אַתֶּם*'
    YOU_WW = '*אַתֶּן*'
    THEY_MM = '*הֵם*'
    THEY_WW = '*הֵן*'
    Z = '*ז"*'
    N = '*נ"*'
    ZR = '*ז"ר*'
    NR = '*ז"ר*'
    answer1 = ('ע"ב '+"[@ivrit_bot](https://t.me/ivrit_bot)    \n"
            '*глагол*: '+list.row(row)[4].value+part2(4,row)+
            #'*инф.*: '
            '\n' + list.row(row)[3].value+ '\n'
            '*биньян.*: '+list.row(row)[10].value+'\n'
            '*корень*: '+list.row(row)[11].value+'\n'
            '*наст. вр.*:' + '\n'
            + Z + '-       '+list.row(row)[17].value +part2(17,row)+'\n'
            + N + '-       '+ list.row(row)[23].value +part2(23,row)+'\n'
            + ZR + '-     '+ list.row(row)[29].value +part2(29,row)+'\n'
            + NR + '-     '+ list.row(row)[35].value +part2(35,row)+'\n'
            '*прошед. вр.*:' + '\n'
            + I + '-      ' + list.row(row)[41].value +part2(41,row)+ '\n'
            + YOU_M + '-   ' + list.row(row)[47].value +part2(47,row)+ '\n'
            + YOU_W + '-      ' + list.row(row)[53].value +part2(53,row)+ '\n'
            + HE + '-     ' + list.row(row)[59].value +part2(59,row)+ '\n'
            + SHE + '-     ' + list.row(row)[65].value +part2(65,row)+ '\n'
            + WE + '-  ' + list.row(row)[71].value +part2(71,row)+ '\n'
            + YOU_MM + '-   ' + list.row(row)[77].value +part2(77,row)+ '\n'
            + YOU_WW + '-     ' + list.row(row)[83].value +part2(83,row)+ '\n'
            + THEY_MM + '/' + THEY_WW + '- ' + list.row(row)[89].value +part2(89,row)+ '\n'
            '*буд. вр.*:' + '\n'
            + I + '-     ' + list.row(row)[95].value +part2(95,row)+ '\n'
            + YOU_M + '-   ' + list.row(row)[101].value +part2(101,row)+ '\n'
            + YOU_W + '-      ' + list.row(row)[107].value +part2(107,row)+ '\n'
            + HE + '-     ' + list.row(row)[113].value +part2(113,row)+ '\n'
            + SHE + '-     ' + list.row(row)[119].value +part2(119,row)+ '\n'
            + WE + '-  ' + list.row(row)[125].value +part2(125,row)+ '\n'
            + YOU_MM + '-   ' + list.row(row)[131].value +part2(131,row)+ '\n'
            + YOU_WW + '-     ' + list.row(row)[137].value +part2(137,row)+ '\n'
            + THEY_MM + '/' + THEY_WW + '- ' + list.row(row)[143].value +part2(143,row)+ '\n')
    print(' Нашли answer1 ')
    answer2 = ('*пов. накл.*:' + '\n'
            + Z + '-       ' + list.row(row)[155].value +part2(155,row)+'\n'
            + N + '-       ' + list.row(row)[161].value +part2(161,row)+'\n'
            + ZR + '-     ' + list.row(row)[167].value +part2(167,row)+'\n'
            + NR + '-     ' + list.row(row)[173].value +part2(173,row)+'\n')

    footer = ('\n' +'_Сообщить об ошибке -_'+"[@vera_ira](https://t.me/vera_ira)")
    if kind_of_table == 'short':
        answer = answer1#+footer
    elif kind_of_table == 'long':
        answer = answer1+answer2+footer
    elif kind_of_table == 'long+pyal_hyfal':
        #data_but_py_hy = str("id_imper-"+ts_and_id+"id_py_hy-" + str(id_py_hy))
        print("row - ",row)
        print("list.row(row)[179].value",list.row(row)[179].value)
        id_py_hy = str(list.row(row)[179].value)
        #id_py_hy = str(list.row(row)[179].value)
        print("id_py_hy -------------------------------------",id_py_hy)

        for row_py_hy in range(4502, 5714):
            #print("ищу совпаление - ", str(list.row(row_py_hy)[2].value), "и", str(id_py_hy))
            #print("++++++++row_py_hy++++++++",row_py_hy)
            #print(str(list.row(row_py_hy)[2].value))
            if str(list.row(row_py_hy)[2].value) == str(id_py_hy):
                print("одинаковые")
                answer3 = ('*страдательный залог:*\n'
                    '*биньян*: ' + list.row(row_py_hy)[10].value + '\n'
                    #'*корень*: ' + list.row(row_py_hy)[11].value + '\n'
                    '*наст. вр.*:' + '\n'
                    + Z + '-       ' + list.row(row_py_hy)[17].value + part2(17,row_py_hy) + '\n'
                    + N + '-       ' + list.row(row_py_hy)[23].value + part2(23,row_py_hy) + '\n'
                    + ZR + '-     ' + list.row(row_py_hy)[29].value + part2(29,row_py_hy) + '\n'
                    + NR + '-     ' + list.row(row_py_hy)[35].value + part2(35,row_py_hy) + '\n'
                    '*прошед. вр.*:' + '\n'
                    + I + '-      ' + list.row(row_py_hy)[41].value + part2(41,row_py_hy) + '\n'
                    + YOU_M + '-   ' + list.row(row_py_hy)[47].value + part2(47,row_py_hy) + '\n'
                    + YOU_W + '-      ' + list.row(row_py_hy)[53].value + part2(53,row_py_hy) + '\n'
                    + HE + '-     ' + list.row(row_py_hy)[59].value + part2(59,row_py_hy) + '\n'
                    + SHE + '-     ' + list.row(row_py_hy)[65].value + part2(65,row_py_hy) + '\n'
                    + WE + '-  ' + list.row(row_py_hy)[71].value + part2(71,row_py_hy) + '\n'
                    + YOU_MM + '-   ' + list.row(row_py_hy)[77].value + part2(77,row_py_hy) + '\n'
                    + YOU_WW + '-     ' + list.row(row_py_hy)[83].value + part2(83,row_py_hy) + '\n'
                    + THEY_MM + '/' + THEY_WW + '- ' + list.row(row_py_hy)[89].value + part2(89,row_py_hy) + '\n'
                    '*буд. вр.*:' + '\n'
                    + I + '-     ' + list.row(row_py_hy)[95].value + part2(95,row_py_hy) + '\n'
                    + YOU_M + '-   ' + list.row(row_py_hy)[101].value + part2(101,row_py_hy) + '\n'
                    + YOU_W + '-      ' + list.row(row_py_hy)[107].value + part2(107,row_py_hy) + '\n'
                    + HE + '-     ' + list.row(row_py_hy)[113].value + part2(113,row_py_hy) + '\n'
                    + SHE + '-     ' + list.row(row_py_hy)[119].value + part2(119,row_py_hy) + '\n'
                    + WE + '-  ' + list.row(row_py_hy)[125].value + part2(125,row_py_hy) + '\n'
                    + YOU_MM + '-   ' + list.row(row_py_hy)[131].value + part2(131,row_py_hy) + '\n'
                    + YOU_WW + '-     ' + list.row(row_py_hy)[137].value + part2(137,row_py_hy) + '\n'
                    + THEY_MM + '/' + THEY_WW + '- ' + list.row(row_py_hy)[143].value + part2(143,row_py_hy) + '\n')
        answer = answer1 + answer2 + answer3 + footer

    #--------------
    '''
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    '''
    status_searching = 'Ответ в файле есть.'
    return answer


def make_batton_imper(message, ts_and_id,add_buttons):
    print("...................................СЕЙЧАС МЫ В make_batton_imper")
    print("...................................СЕЙЧАС МЫ В make_batton_imper")
    print("...................................СЕЙЧАС МЫ В make_batton_imper")
    print("add_buttons - ",add_buttons)
    key = telebot.types.InlineKeyboardMarkup(row_width=2) # задаем ее тип. Это клвиатура инлайн
    data_but_imper = str("id_imper" + str(ts_and_id))
    print("data_but_imper =", "id_imper" + str(ts_and_id) )
    but_imper = telebot.types.InlineKeyboardButton(text=" + Повелительное наклонение.", callback_data=data_but_imper)

    # elif add_buttons == "passiva" or add_buttons == "all":
    # if str(list.row(int(ts_and_id))[179].value) != "":
    #    print("----Нашли и в нужной ячеке НЕ пусто---")

    #id_py_hy = list.row(int(ts_and_id))[179].value

    data_but_py_hy = str("id_py_hy-" + str(ts_and_id))
    but_py_hy = telebot.types.InlineKeyboardButton(text=" + Страдательный залог.", callback_data=data_but_py_hy)

    if add_buttons == "no buttons":
        key.row()
    elif add_buttons == "passiva":
        print ("----Нажата кнопка после которой нужно сформировать кнопку пассива---")
        print("----СФОРМИРОВАЛИ КНОПКУ - Страдательный залог---")
        key.add(but_py_hy)
    elif add_buttons == "imper":
        key.row(but_imper)
    elif add_buttons == "all":
        key.row(but_imper, but_py_hy)
    return key

#kb1 = Types.InlineKeyboardMarkup(row_width=1) # самая длинная кнопка
#kb2 = Types.InlineKeyboardMarkup(row_width=2) # деление пополам
#kb3 = Types.InlineKeyboardMarkup(row_width=3) # деление на три равных кнопки

def make_battons(message, id_maybe_answer_links, status_searching, namber_bort):
    #Нужно - namber_bort, maybe_answer_links (или все id),
    print("...................................СЕЙЧАС МЫ В make_battons")
    print("----тестируем. что такое - id_maybe_answer_links -----",id_maybe_answer_links)
    print("message.message_id-",message.message_id)
    print("message-", message)
    sb = constants1.sum_buttons_on_botr
    if (int(namber_bort*sb))<=(int(len(id_maybe_answer_links))): #определяем сколько на этом борту напечатать кнопок. Если борт не последний, то печатаем кол-во sb. Оно забито в константах и изменить его можно там.
        #if len(maybe_answer_links) > 10:  # программа вуыдает ошибку, если список возможных слов слишком велик. Например если юзер ввел просто ы, то программа скорее всего предложит более 1000 слов. В чат все варианты невозможно отправить. Поэтому мы сокращаем этот список до 20 первых.
        #    del maybe_answer_links[10:]
        #    del id_maybe_answer_links[10:]
        botr = sb
    else:
        botr = sb-((int(namber_bort * sb))-(int(len(id_maybe_answer_links)))) #Если это последний борт, то тогда из sb вычитаем кол-во пустыхх мест.
    print("sb-",sb)
    # теперь определим, с какой кнопки начнем и какой закончим.
    start = (int(namber_bort*sb)-int(sb))
    print("start-", start)
    stop = (start+botr)
    print("stop-", stop)
    key = telebot.types.InlineKeyboardMarkup() # задаем ее тип. Это клвиатура инлайн
    # тут начиная с кнопки start и заканчивая stop делаем кнопки.
    for nomer in range(start,stop):
        print("печатаем данные о под номером - ",nomer)
        print("-----------------")
        print("-----------------")
        print("1---- ",str(id_maybe_answer_links[nomer])) #- это извлекли Id глагола из списка преданного.
        print("2---- ",str(list.row((int(id_maybe_answer_links[int(nomer)]))+int(constants1.table_start))[4].value)) #"- так мы из таблицы достали инфинитив глагола на иврите. 4 столбик. constants1.table_start - это номер начал таблицы. нужен для поиска глагола
        print("3---- ",str(list.row((int(id_maybe_answer_links[int(nomer)])) + int(constants1.table_start))[3].value)) # -  так мы из таблицы извлекли перевод на русский язык в инфинитиве. 3 столбик
        but = telebot.types.InlineKeyboardButton(
            text=str(str(list.row((int(id_maybe_answer_links[int(nomer)]))+int(constants1.table_start))[4].value) + '- '+ str(list.row((int(id_maybe_answer_links[int(nomer)])) + int(constants1.table_start))[3].value)),
            callback_data = str(id_maybe_answer_links[nomer]))
        key.add(but)  # добавляем каждую в клавиатуру, которую задали ранее
        # тут сделаем кнопки нижние, если кол-во элементов для вывода больше sd (заданное кол-во кнопок на на одном выводе\борту)
    next = len(id_maybe_answer_links)-stop
    print("next-",next)
    text_but_next=(str(next)+">>")
    n = int(namber_bort)+1
    data_but_next = ("id_botr-" + str(n) + "-test-" + str(message.message_id))
    but_next = telebot.types.InlineKeyboardButton(text=text_but_next, callback_data=data_but_next)
    befor = int(start)
    print("befor-", befor)
    text_but_befor = ("<<"+str(befor))
    b = int(namber_bort)-1
    data_but_befor = ("id_botr-" + str(b) + "-test-" + str(message.message_id))
    but_befor = telebot.types.InlineKeyboardButton(text=text_but_befor, callback_data=data_but_befor)
    if (len(id_maybe_answer_links)/sb)>1: #если кнопки не уместятся на 1 борту, то делаем доп кнопки прокрутки.
        if namber_bort == 1: # если мы в б первом ботру, то...
            key.row(but_next) # так добавили кнопку , через row
        elif (len(id_maybe_answer_links))/sb<=namber_bort: # если мы в б последнем ботру, то...
            key.row(but_befor) # так добавили кнопку , через row
        else: # иначе мы в середнем борту,то...
            key.row(but_befor, but_next) # так добавили обе кнопки

    #-------------------ниже старый вариант записи данных

    #wd = Workbook()
    #sheet1=wd.add_sheet("for buttons")
    #sheet1.write(2, 1, message.message_id)
    #sheet1.write(2, 5, len(id_maybe_answer_links))
    #wd.save('words_first.xls')

    #--------------------Ниже новый вариант записи данных
    print("message.message_id в json ------ ",message.message_id)
    print("id_maybe_answer_links в json ---",id_maybe_answer_links)
    for_group_buttons = { #Дальше создаю словарь с данными о результатах поиска в базе. Это передам в кнопку.
        "message.message_id": message.message_id,
        "info_buttons":{
            "status_searching": status_searching,
            "namber_bort": namber_bort,
            "id_maybe_answer_links": id_maybe_answer_links
        }
    }
    try: #тут проверяю, есть ли такой объект и файл уже (на случай если я его удалю). Если есть, то работает с ним.
        many_battons = json.load(open("many_battons.json"))
    except: # если такоего объекта и файла нет, то создает новый список. пока пустой
        many_battons = []
    many_battons.append(for_group_buttons) #тут добавляет в json файл новый
    with open("many_battons.json", "w") as file:
        json.dump(many_battons, file, ensure_ascii=True)
        print("добавили данные о кнопках")
    return key  # эта строка должна быть в конце функции всей
""" 
# ---- эта чать ниже, это проверка записанных данных. Ее можно удалить.
    file = open("many_battons.json", "r")
    new_info = json.load(file)
    for i in new_info:
        print("ПЕЧАТАЕМ ВСЮ что внути json.............................................................")
        print("ТУТУ НАПЕЧАТАЕМ СПИСОК ИЗ ID" +(str(i["info_buttons"]["id_maybe_answer_links"])))
"""


@bot.message_handler(commands=['info'])
def handle_text(message):
    choic_dict[message.chat.id]= 0
    bot.send_message(message.chat.id, 'Я бот. И знаю почти все глаголы в иврите. Люблю делиться знаниями.'
                                      'Если у тебя есть предложения или вопросы к моему создателю, напиши сюда - @vera_ira.')
    alert_new_user(message)

@bot.message_handler(commands=['start'])
def handle_text(message):
    choic_dict[message.chat.id] = 0
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/start','/info')
    #user_markup.row ('фото','аудио','документ')
    #user_markup.row('стикер','видео','голос','локация')
    hi_name=str('Привет, '+message.from_user.first_name+'!\nОтправляй мне любой глагол.')
    bot.send_message(message.chat.id, hi_name, reply_markup=user_markup)
    #bot.send_message(message.chat.id, '.', reply_markup=user_markup)
    #bot.send_message(message.chat.id, 'Привет! Чем я могу тебе помочь?')
    #buttons == "do not need a choice"
    alert_new_user(message)

@bot.message_handler(commands=['stop'])
def handle_text(message):
    choic_dict[message.chat.id] = 0
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Клавиатуру свернули, Но ты ее всегда можешь развернуть обратно.', reply_markup = remove_markup)
    #buttons == "do not need a choice"

"""
# думаю, эту чать ниже можно удалить.
def inline(message): #all_answer_links, answer_links
    key = telebot.types.InlineKeyboardMarkup()
    for k in range(len(answer_links)):
        but = telebot.types.InlineKeyboardButton(text=answer_links[k], callback_data=answer_links[k])
        key.add(but)
    bot.send_message(message.chat.id , "туту текст....", reply_markup=key)
"""

@bot.message_handler(content_types=['text'])
def handle_text(message):
    alert_new_user(message)
    mes = message.text
    mes = mes.lower() # Все буквы меняем на мленькие
    mes = mes.split(',')  # разделяем по запятой смс-запрос
    status_searching = 'Ответа в файле нет.'
    if '*' in mes:
        bot.send_message(message.chat.id, 'Я не знаю такого символа * . Введите запрос заново.', parse_mode='Markdown')
    #words_verb = xlrd.open_workbook('./Pealim_FINAL.xlsx') # Открываем файл эксель из папки в которой находится программа
    #list = words_verb.sheet_by_index(0)  # открываем первый лист (индекс 0)
    maybe_answer_links = [] #Сюда будем заносить все возможные ответы.
    id_maybe_answer_links = []
    inf_maybe_answer_links = []
    tx_maybe_answer_links = []
    answer_links = [] #Сюда будем заносить все подходяшие ответы.
    id_answer_links = [] #Это нужный список, туда будем добавлять, все верное.
    inf_answer_links = []
    #print("mes-",mes)
    for one_word in mes:
        one_word = one_word.lstrip()  # убрали пробелы вначале текста в смс-запросе
        print("НАЧИНАЕМ ПОИСК В ТАБЛИЦЕ")
        for row in range(2, 4307): # Открываем каждую строку поочереди начиная со третей строки (шапку не читаем). Сейчас строк всего 4310.
            if one_word in list.row(row)[3].value:   # Если значение в столбце под индексом 3 (толбец с переводом), соответствует переменной mes, то
                print("Ншел подходящий перевод в строке - ",row )
                #maybe_answer_links.append(list.row(row)[3].value) #добавляет это значенте в список возможных
                id_maybe_answer_links.append(int(list.row(row)[2].value)) #добавляет его id в список возможных
                print("добавили в список id_maybe_answer_links -",int(list.row(row)[2].value))
                #inf_maybe_answer_links.append(list.row(row)[4].value) #добавляет его инфинитив на иврите в список возможных
                tx_maybe_answer_links.append(list.row(row)[4].value+'- '+list.row(row)[3].value) # тут составили текст, который будет отображаться на кнопке

                # --------------это можно куда-то перенести в другое место
                if len(tx_maybe_answer_links[-1]) > 35:
                    print('Знаков на кнопке больше 35 - ',tx_maybe_answer_links[-1])
                # --------------это можно куда-то перенести в другое место

                print("--------------------")
                ru_trans = list.row(row)[3].value.split(',') # разделяем по запятой значения с ответами
                sum_verbs_in_the_row = 0 # Тут будем считать сколько подходящих нам слов в этой строке. Пока - 0.
                print("сейчас проверяем полностью ответ совпадает или нет................")
                for word in ru_trans:
                    word = word.lstrip()  # убрали пробелы вначале текста в строке
                    if word[0: len(one_word)] == one_word and sum_verbs_in_the_row == 0: # если первые символы каждого слова(слово имеется ввиду, текст между запятыми) равны смс-запросу. И это первая проверка в строке, то
                        id_answer_links.append(int(list.row(row)[2].value)) #добавляем id перевода который, точно подходит. Верный перевод.
                        #inf_answer_links.append(list.row(row)[4].value)
                        #answer_links.append(list.row(row)[3].value) # добавляем ответ в список  ответов.
                        sum_verbs_in_the_row += 1 # Увеличиваем счетчик слов в строке на 1
    print("СОБРАЛИ ОТВЕТОВ MAYBE - ", len(id_maybe_answer_links), ". Все: ",id_maybe_answer_links)
    print("СОБРАЛИ ОТВЕТОВ YES   - ", len(id_answer_links), ". Все: ",id_answer_links)
    # Сначала определим есть ли подходящие ответы. Сели нет, то тогда предоставим примерные ответы по запросу.

    if len(id_answer_links) != 0:
        id_maybe_answer_links = id_answer_links #если подходящие ответы есть, то дальше будем делать все манипуляции с этим списком ответов
        status_searching = 'Ответ в файле есть.'
        print("id_maybe_answer_links присвоили список id_answer_links. Он теперь такой - ", id_answer_links)

    if len(id_maybe_answer_links) == 1:
        ts_plus_id_answer_links = int(constants1.table_start)+int(id_maybe_answer_links[0]) #constants1.table_start - это начало таблицы. помогает быстро найти строку в таблиуе. Для поска прибавляем эту констунту к id глагола
        if str(list.row(int(ts_plus_id_answer_links))[179].value) != "":
            key = make_batton_imper(message, str(ts_plus_id_answer_links),add_buttons="all")
        else:
            key = make_batton_imper(message, str(ts_plus_id_answer_links), add_buttons="imper")
        answer = send_table(message, ts_plus_id_answer_links, kind_of_table="short")
        bot.send_message(message.chat.id, answer, reply_markup=key, parse_mode='Markdown',disable_web_page_preview=True) # disable_web_page_preview=True - это для того, чтоб сниппет не отправлялся
        log(message, send_table(message, ts_plus_id_answer_links, kind_of_table="short"))

    elif len(id_maybe_answer_links) > 1:
        namber_bort = 1
        key = make_battons(message, id_maybe_answer_links, status_searching, int(namber_bort))
        #id_maybe_answer_links = '\n-'.join(str(id_maybe_answer_links))  # тут все названи складываем через перевод на новую строку и вначале каждого названия ставим тире
        if status_searching == 'Ответа в файле нет.':
            answer = 'Извините, я еще не знаю этого глагола. Возможно вы искали(борт-' + str(namber_bort) + ':\n-' + str(id_maybe_answer_links) + '\n'
            answer_for_send = "Извините, я еще не знаю этого глагола. Возможно вы искали:"
        elif status_searching == 'Ответ в файле есть.':
            answer = 'Есть несколько подходящих ответов(борт-'+str(namber_bort)+':\n-' + str(id_maybe_answer_links) + '\n'
            answer_for_send = "Есть несколько подходящих ответов:"
        bot.send_message(message.chat.id, text=answer_for_send, reply_markup=key)
        log(message, answer)

    else: # если нет ответов совсем
        from alphabet_detector import AlphabetDetector #библеотека опрелеяет тип букв. Мне нужны иврит и кириллица
        ad = AlphabetDetector()
        if ad.is_cyrillic(message.text) == False and ad.is_hebrew(message.text) == False:
            answer = 'Извините, я еще не знаю глагола "*' + message.text+'*".\nВозможно вы ввели текст на неизвестном мне языке.\nЯ понимаю Русский и עברית. Попробуй снова.'
            bot.send_message(message.chat.id, answer, parse_mode='Markdown')
            log(message, answer)
        else:
            answer = 'Извините, я еще не знаю глагола "*'+message.text+'*"\n_Если Вы считаете, что он важен, отправь этот глагол моему переводчику. И он внесет его в базу знаний._'
            key = telebot.types.InlineKeyboardMarkup()
            but = telebot.types.InlineKeyboardButton(text='Отправить глагол.',callback_data='88888888')
            key.add(but)
            bot.send_message(message.chat.id, answer, parse_mode='Markdown', reply_markup=key)
            log(message, answer)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print("...................................СЕЙЧАС МЫ В callback_inline")
    print("call.message.message_id -", call.message.message_id)
    print("call.data -",call.data)
    if call.message: # на это нужно обратить внимание. call.message указывает на нажатую кнопку из чата с ботом а не инлайн (из другого чата)
        #bot.answer_callback_query(call.id, text="нажал...") # "эта фишка выводит на экран сообщение о том, что кнопка нажата. но не скрывает(((
        if call.data == '88888888':
            print(" --------- \n Нажата кнопка с id:", call.data)
            new_verb=call.message.json.get('text')[call.message.json.get('entities')[0].get('offset'):call.message.json.get('entities')[0].get('offset')+call.message.json.get('entities')[0].get('length')]
            text_after_button='Я запомнил "*'+new_verb+'*" и если такой глагол существует, я внесу в мой словарь в ближайшие дни.'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_after_button,parse_mode='Markdown')
            print("Нужно найти этот глагол-",new_verb)
            # !!!!тут обязательно нужна функция - уведомить меня.
            # !!!!тут обязательно нужна функция - уведомить меня.
        elif 'id_botr' in call.data:
            call_data = call.data.split("-") #изначальнов кнопку вложили данные в формате id_botr-123456-test-123456. Поэтому сплитовали через тире и получили 4 объекта
            namber_id_botr = call_data[1]
            namber_id_sms_for_find = call_data[3]
            print("это новый namber_id_botr", namber_id_botr)
            print("это новый namber_id_sms_for_find", namber_id_sms_for_find)
            file = open("many_battons.json", "r")
            all_story_buttons = json.load(file)
            print("ЭТО all_story_buttons!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! - ",all_story_buttons)
            for request in all_story_buttons: # тут будем искать нужный нам словарь с даными о собранных ответах в джейсоне
                if str(request["message.message_id"]) == str(namber_id_sms_for_find):
                    print("Н-А-Ш-Л-И .............................................................")
                    print(str(request["message.message_id"]))
                    print(str(request["info_buttons"]["status_searching"]))
                    print(str(request["info_buttons"]["namber_bort"]))
                    print(str(request["info_buttons"]["id_maybe_answer_links"]))
                    mmid1 = str(request["message.message_id"])
                    status_searching = str(request["info_buttons"]["status_searching"])
                    id_maybe_answer_links = request["info_buttons"]["id_maybe_answer_links"]
                    #key = make_battons(call.message, a_links, id_a_links, inf_a_links, idnk, int(namber_id_botr))
                    key = make_battons(call.message, id_maybe_answer_links, status_searching,
                                       int(namber_id_botr))  # убрать  - a_links -  и - a_links -

                    continue
                #else: !!!!!! нужно решить, что если не найдет запрос...

            # --------------------- ВЫШЕ ПРОБУЮ ДОСТАТЬ ДАННЫЕ ИЗ ДЖЕЙСОН-----
            #a_links=[]
            #id_a_links=[]
            #inf_a_links=[]

            #links_for_answer = '\n-'.join(id_maybe_answer_links)  # тут все названи складываем через перевод на новую строку и вначале каждого названия ставим тире (всременно это id-шники)
            if status_searching == 'Ответ в файле есть.':
                answer = 'Есть несколько подходящих ответов (борт-'+namber_id_botr+':\n-' + str(id_maybe_answer_links) + '\n'
                answer_for_send = "Есть несколько подходящих ответов:"
            else:
                answer_for_send = "Извините, я еще не знаю этого глагола. Возможно вы искали:"
                answer = 'Извините, я еще не знаю этого глагола. Возможно вы искали(борт-' + namber_id_botr + ':\n-' + str(id_maybe_answer_links) + '\n'

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=answer_for_send,
                                  reply_markup=key)
            log(call.message, answer)
            #https://web.telegram.org/#/im?p=@ivrit_support_bot
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо. Я проверю.")
            #bot.send_message(chat_id=call.message.chat.id, text="Спасибо. Я проверю.")
        elif "py_hy" in call.data:
            print("есть в кнопке data_but_py_hy-", call.data)
            call_data = call.data.split("-")  # изначальнов кнопку вложили данные в формате id_botr-123456-test-123456. Поэтому сплитовали через тире и получили 4 объекта
            #ts_and_id = call_data[1]
            id_py_hy = call_data[1]
            #id_py_hy = str(call.data[6:])
            #row = int(id_py_hy[:-2])#+int(constants1.table_start)
            print(id_py_hy)
            row = id_py_hy
            print(row)
            answer = send_table(call.message, row, kind_of_table="long+pyal_hyfal")
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=answer,
                                  parse_mode='Markdown',
                                  disable_web_page_preview=True)
            log(call.message, answer)
            #data_but_py_hy = str("py_hy-" + "1000pr")
        elif 'id_imper' in call.data:
            print("есть в кнопке id_imper-", call.data)
            ts_and_id = str(call.data[8:])
            row = int(ts_and_id)
            print("взяли глагол из строки-", row)
            answer = send_table(call.message, row, kind_of_table="long")

            #make_batton_imper(message, ts_and_id)


            if str(list.row(int(ts_and_id))[179].value) != "": #тут проверяю, нужно ли мне снова присылкть кнопку пассива или нет.
                key = make_batton_imper(call.message, ts_and_id, add_buttons="passiva")
                print("key---------------------", key)
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=answer,
                                      reply_markup=key,
                                      parse_mode='Markdown',
                                      disable_web_page_preview=True)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=answer,
                                      parse_mode='Markdown',
                                      disable_web_page_preview=True)
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=answer,parse_mode='Markdown',reply_markup=key,disable_web_page_preview=True)
            log(call.message, answer)



        else:
            print("Нажали кнопку со словом")
#            words_verb = xlrd.open_workbook('./Pealim_FINAL.xlsx') # Открываем файл ексель из папки в которой находится программа
#            list = words_verb.sheet_by_index(0)  # открываем первый лист (индекс 0)
            ts = constants1.table_start
            ts_and_id = int(ts)+int(call.data)
            print("Отправляем глагол и строки (row_and_id) - ",ts_and_id)
            answer = send_table(call.message, ts_and_id, kind_of_table="short")
            #bot.send_message(call.message.chat.id, answer, parse_mode='Markdown')
            #log(call.message, answer)

            if str(list.row(int(ts_and_id))[179].value) != "":
                key = make_batton_imper(call.message, str(ts_and_id), add_buttons="all")
            else:
                key = make_batton_imper(call.message, str(ts_and_id), add_buttons="imper")

            #key = make_batton_imper(call.message, ts_and_id, add_buttons="all")
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=answer, reply_markup=key_imper,parse_mode='Markdown')
            bot.send_message(call.message.chat.id, text=answer, reply_markup=key, parse_mode='Markdown',disable_web_page_preview=True)
            log(call.message, answer)


"""
            for row in range(2, 4307):
                print("проверяю строку -",row )

                if int(call.data) == int(list.row(row)[2].value):
                    print("int(list.row(row)[2].value)-", int(list.row(row)[2].value))
                    #answer = "ответ верный"
                    answer=send_table(call.message, row, size="short")
                    bot.send_message(call.message.chat.id, answer, parse_mode='Markdown')
                    log(call.message, answer)
                    continue

"""


"""
# Эта функция по кнопке "фото" отправляет один файл рандомом из паки указанной на моем компе.
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'фото': # если сообщение = фото, делаем следующее
        directory = 'C:/Users/Irina/PycharmProjects/stepik/photo_bots' # указываем адрес папки с файлами
        all_files_in_directory=os.listdir(directory) #os берет названия файлов из папки. Нужно изучить работу этой функции
        random_file=random.choice(all_files_in_directory) # ранее, мы импортировали рандом функцию. random.choice выбирает один файл из папки.
        img = open(directory+'/'+random_file, 'rb') #тут склеиваем название адрес папки и название файла
        bot.send_photo(message.chat.id, img) # отправляем файл юзеру
        print(random_file)  # печатаем название отправленного файла
        img.close() # закрываем файл


# Эта функция по кнопке "фото" отправляет все фотографии из паки юзеру.
@bot.message_handler(content_types=['text']) 
def handle_text(message): 
    if message.text == 'фото': # если сообщение = фото, делаем следующее
        directory = 'C:/Users/Irina/PycharmProjects/stepik/photo_bots' # указываем адрес папки с файлами
        all_files_in_directory=os.listdir(directory) #os берет названия файлов из папки. Нужно изучить работу этой функции
        print(all_files_in_directory) # печатаем все названия файлов по указанной ссылке
        for file in all_files_in_directory: # дальше будем отправлять все фото из указанной паки
            img = open(directory+'/'+file, 'rb') #тут склеиваем название адрес папки и название файла
            #bot.send_chat_action (message.chat.id, 'upload_photo') # Я пока не поняла, что именно делает эта строчка
            bot.send_photo(message.chat.id, img) # отправляем каждый файл
            img.close() # закрываем каждый файл
"""



if __name__ == '__main__':
    #bot.polling(none_stop=False, interval=0, timeout=20)
    bot.polling(none_stop=True, interval=0) #Функция, которая обновляет постоянно информацю с сервера.