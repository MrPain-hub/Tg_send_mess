import requests


class ExceptionRequestsCode(Exception):
    """
    Принимает status_code
    """
    def __init__(self, code):
        data_code = {400: "Неверный id получателя",
                     401: "Неверный токен",
                     403: "Бот не может начать диалог первым"
                     }
        if code in data_code:
            self.text = f"{data_code[code]}"
        else:
            self.text = f"{code} неизвестная ошибка"

    def __str__(self):
        return f"\n-------ERROR-------\n" \
               f"Сообщение не отправлено\n" \
               f"{self.text}"


class RequestsBot:
    """
    Получить token -> @BotFather
    Узнать свой id -> @getmyid_bot
    """
    def __init__(self, token, recipient_id):
        self.token = token
        self.recipient_id = recipient_id
        self.url = f"https://api.telegram.org/bot{token}/"

    def send_text(self, text):
        req = requests.post(self.url+"sendMessage", data={'chat_id': self.recipient_id, 'text': text})
        code = req.status_code
        if code == 200:
            return True
        raise ExceptionRequestsCode(code)


if __name__ == "__main__":
    pass
