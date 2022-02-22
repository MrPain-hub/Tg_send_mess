En/Ru

Tg_send_mess - Class for sending messages to telegram./\
Класс для отправки сообщений в telegram.

Language: Python 3.6+ OS: Windows

    The class uses the requests module, you can install it by entering the command: pip install requests.
    Класс использует модуль requests, для установки введите команду pip install requests.
    
    
To get a token, you need to create a bot in telegram using @BotFather/\
Чтобы получить токен, нужно создать бота в telegram с помощью @BotFather

        Get my token -> @BotFather

To get your id, you need to write to the bot in the telegram @getmyid_bot/\
Чтобы получить свой id, нужно написать боту в telegram @getmyid_bot

        Find out your ID -> @getmyid_bot

The class sends a message to the user or to the chat, which makes it possible to notify about the completion of the script execution in telegram./\
Класс отправляет сообщение пользователю или в чат, что дает возможность оповестить о завершении выполнения py скрипта в telegram.

Пример:
        
        bot = RequestsBot(token=token, recipient_id=user_id)
        bot.send_text("❤️")     # метод отправки сообщения
        
