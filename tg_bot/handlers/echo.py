from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tg_bot.BARD import Chatbot
import logging

logger = logging.getLogger(__name__)

token = 'WggVSk6eVaLHzzDR1DWDARPQHN5NfSWRwEL1kAtB504Q8cAySVa-CF8NUROxEMcQIGVRjw.'
chatbot = Chatbot(token)



async def bot_echo(message: types.Message):
    answer = chatbot.ask(message.text)
    logger.info(f'user tg_id: {message.from_user.id}, ask to bard: {message.text}')
    await message.answer(answer['content'])




def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)

