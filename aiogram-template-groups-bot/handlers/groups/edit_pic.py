import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("change_photo", prefixes="!/"), AdminFilter())
async def change_photo(message: types.Message):
    s_message =     message.reply_to_message
    title = s_message.text
    await bot.set_chat_photo(message.chat.id, title=title)