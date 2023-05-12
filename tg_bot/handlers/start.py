from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
import logging

logger = logging.getLogger(__name__)

async def start(message: types.Message):
    logger.info(f"user tg_ud: {message.from_user.id}, command: /start")
    await message.reply('Hello, this bot will help you with everything using Google Bard, ask the question, but know, that bard using only english language):')

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')


