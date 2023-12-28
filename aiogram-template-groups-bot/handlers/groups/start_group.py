from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from filters import IsGroup

from loader import dp




@dp.message_handler(IsGroup(), Command())
async def start_group(message: types.Message):
    await message.answer(f"Salom, {message.from_user.first_name} guruhga qo'shildingiz")