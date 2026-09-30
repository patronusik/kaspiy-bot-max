from config import (
    TEXT_WELCOME, TEXT_ABOUT, TEXT_ADDRESSES, TEXT_PAID_SERVICES,
    TEXT_ABOUT_FOK, TEXT_CONTACTS, SITE_URL
)
from keyboards import (
    main_menu_kb, back_to_menu_kb
)
from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        payload = cb.payload
        user_id = cb.user.id

        # --- ПРОВЕРКА ПОДПИСКИ ---
        if payload == "check_sub":
            await bot.send_message(
                chat_id=user_id,
                text=TEXT_WELCOME,
                reply_markup=main_menu_kb
            )

        # --- О КЛУБЕ ---
        elif payload == "about":
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🌐 Перейти на сайт", url=SITE_URL)],
                [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
            ])
            await bot.send_message(chat_id=user_id, text=TEXT_ABOUT, reply_markup=kb)

        # --- АДРЕСА ---
        elif payload == "addresses":
            await bot.send_message(chat_id=user_id, text=TEXT_ADDRESSES, reply_markup=back_to_menu_kb)

        # --- ПЛАТНЫЕ УСЛУГИ ---
        elif payload == "paid_services":
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🌐 Перейти на сайт", url=SITE_URL)],
                [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
            ])
            await bot.send_message(chat_id=user_id, text=TEXT_PAID_SERVICES, reply_markup=kb)

        # --- ПРО ФОК ---
        elif payload == "about_fok":
            await bot.send_message(chat_id=user_id, text=TEXT_ABOUT_FOK, reply_markup=back_to_menu_kb)

        # --- СПРАВОЧНАЯ ИНФОРМАЦИЯ ---
        elif payload == "contacts":
            await bot.send_message(chat_id=user_id, text=TEXT_CONTACTS, reply_markup=back_to_menu_kb)

        # --- НАЗАД В МЕНЮ ---
        elif payload == "back_to_menu":
            await bot.send_message(
                chat_id=user_id,
                text=TEXT_WELCOME,
                reply_markup=main_menu_kb
            )