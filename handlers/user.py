from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "user")
async def hi_user(message: Message):
    await message.answer("Hi, user")
