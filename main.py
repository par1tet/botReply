import asyncio
import logging
from aiogram import Bot, Dispatcher
from routes import r


TOKEN = "7590463321:AAF_XdG82JrnxpFlWh9vT5PFWtWq4OSWA9I"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(r)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())