import asyncio
import logging
from aiogram import Bot, Dispatcher
from routes import r


TOKEN = "7333198091:AAFL9bK9eIt077K3Q_zmFrDx00GlQOSDcCg"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(r)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())