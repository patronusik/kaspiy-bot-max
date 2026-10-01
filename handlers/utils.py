import aiohttp
from config import CHANNEL_ID, MAX_BOT_TOKEN

async def is_user_subscribed(user_id: int) -> bool:
    """
    Проверяет, подписан ли пользователь на канал.
    Возвращает True, если подписан, и False, если нет.
    """
    url = f"https://platform-api2.max.ru/chats/{CHANNEL_ID}/members"
    headers = {
        "Authorization": MAX_BOT_TOKEN
    }
    params = {
        "user_ids": user_id
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as resp:
                if resp.status != 200:
                    print(f"Ошибка API проверки подписки: {resp.status}, {await resp.text()}")
                    return False
                
                data = await resp.json()
                members = data.get("members", [])
                
                # Если массив members не пустой — пользователь подписан
                return len(members) > 0
    except Exception as e:
        print(f"Ошибка при проверке подписки: {e}")
        return False
