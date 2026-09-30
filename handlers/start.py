python
from maxbot.types import Message
from config import TEXT_SUBSCRIBE, TEXT_WELCOME
from keyboards import subscribe_kb, main_menu_kb

def register(dp, bot):
    
    @dp.bot_started
    async def on_bot_started(update):
        """Проверка подписки при запуске"""
        await bot.send_message(
            chat_id=update.user.id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb
        )

    @dp.message()
    async def on_message(message: Message):
        """Если пользователь пишет что-то вручную — показываем подписку"""
        await bot.send_message(
            chat_id=message.sender.id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb
        )