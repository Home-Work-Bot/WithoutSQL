import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

#messageLinkExample
#https://t.me/c/1401136600/18634
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
async def main():
    
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

#from logic.getData import getData
if __name__ == "__main__":
    #getData()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
