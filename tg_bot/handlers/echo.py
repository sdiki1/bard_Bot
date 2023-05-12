from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
#from tg_bot.BARD import Chatbot

#token = 'WggVSk6eVaLHzzDR1DWDARPQHN5NfSWRwEL1kAtB504Q8cAySVa-CF8NUROxEMcQIGVRjw.'
#chatbot = Chatbot(token)


#def ask(ask: str) -> str:
#    answer = chatbot.ask(ask)
#    return answer['content']

async def bot_echo(message: types.Message):
    text = [
        f"Эхо без состояния",
        "Сообщение:",
        message.text
    ]
    await message.answer('\n'.join(text))



async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f"Эхо в состояни {hcode(state_name)}",
        "Сообщение:",
        message.text
    ]


    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state='*', content_types=types.ContentType.ANY)

