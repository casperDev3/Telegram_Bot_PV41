import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7331456101:AAHmQ0Sf6NqQCEjfIC57uWgaR_umLIKzF2U"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

# reply keyboard markup
def get_main_keyboard():
    return {
        "keyboard": [
            [{"text": "⚙️Налаштування"}, {"text": "🏚Про нас"}],
            [{"text": "📞Зв'язатися з нами"}]
        ],
        "resize_keyboard": False
    }

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("Мур-мур-мур", reply_markup=get_main_keyboard())


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        msg = message.text
        if msg == "⚙️Налаштування":
            await message.answer("Виберіть налаштування")
        elif msg == "🏚Про нас":
            await message.answer("Ми найкращий бот для вас")
        elif msg == "📞Зв'язатися з нами":
            await message.answer("Телефонуйте нам за номером +380123456789")
        else:
            await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())