from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo


start_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Играть в кликер 🐬', callback_data='goto_clicker')],
        [InlineKeyboardButton(text='Подписаться на канал', url='https://t.me/dolphin_kombat')],
        [InlineKeyboardButton(text='Как зарабатывать', callback_data='how_to_earn')]
    ]
)


async def markup_webapp_build_clicker() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Играть в кликер 🐬',
        web_app=WebAppInfo(url='URL КЛИКЕРА')
    )
    return builder.adjust(1).as_markup()


help_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Играть в кликер 🐬', callback_data='goto_clicker'),
            InlineKeyboardButton(text='Подписаться на канал', url='https://t.me/dolphin_kombat')
        ]
    ]
)
