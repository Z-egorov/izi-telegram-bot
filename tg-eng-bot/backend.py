# This Python file uses the following encoding: utf-8
import telebot
import sqlite3
from telebot import types
import time
import config

bot = telebot.TeleBot(config.Token)

connect = sqlite3.connect('tasks.db')
cursor = connect.cursor()

cursor.execute("SELECT * FROM Tasks")
all_tasks = cursor.fetchall()
# print(all_tasks)
kol = 0

@bot.message_handler(commands=['start'])
def starting(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}, я - {1.first_name}, твой помощник по английскому языку! Выбирай скорее время и погнали! ".format(message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id, """ Ты можешь написать словами или командой!
    1) Простое настоящее - Present Simple (Команда: /present_simple)
    2) Простое прошедшее - Past Simple (Команда: /past_simple)
    3) Простое будущее - Future Simple (Команда: /future_simple)
    4) Настоящее продолженное - Present Continious (Команда: /present_continious)
    5) Настоящее совершенное -  Present Perfect (Команда: /present_perfect)
    """, parse_mode='html')

@bot.message_handler(commands=['present_simple'])
def present_simple(message):
    bot.send_message(message.chat.id, "Present Simple? Отличный выбор!)", parse_mode='html')
    time.sleep(2)
    bot.send_message(message.chat.id, "Мы используем Present Simple когда нам надо сказать о постоянном, повторяющемся действии, а также общеизвестные факты. Например, ты делишься с друзьями своим расписанием или привычкой: I often go to sport club.", parse_mode='html')
    time.sleep(5)
    bot.send_message(message.chat.id, "Слова подсказки: always - всегда,\n usually - обычно,\n often - часто,\n sometimes - иногда,\n never - никогда,\n seldom - редко.\n Например: Dan is always late.\n Susan sometimes wathches movies.", parse_mode='html')
    time.sleep(5)
    bot.send_message(message.chat.id, "Как образовать Present Simple? Легко! Мы добавляем 'S' к глаголу с 'He', 'She', 'it'. She cooks dinner. He eats meet.", parse_mode='html')
    time.sleep(5)
    bot.send_message(message.chat.id, "А что если нам надо сказать отрицание? На помощь всегда приходит вспомогательный глагол. с 'He' 'She' 'it' - Does + not. С 'I' 'We' 'You' 'They' - Do + not ", parse_mode='html')
    time.sleep(5)
    bot.send_message(message.chat.id, "А как же вопросительные предложения!? Для вопросительных предложений тут нам опять поможет вспомогательный глагол. с 'He' 'She' 'it' - Does. С 'I' 'We' 'You' 'They' - Do. Если вопрос общий, то просто ставим нужный нам глагол в начало!", parse_mode='html')
    time.sleep(5)
    global kol
    kol = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Давай!")
    No = types.KeyboardButton("Не хочу, но надо!")
    markup.add(Yes, No)
    m = bot.send_message(message.chat.id, "Ну что, потренируемся?)", reply_markup = markup)
    

     

    def present_simple_question(message):
        global m
        global markup
        markup = types.ReplyKeyboardRemove() 
        if message.text == "Давай!" or message.text == "Не хочу, но надо!":
            bot.send_message(message.chat.id, "Выбери номер правильного по твоему мнению ответа и напиши!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[0][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_first_task)
            
    def present_simple_first_task(message):
        global kol
        global m
        if message.text == str(all_tasks[0][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[1][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_second_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[1][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_second_task)
    
    def present_simple_second_task(message):
        global kol
        global m
        if message.text == str(all_tasks[1][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[2][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_third_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[2][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_third_task)
    
    def present_simple_third_task(message):
        global kol
        global m
        if message.text == str(all_tasks[2][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[3][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_fourth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[3][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_fourth_task)
    
    def present_simple_fourth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[3][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[4][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_fifth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[4][0], parse_mode='html')
            bot.register_next_step_handler(m, present_simple_fifth_task)
    
    def present_simple_fifth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[4][1]):
            kol += 1
            m = bot.send_message(message.chat.id, "Правильно, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
        else:
            m = bot.send_message(message.chat.id, "Неправильно(, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
    
    def result(message):
        global kol
        if kol < 3:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Не расстраивайся, перечитай теорию и повтори тест!)", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Молодец, ты хорошо справился! Можешь приступать к следующей теме!", parse_mode = 'html')


    bot.register_next_step_handler(m, present_simple_question)
    

################################## PAST SIMPLE

@bot.message_handler(commands=['past_simple'])
def past_simple(message): 
    bot.send_message(message.chat.id,"Past Simple? Это изи :)")
    time.sleep(2)
    bot.send_message(message.chat.id,"Past Simple используется тогда, когда мы хотим сказать о действии в прошлом. Важно понимать, что действие было в прошлом, или мы перечисляем действия в прошлом!")
    time.sleep(3)
    bot.send_message(message.chat.id,"I saw Mike in the cafe / я видел Майка в кафе. He had a shower, had breakfast and went to school / он принял душ, позавтракал и пошел в школу.")
    time.sleep(3)
    bot.send_message(message.chat.id,"'Изи, а есть слова напоминалки?' - конечно! Yesterday - вчера; Last week, month, Monday - на прошлой неделе, месяце, в прошлый понедельник.")
    time.sleep(3)
    bot.send_message(message.chat.id,"Как образуется Past Simple? С He, She, it, We, You, They - используем II форму неправильного глагола, а если глагол правильный, то добавляем окончание -ed!")
    time.sleep(3)
    bot.send_message(message.chat.id,"Что делать в отрицании? Берем вспомогательный глагол 'did', добавляем отрицание 'not', после этого нужно обязательно поставить смысловой глагол в первую форму. Например: I didn't watch TV yesterday / я не смотрел телевизор вчера.")
    time.sleep(4)
    bot.send_message(message.chat.id,"Для вопросительных предложений в Past Simple используем уже известный вспомогательный глагол 'did' и первую форму смыслового глагола. Главное поставить слова в нужном порядке. Запоминай! Did she eat ice-cream yesterday? / Она ела мороженное вчера? Did he start his work? / Он начал работу?")
    time.sleep(5)
    global kol
    kol = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Давай!")
    No = types.KeyboardButton("Не хочу, но надо!")
    markup.add(Yes, No)
    m = bot.send_message(message.chat.id, "Ну что, потренируемся?)", reply_markup = markup)
    

    def past_simple_question(message):
        global m
        global markup
        markup = types.ReplyKeyboardRemove() 
        if message.text == "Давай!" or message.text == "Не хочу, но надо!":
            bot.send_message(message.chat.id, "Выбери номер правильного по твоему мнению ответа и напиши!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[10][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_first_task)

    def past_simple_first_task(message):
        global kol
        global m
        if message.text == str(all_tasks[10][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[11][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_second_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[11][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_second_task)
    
    def past_simple_second_task(message):
        global kol
        global m
        if message.text == str(all_tasks[11][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[12][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_third_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[12][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_third_task)
    
    def past_simple_third_task(message):
        global kol
        global m
        if message.text == str(all_tasks[12][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[13][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_fourth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[13][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_fourth_task)
    
    def past_simple_fourth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[13][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[14][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_fifth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[14][0], parse_mode='html')
            bot.register_next_step_handler(m, past_simple_fifth_task)
    
    def past_simple_fifth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[14][1]):
            kol += 1
            m = bot.send_message(message.chat.id, "Правильно, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
        else:
            m = bot.send_message(message.chat.id, "Неправильно(, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
    
    def result(message):
        global kol
        if kol < 3:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Не расстраивайся, перечитай теорию и повтори тест!)", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Молодец, ты хорошо справился! Можешь приступать к следующей теме!", parse_mode = 'html')

    bot.register_next_step_handler(m, past_simple_question)

################################## FUTURE SIMPLE

@bot.message_handler(commands=['future_simple'])
def future_simple(message: types.Message):
    bot.send_message(message.chat.id,"Просто будущее время - Future Simple!")
    time.sleep(2)
    bot.send_message(message.chat.id,"Мы используем его для описания события и действий, которые совершаются в неопределенном или отдаленным будущем! (А еще, если ты вот прям сию минутку решил куда-то пойти) I will send a postcart tomorrow)")
    time.sleep(3)
    bot.send_message(message.chat.id,"Образовать это время на изи) Со всеми местоимениями используется вспомогательный глагол will + смысловой глагол! I will go / He will go. Реально изи!")
    time.sleep(3)
    bot.send_message(message.chat.id,"Слова подсказки: tomorrow, next year, month, week / завтра, в следующем году, месяце, на следующей неделе")
    time.sleep(3)
    bot.send_message(message.chat.id,"Вопросы? Тоже очень легко! Берем will, ставим на первое место в предложении и вауля, ты уже спрашиваешь о том, кто и что будет выполнять в будущем! Will they cook next week? Wil you travel to Spain? ")
    global kol
    kol = 0
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Давай!")
    No = types.KeyboardButton("Не хочу, но надо!")
    markup.add(Yes, No)
    m = bot.send_message(message.chat.id, "Ну что, потренируемся?)", reply_markup = markup)
    

    def future_simple_question(message):
        global m
        global markup
        markup = types.ReplyKeyboardRemove() 
        if message.text == "Давай!" or message.text == "Не хочу, но надо!":
            bot.send_message(message.chat.id, "Выбери номер правильного по твоему мнению ответа и напиши!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[15][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_first_task)

    def future_simple_first_task(message):
        global kol
        global m
        if message.text == str(all_tasks[15][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[16][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_second_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[16][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_second_task)
    
    def future_simple_second_task(message):
        global kol
        global m
        if message.text == str(all_tasks[16][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[17][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_third_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[17][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_third_task)
    
    def future_simple_third_task(message):
        global kol
        global m
        if message.text == str(all_tasks[17][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[18][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_fourth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[18][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_fourth_task)
    
    def future_simple_fourth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[18][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[19][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_fifth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[19][0], parse_mode='html')
            bot.register_next_step_handler(m, future_simple_fifth_task)
    
    def future_simple_fifth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[19][1]):
            kol += 1
            m = bot.send_message(message.chat.id, "Правильно, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
        else:
            m = bot.send_message(message.chat.id, "Неправильно(, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
    
    def result(message):
        global kol
        if kol < 3:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Не расстраивайся, перечитай теорию и повтори тест!)", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Молодец, ты хорошо справился! Можешь приступать к следующей теме!", parse_mode = 'html')

    bot.register_next_step_handler(m, future_simple_question)
    
################################## PRESENT CONTINIOUS

@bot.message_handler(commands=['present_continious'])
def present_continious(message: types.Message):
    bot.send_message(message.chat.id, "Настоящее продолженное время - Present Continious!")
    time.sleep(1)
    bot.send_message(message.chat.id, "Это время мы используем, когда говорим о событиях, которые происходят сейчас, в момент речи!")
    time.sleep(2)
    bot.send_message(message.chat.id, "Слова-подсказки: now - сейчас; at the moment - на данный момент; today - сегодня; Look - посмтори; Listen - послушай. I am playing now / я сейчас играю.")
    time.sleep(3)
    bot.send_message(message.chat.id,"Образуется Present Continious при помощи глагола 'to be' и добавляем к смысловому глаголу окончание '-ing'. НО! Глагол 'to be' изменяется в зависимости от местоимения: c I используем am + ing; с He, She, it - is + ing; с we, you, the - are + ing.")
    time.sleep(6)
    bot.send_message(message.chat.id, "В отрицании добавляем not к глаголу to be и не забываем -ing. I am not reading a book now / я не читаю книгу сейчас; He is not reading a book now / он не читает книгу сейчас; They are not reading books now / они не читают книги сейчас.")
    time.sleep(3)
    bot.send_message(message.chat.id, "Чуть не забыл про вопрос! Чтобы задать вопрос, мы выносим вспомогательный глагол на первое место, потом подлежащее и смысловой глагол!")
    global kol
    kol = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Давай!")
    No = types.KeyboardButton("Не хочу, но надо!")
    markup.add(Yes, No)
    m = bot.send_message(message.chat.id, "Ну что, потренируемся?)", reply_markup = markup)
    

    def present_continious_question(message):
        global m
        global markup
        markup = types.ReplyKeyboardRemove() 
        if message.text == "Давай!" or message.text == "Не хочу, но надо!":
            bot.send_message(message.chat.id, "Выбери номер правильного по твоему мнению ответа и напиши!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[20][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_first_task)

    def present_continious_first_task(message):
        global kol
        global m
        if message.text == str(all_tasks[20][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[21][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_second_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[21][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_second_task)
    
    def present_continious_second_task(message):
        global kol
        global m
        if message.text == str(all_tasks[21][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[22][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_third_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[22][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_third_task)
    
    def present_continious_third_task(message):
        global kol
        global m
        if message.text == str(all_tasks[22][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[23][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_fourth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[23][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_fourth_task)
    
    def present_continious_fourth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[23][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[24][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_fifth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[24][0], parse_mode='html')
            bot.register_next_step_handler(m, present_continious_fifth_task)
    
    def present_continious_fifth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[24][1]):
            kol += 1
            m = bot.send_message(message.chat.id, "Правильно, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
        else:
            m = bot.send_message(message.chat.id, "Неправильно(, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
    
    def result(message):
        global kol
        if kol < 3:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Не расстраивайся, перечитай теорию и повтори тест!)", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Молодец, ты хорошо справился! Можешь приступать к следующей теме!", parse_mode = 'html')

    bot.register_next_step_handler(m, present_continious_question)


################################## PRESENT PERFECT

@bot.message_handler(commands=['present_perfect'])
def present_perfect(message: types.Message):
    bot.send_message(message.chat.id, "Present Perfect? Сейчас расскажу!")
    time.sleep(1)
    bot.send_message(message.chat.id, "Смотри, Мы используем Present Perfect когда нам надо рассказать о действии, которое началось в прошлом и продолжается до сих пор. (Они живут в этом доме с декабря прошлого года.)")
    time.sleep(2)
    bot.send_message(message.chat.id, "а еще, в present perfect мы рассказываем о действии, которое имеет видимый результат в настоящем. (Она сдала экзамены.)")
    time.sleep(3)
    bot.send_message(message.chat.id,"Слова - подсказки: ever - всегда , never - никогда , just - только что, already - уже , yet - всё еще , since - с тех пор , for - на протяжении")
    time.sleep(6)
    bot.send_message(message.chat.id, "Как построить Present Perfect? Довольно просто, но есть одна проблемка, если не знаешь третью форму неправильных глаголов, то это время тебе не победить! Строим предложения так: глагол Have с местоимениями I/we/you/they и 3я форма глагола.  We have done our homework.   Глагол Has с местоимениями He/she/it и 3я форма глагола. He has been in Rome for a week.")
    time.sleep(3)
    bot.send_message(message.chat.id, "В отрицании добавляем Not к Have/has и получаем, We haven't done our project. He hasn't been in Rome for a week.")
    time.sleep(3)
    bot.send_message(message.chat.id, "Но как же задать вопрос с этим временем? Легко! Забираем Have или has в начало вопроса и спрашиваем: Has he arrived yet? Have they done their project?")
    global kol
    kol = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Yes = types.KeyboardButton("Давай!")
    No = types.KeyboardButton("Не хочу, но надо!")
    markup.add(Yes, No)
    m = bot.send_message(message.chat.id, "Ну что, потренируемся?)", reply_markup = markup)

    """ПЕРЕПИСАТЬ НАЗВАНИЯЯ""" # СДЕЛАЛ!!

    def present_perfect_question(message):
        global m
        global markup
        markup = types.ReplyKeyboardRemove() 
        if message.text == "Давай!" or message.text == "Не хочу, но надо!":
            bot.send_message(message.chat.id, "Выбери номер правильного по твоему мнению ответа и напиши!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[25][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_first_task)

    def present_perfect_first_task(message):
        global kol
        global m
        if message.text == str(all_tasks[25][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[26][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_second_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[26][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_second_task)
    
    def present_perfect_second_task(message):
        global kol
        global m
        if message.text == str(all_tasks[26][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[27][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_third_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[27][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_third_task)
    
    def present_perfect_third_task(message):
        global kol
        global m
        if message.text == str(all_tasks[27][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[28][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_fourth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[28][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_fourth_task)
    
    def present_perfect_fourth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[28][1]):
            kol += 1
            bot.send_message(message.chat.id, "Правильно, идем дальше!", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[29][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_fifth_task)
        else:
            bot.send_message(message.chat.id, "Неправильно(", parse_mode='html')
            time.sleep(2)
            m = bot.send_message(message.chat.id, all_tasks[29][0], parse_mode='html')
            bot.register_next_step_handler(m, present_perfect_fifth_task)
    
    def present_perfect_fifth_task(message):
        global kol
        global m
        if message.text == str(all_tasks[29][1]):
            kol += 1
            m = bot.send_message(message.chat.id, "Правильно, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
        else:
            m = bot.send_message(message.chat.id, "Неправильно(, на этом всё, подведем итоги)", parse_mode='html')
            time.sleep(2)
            result(message)
    
    def result(message):
        global kol
        if kol < 3:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Не расстраивайся, перечитай теорию и повтори тест!)", parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Ты ответил на {kol} из 5. Молодец, ты хорошо справился! Можешь приступать к следующей теме!", parse_mode = 'html')

    bot.register_next_step_handler(m, present_perfect_question)

################################## OTHER

@bot.message_handler(content_types=['text'])
def react(message):
    if message.chat.type == 'private':
        if message.text.lower() == "present simple":
            present_simple(message)
        if message.text.lower() == "past simple":
            past_simple(message)
        if message.text.lower() == "future simple":
            future_simple(message)
        if message.text.lower() == "present_continious":
            present_continious(message)
        if message.text.lower() == "present perfect":
            present_perfect(message)
        else:
            bot.send_message(message.chat.id, "Не понимаю ((", parse_mode='html')

bot.polling(none_stop=True)
