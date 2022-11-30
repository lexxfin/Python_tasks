import telebot
from sympy import sympify
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)
ready = False
expr_1 = None
expr_2 = None


def parse_to_sympy(txt: str):
    result = txt.replace(' ', '').removesuffix('=0').replace('^', '**').lower()
    result = result.replace('x', '*x').replace('+*', '+').replace('-*', '-')
    if result.startswith('*x'):
        result = result.replace('*x', 'x', 1)
    return result


@bot.message_handler(commands=['start'])
def start(msg):
    gif = open('start_cat.mp4', 'rb')
    bot.send_animation(msg.chat.id, gif)
    txt = f'''✋Привет {msg.from_user.first_name})
    Я вроде как научился складывать многочлены. Давай попробуем?
    При вводе степени используй символ <b>"^"</b>.
    Например так <b>2x^2 + 4x + 5 = 0</b>'''
    bot.send_message(msg.chat.id, txt, parse_mode='html')
    bot.send_message(msg.chat.id, '1️⃣ Введи первый многочлен')


@bot.message_handler(content_types=['text'])
def answer(msg):
    if 'x' not in msg.text.lower():
        bot.reply_to(msg, '😬Что-то не похоже на многочлен')
    else:
        try:
            expr = sympify(parse_to_sympy(msg.text))
        except:
            bot.reply_to(msg, '😬Что-то не похоже на многочлен')

        global ready
        if not ready:
            # input 1 expr
            global expr_1
            expr_1 = sympify(parse_to_sympy(msg.text))
            bot.send_message(msg.chat.id, '2️⃣ Введи второй многочлен')
            ready = True
        else:
            # input 2 expr
            global expr_2
            expr_2 = sympify(parse_to_sympy(msg.text))
            # output result
            result = str(expr_1 + expr_2).replace('**', '^').replace('*', '') + ' = 0'
            bot.send_message(msg.chat.id, '1️⃣➕2️⃣️ Сумма многочленов равна')
            bot.send_message(msg.chat.id, result)
            ready = False
            bot.send_message(msg.chat.id, '1️⃣ Введи первый многочлен')


if __name__ == '__main__':
    print('Bot started')
    bot.polling(none_stop=True)
