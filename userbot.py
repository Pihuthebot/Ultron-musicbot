# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> Uɭtʀoŋ Usɘʀɓot Stʌʀtɘɗ')
idle()
app.stop()
print('\n>>> Uɭtʀoŋ Usɘʀɓot Stoppɘɗ')
