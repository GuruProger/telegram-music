from aiogram import Bot
from aiogram.types import Message


async def start_command(message: Message, bot: Bot):
	await message.answer(
		'Просто вводи название трека или имя исполнителя (или и то, и другое) я сделаю всё остальное! 😉')


async def get_music(message: Message, bot: Bot, state):
	"""Бот ищет музыку по названию"""
	music_name = message.text
	...
