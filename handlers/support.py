from config import TEXT_SUPPORT_MENU, SUPPORT_DATA
from keyboards import support_menu_kb, back_to_support_kb

def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        payload = cb.payload
        user_id = cb.user.id

        # --- МЕНЮ МЕР ПОДДЕРЖКИ ---
        if payload == "support_menu":
            await bot.send_message(
                chat_id=user_id,
                text=TEXT_SUPPORT_MENU,
                reply_markup=support_menu_kb
            )

        # --- КОНКРЕТНАЯ МЕРА ПОДДЕРЖКИ ---
        elif payload.startswith("support_"):
            key = payload[8:]  # убираем "support_"
            text = SUPPORT_DATA.get(key, "Информация скоро появится.")
            await bot.send_message(
                chat_id=user_id,
                text=text,
                reply_markup=back_to_support_kb
            )