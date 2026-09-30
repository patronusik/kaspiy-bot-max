import asyncio
from maxbot.bot import Bot
from maxbot.dispatcher import Dispatcher
from config import BOT_TOKEN

from handlers import start, menu, support

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрируем обработчики из модулей
start.register(dp, bot)
menu.register(dp, bot)
support.register(dp, bot)

if __name__ == "__main__":
    asyncio.run(dp.run_polling())