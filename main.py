import os
import asyncio
import logging
from aiogram import F
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from core.utils.commands import set_commands
from core.handlers.message import start_command, get_music

load_dotenv()
token = os.getenv("TOKEN_TG")


async def start_bot(bot: Bot):
	"""Функция, вызываемая при остановке бота"""
	await set_commands(bot)  # Настраиваем команды бота


async def stop_bot(bot: Bot):
	"""Функция, вызываемая при остановке бота"""
	# Отправляем запрос на получение информации о боте и сохраняем его имя в переменной bot_name.
	...


async def start():
	bot = Bot(token=token, parse_mode='HTML')  # Создаём объект бота с заданным токеном

	dp = Dispatcher()  # Создаём диспетчер для обработки входящих сообщений и команд

	# Регистрируем функции-обработчики при старте и остановке бота
	dp.startup.register(start_bot)  # Функция срабатывает при запуске бота
	dp.shutdown.register(stop_bot)  # Функция срабатывает при остановке бота

	dp.message.register(start_command, Command(commands=['start']))

	dp.message.register(get_music)

	logging.basicConfig(level=logging.INFO)  # Настраиваем логирование

	try:
		await dp.start_polling(bot)  # Запускаем бота на прослушивание входящих сообщений
	finally:
		await bot.session.close()


# Основной запуск
if __name__ == '__main__':
	while True:
		asyncio.run(start())
