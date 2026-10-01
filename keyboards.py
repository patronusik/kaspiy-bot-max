from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL, SITE_URL, FORM_URL

# --- ПРОВЕРКА ПОДПИСКИ ---
subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

# --- ГЛАВНОЕ МЕНЮ ---
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏛️ О клубе", callback_data="about")],
    [InlineKeyboardButton(text="📍 Адреса учреждения", callback_data="addresses")],
    [InlineKeyboardButton(text="💳 Платные услуги", url="https://kaspiy-ast.ru/roditelyam/")],
    [InlineKeyboardButton(text="🎖️ Меры поддержки СВО", callback_data="support_menu")],
    [InlineKeyboardButton(text="🏋️ Про ФОК", callback_data="about_fok")],
    [InlineKeyboardButton(text="📞 Справочная информация", callback_data="contacts")],
])

# --- МЕНЮ МЕР ПОДДЕРЖКИ ---
support_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏐 Волейбол сидя", callback_data="support_volleyball")],
    [InlineKeyboardButton(text="🎲 Нарды без границ", callback_data="support_backgammon")],
    [InlineKeyboardButton(text="🧘 Мягкий фитнес", callback_data="support_fitness")],
    [InlineKeyboardButton(text="🏓 Настольный теннис", callback_data="support_table_tennis")],
    [InlineKeyboardButton(text="🎯 Метание ножей", callback_data="support_knife_throwing")],
    [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")],
])

# --- КНОПКА "НАЗАД" ДЛЯ ПОДМЕНЮ ---
back_to_support_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к мерам поддержки", callback_data="support_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])
