from aiogram import Bot
from aiogram.types import Message


async def start_command(message: Message, bot: Bot):
    await message.answer('Hello world')  # Отправляем сообщение пользователю