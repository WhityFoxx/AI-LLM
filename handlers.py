from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from llmapi import get_response
from aiogram.enums.parse_mode import ParseMode
router = Router()

messages = {} # 
@router.message()
async def message_handler(msg: Message) -> None:
    if msg.chat.id not in messages.keys():
        messages[msg.chat.id] = []

    if msg.text is None:
        return await msg.answer("Извини, но я пока принимаю только текст!")
    

    messages[msg.chat.id].append({'role': 'user', 'content': msg.text})
    response = get_response(messages[msg.chat.id])
    await msg.answer(response, parse_mode=ParseMode.MARKDOWN)
@router.message(CommandStart())
async def start(msg: Message) -> None:
    await msg.mark("Привет, я бот для взаимодействия с LLM! Бот сделать Ким И.В БИК2405.")
@router.message(Command("help"))
async def help(msg: Message) -> None:
    await msg.answer("Можешь написать мне сообщение, а я постараюсь вам на него мяутветить!")

