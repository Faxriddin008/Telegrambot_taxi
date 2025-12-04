
# # config.py

# import os
# import logging

# # BOT TOKEN'ni Render Environment Variables'dan o'qish
# BOT_TOKEN = os.environ.get("8512718256:AAGGcXzuf1BLLSYKnhEPbxpTMdlNeWXUQbA") 

# # Operator ID'larini stringdan int ro'yxatiga o'tkazish
# op_ids_str = os.environ.get("OPERATOR_IDS", "")
# try:
#     # Virgullar bilan ajratilgan stringni int ro'yxatiga aylantiramiz
#     OPERATOR_IDS = [int(i.strip()) for i in op_ids_str.split(',') if i.strip().isdigit()]
# except Exception as e:
#     logging.error(f"OPERATOR_IDS'ni o'qishda xato: {e}. Ro'yxat bo'sh qoladi.")
#     OPERATOR_IDS = [
#     5617184769,  # Operator 1 ID'si
#     7394345210   # Operator 2 ID'si
# ]

# # --- PostgreSQL ma'lumotlari (Render'dagi tashqi DB bo'lsa) ---
# # DB_HOST, DB_USER, DB_PASSWORD, DB_NAME Render Environment Variables orqali o'qilishi kerak
# DB_HOST = os.environ.get("dpg-d4mq93hr0fns73adstig-a")
# DB_USER = os.environ.get("telegram_bot_nc61_user")
# DB_PASSWORD = os.environ.get("3AzjnFQbCT9YWkC5yauXnBQiETAo4YcK")
# DB_NAME = os.environ.get("telegrambot_taxi")
# DB_PORT = os.environ.get("5432") # Agar port alohida bo'lsa

# # Ishga tushirishdan oldin TOKEN mavjudligini tekshirish
# if not BOT_TOKEN:
#     raise ValueError("❌ BOT_TOKEN muhit o'zgaruvchilari orasida topilmadi!")

# # Agar boshqa maxfiy sozlamalar bo'lsa, ularni ham shu tarzda qo'shing.


import os

    # Telegram bot tokenini Railway Environment Variables dan olish
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # Operator ID'larini olish
    OPERATOR_IDS = [int(i.strip()) for i in os.environ.get("OPERATOR_IDS", "").split(',') if i.strip()]

    # Railway tomonidan avtomatik yaratilgan PostgreSQL o'zgaruvchilaridan foydalanish
    DB_HOST = os.environ.get("PGHOST")
    DB_USER = os.environ.get("PGUSER")
    DB_PASSWORD = os.environ.get("PGPASSWORD") # DB_PASS o'rniga DB_PASSWORD/PGPASSWORD ishlatish muhim
    DB_NAME = os.environ.get("PGDATABASE")
    DB_PORT = os.environ.get("PGPORT")

    # Agar xost yoki token topilmasa, xato xabarini ko'rsatish
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN muhit o'zgaruvchisi topilmadi.")
    if not DB_HOST:
        print("DIQQAT: PostgreSQL muhit o'zgaruvchilari (PGHOST kabi) topilmadi. DB ulanishsiz ishlaydi.")
