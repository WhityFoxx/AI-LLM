import aiogram

import os
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
from handlers import router

async def main():
    bot = aiogram.Bot(os.environ.get("TOKEN") )

    dp = aiogram.Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
