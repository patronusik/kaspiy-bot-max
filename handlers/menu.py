from config import (
    TEXT_WELCOME, TEXT_ABOUT, TEXT_ADDRESSES, TEXT_PAID_SERVICES,
    TEXT_ABOUT_FOK, TEXT_CONTACTS, SITE_URL
)
from keyboards import main_menu_kb, back_to_menu_kb, check_sub_kb
from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.start import is_user_subscribed  # ← импорт функции проверки

def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        print(f"CALLBACK: payload={cb.payload} user={getattr(cb, 'user', None)}")

        # Пытаемся получить user_id разными способами — зависит от версии umaxbot
        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (cb.user.get("user_id") if isinstance(cb.user, dict) else None)
        if user_id is None:
            user_id = getattr(cb, "user_id", None)

        print(f"CALLBACK: resolved user_id={user_id}")

        payload = cb.payload

        if payload == "check_sub":
            # Делаем реальную проверку подписки
            subscribed = await is_user_subscribed(user_id)
            
            if subscribed:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_WELCOME,
                    reply_markup=main_menu_kb,
                    format="markdown"
                )
            else:
                await bot.send_message(
                    user_id=user_id,
                    text="❌ Ты ещё не подписался на канал. Подпишись и нажми кнопку «Я подписался» ещё раз.",
                    reply_markup=check_sub_kb
                )

        elif payload == "about":
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🌐 Перейти на сайт", url=SITE_URL)],
                [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
            ])
            await bot.send_message(user_id=user_id, text=TEXT_ABOUT, reply_markup=kb)

        elif payload == "addresses":
            await bot.send_message(user_id=user_id, text=TEXT_ADDRESSES, reply_markup=back_to_menu_kb)

        elif payload == "paid_services":
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🌐 Перейти на сайт", url=SITE_URL)],
                [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
            ])
            await bot.send_message(user_id=user_id, text=TEXT_PAID_SERVICES, reply_markup=kb)

        elif payload == "about_fok":
            await bot.send_message(user_id=user_id, text=TEXT_ABOUT_FOK, reply_markup=back_to_menu_kb)

        elif payload == "contacts":
            await bot.send_message(user_id=user_id, text=TEXT_CONTACTS, reply_markup=back_to_menu_kb)

        elif payload == "back_to_menu":
            await bot.send_message(user_id=user_id, text=TEXT_WELCOME, reply_markup=main_menu_kb)
