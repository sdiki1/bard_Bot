import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.handlers.start import register_start
from tg_bot.config import load_config
from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.echo import register_echo

logger = logging.getLogger(__name__)



def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)

def register_all_handlers(dp):
    register_start(dp)
    register_echo(dp)




async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot)
    bot['config'] = config

    #register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storager.close()
        await dp.storage.wait_closed()
        await bot.session.close()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

