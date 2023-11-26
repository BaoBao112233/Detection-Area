import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "6670909737:AAH5PzKUWU65e2t2FzHqSGSkQHQF_TJ27Og" # Điều khiển bot để gửi tin nhắn
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="6727234923", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")