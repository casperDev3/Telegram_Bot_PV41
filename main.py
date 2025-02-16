import asyncio
import logging
import sys
from os import getenv


from utils.products import get_all_products, get_all_categories
from utils.formatter import formatter_msg_with_product, formatter_msg_with_all_categories

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
            [{"text": "📞Зв'язатися з нами"}, {"text": "СПАМ МАТВІЯ"}],
            [{"text": "🥡Продукти"}]
        ],
        "resize_keyboard": False
    }


def get_products_keyboard():
    return {
        "keyboard": [
            [{"text": "Показати всі продукти"}, {"text": "Показати категорії"}],
            [{"text": "Головне меню"}]
        ],
        "resize_keyboard": False
    }


# inline keyboard markup
def get_categories_inline_keyboard(categories):
    keyboard = []
    for category in categories:
        keyboard.append([{"text": f"🎒 {category}", "callback_data": category}])

    return {
        "inline_keyboard": keyboard
    }


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("Мур-мур-мур", reply_markup=get_main_keyboard())
    print("__USER_ID", message.from_user.id)


@dp.message()
async def reply_keyboard_handler(message: Message) -> None:
    msg = message.text
    if msg == "⚙️Налаштування":
        await message.answer("Виберіть налаштування")
    elif msg == "🏚Про нас":
        await message.answer("Ми найкращий бот для вас")
    elif msg == "📞Зв'язатися з нами":
        await message.answer("Телефонуйте нам за номером +380123456789")
    elif msg == "🥡Продукти":
        await message.answer("Ви перейшли в категорію продукти. Зробіть свій вибір:",
                             reply_markup=get_products_keyboard())
    elif msg == "Головне меню":
        await message.answer("Головне меню", reply_markup=get_main_keyboard())
    elif msg == "Показати всі продукти":
        products = get_all_products()
        for product in products:
            text_msg = formatter_msg_with_product(product)
            await message.answer(text_msg)
    elif msg == "Показати категорії":
        categories = get_all_categories()
        text_msg = formatter_msg_with_all_categories(categories)
        await message.answer("Категорії продуктів:", reply_markup=get_categories_inline_keyboard(categories))
    elif msg == "СПАМ МАТВІЯ":
        for i in range(30):
            user_id = "5790648458"
            # send message to user with user_id




# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
