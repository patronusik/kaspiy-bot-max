from config import TEXT_SUPPORT_MENU, SUPPORT_DATA
from keyboards import support_menu_kb, back_to_support_kb

def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        payload = cb.payload

        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (cb.user.get("user_id") if isinstance(cb.user, dict) else None)
        if user_id is None:
            user_id = getattr(cb, "user_id", None)

        if payload == "support_menu":
            await bot.send_message(user_id=user_id, text=TEXT_SUPPORT_MENU, reply_markup=support_menu_kb, format="markdown")

        elif payload.startswith("support_"):
            key = payload[8:]
            text = SUPPORT_DATA.get(key, "Информация скоро появится.")
            await bot.send_message(user_id=user_id, text=text, reply_markup=back_to_support_kb, format="markdown")
