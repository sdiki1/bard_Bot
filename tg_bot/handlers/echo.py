from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tg_bot.BARD import Chatbot
import logging

logger = logging.getLogger(__name__)

token = 'WggVSk6eVaLHzzDR1DWDARPQHN5NfSWRwEL1kAtB504Q8cAySVa-CF8NUROxEMcQIGVRjw.'
chatbot = Chatbot(token)



async def bot_echo(message: types.Message):
    logger.info(f'user tg_id: {message.from_user.id}, ask to bard: {message.text}')
    answer = chatbot.ask(message.text)
    if 'Google Bard encountered an error:' in answer:
        logger.error(f'{answer}')
        await message.answer('Some troubles with bard, wait some time')
    else:
        logger.info(f'user tg_id: {message.from_user.id}, answer from broad has been got')
        await message.answer(answer['content'])


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)

