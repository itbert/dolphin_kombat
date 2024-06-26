from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import WebAppInfo


async def webapp_build_clicker() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Играть в кликер 🐬', web_app=WebAppInfo(
            url='URL КЛИКЕРА'
        )
    )
    return builder.adjust(1).as_markup()
