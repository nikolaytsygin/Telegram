#Импортируем Telegram API
import telegram
#Импортируем класс Bot
from telegram import Bot
#Импортирвуем класс Updater
from telegram.ext import Updater, Filters, MessageHandler

# импортируем файл с токенном
import config


# Объявляем бота и импортируемый токен
bot = Bot(config.TOKEN)
updater = Updater(config.TOKEN)

# Укажите id своего аккаунта в Telegram
chat_id = 73879154
text = 'Вам телеграмма!'
# Отправка сообщения при запуске бота
bot.send_message(chat_id, text)

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')

# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle()
