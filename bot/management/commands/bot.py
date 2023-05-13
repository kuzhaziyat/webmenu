from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import types
import telebot


# Объявление переменной бота
bot = telebot.TeleBot("5603075576:AAFATIivcnb7hArq7LwbSsdUS9knjQINEnY")


# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
            keyboard = types.InlineKeyboardMarkup(row_width=1)  # создаем клавиатуру inline
            webApp = types.WebAppInfo("https://kyzyl.kannam.ru/")  # создаем webappinfo - формат хранения url
            VK = "https://vk.com/grandcafepaparazzi"  # создаем webappinfo - формат хранения url
            Insta = "https://instagram.com/paparazzi_kzl"  # создаем webappinfo - формат хранения url
            app = types.InlineKeyboardButton(text="🍱Заказать тут", web_app=webApp)  # создаем кнопку типа webapp
            vkButton = types.InlineKeyboardButton(text="Наша группа ВК", url=VK)
            instaButton = types.InlineKeyboardButton(text="Наша группа Instagramm", url=Insta)
            call = types.InlineKeyboardButton(text="📲Позвонить",callback_data="call")
            switch = types.InlineKeyboardButton(text='🙎Пригласить друга', switch_inline_query='[PaparazziGroup](https://paparazzikzl.ru/)')
            keyboard.add(app,vkButton,instaButton,call,switch)  # добавляем кнопку в клавиатуру
        
            return keyboard  # возвращаем клавиатуру

        def callKeyboard(): #создание клавиатуры с webapp кнопкой
            keyboard = types.InlineKeyboardMarkup(row_width=1)  # создаем клавиатуру inline
        
            back = types.InlineKeyboardButton(text="Назад",callback_data="main")
            call_pc = types.InlineKeyboardButton(text="Показать все номера(Для просмотра с компьютера)",callback_data="call_pc")
            call_kyzyl = types.InlineKeyboardButton(text="Кызыл",url="https://elcar.su/php/call.php?phone=89232682288")
            call_kyzyl2 = types.InlineKeyboardButton(text="Кызыл",url="https://elcar.su/php/call.php?phone=89232682288")
            call_kaa_hem = types.InlineKeyboardButton(text="Каа-Хем",url="https://elcar.su/php/call.php?phone=89233828877")
            call_vavil = types.InlineKeyboardButton(text="Вавилинский",url="https://elcar.su/php/call.php?phone=89235805588")
            call_sam = types.InlineKeyboardButton(text="Самовывоз из кафе/бронь столов",url="https://elcar.su/php/call.php?phone=89232787979")
            keyboard.add(call_kyzyl,call_kyzyl2,call_kaa_hem,call_vavil,call_sam,call_pc,back)  # добавляем кнопку в клавиатуру
        
            return keyboard  # возвращаем клавиатуру
        def viewcallKeyboard(): #создание клавиатуры с webapp кнопкой
            keyboard = types.InlineKeyboardMarkup(row_width=1)  # создаем клавиатуру inline
        
            main = types.InlineKeyboardButton(text="В главное меню",callback_data="main")
            back = types.InlineKeyboardButton(text="Назад",callback_data="call")
            keyboard.add(main,back)  # добавляем кнопку в клавиатуру
        
            return keyboard  # возвращаем клавиатуру
        
        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.message:
                if call.data == "call":
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text='{0.first_name}! Служба доставки принимает заказы с 10.00 до 23.30. Нажмите на кнопку чтобы сделать звонок(Для телефонов)\n'.format(call.message.chat),
                                          parse_mode="Markdown",
                                          reply_markup=callKeyboard())
                if call.data == "call_pc":
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text='{0.first_name}! Служба доставки принимает заказы с 10.00 до 23.30 по телефонам:\n\n📲Кызыл +79232682288 +79232661199'
                                               '\n\n📲Каа-Хем +79233828877\n\n📲Вавилинский +79235805588\n\n📲Самовывоз из кафе/бронь столов +79232787979'.format(call.message.chat),
                                          parse_mode="Markdown",
                                          reply_markup=viewcallKeyboard())
                if call.data == "main":
                    bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=call.message.message_id,
                                          text='Привет, {0.first_name}! Я бот для заказа доставки еды из [PaparazziGroup](https://paparazzikzl.ru/).'.format(call.message.chat),
                                          parse_mode="Markdown",
                                          reply_markup=webAppKeyboard())
        
        @bot.message_handler(commands=['start']) #обрабатываем команду старт
        def start_fun(message):
           bot.send_message( message.chat.id, 'Привет, {0.first_name}! Я бот для заказа доставки еды из [PaparazziGroup](https://paparazzikzl.ru/).'.format(message.from_user),
                             parse_mode="Markdown",
                             reply_markup=webAppKeyboard()) #отправляем сообщение с нужной клавиатурой

        bot.infinity_polling()				