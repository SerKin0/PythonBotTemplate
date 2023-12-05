import asyncio
import logging
from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


load_dotenv(".env")
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Стартовое сообщение!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    logger.info("start message")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создание логгера
    logger = logging.getLogger(__name__)

    # Установка уровня логирования
    logger.setLevel(logging.INFO)

    # Добавление обработчика для записи логов в файл
    file_handler = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    asyncio.run(main())
