from maxbot.types import Message
from config import TEXT_SUBSCRIBE, TEXT_WELCOME
from keyboards import subscribe_kb, main_menu_kb

def register(dp, bot):

    @dp.bot_started
    async def on_bot_started(update):
        """Срабатывает при нажатии кнопки 'Начать' в MAX"""
        # В рабочем коде использовался update['user']['user_id'] — оставляем так
        user_id = update['user']['user_id']
        print(f"BOT_STARTED: user_id={user_id}")
        await bot.send_message(
            user_id=user_id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb
        )

    @dp.message()
    async def on_message(message: Message):
        """Срабатывает на любое текстовое сообщение"""
        print(f"MESSAGE: text={getattr(message, 'text', None)} sender={message.sender.id}")
        await bot.send_message(
            user_id=message.sender.id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb
        )
