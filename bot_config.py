from aiogram import Dispatcher, Bot
from decouple import config

token = config('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)


admins = [5747517813,]