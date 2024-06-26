from typing import Generator, Coroutine

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.methods import SendMessage, AnswerCallbackQuery
from aiogram.types import Message, CallbackQuery

from configuration.texts_to_messages import start_text, help_text

from app_bot.keyboards import start_markup, help_markup, markup_webapp_build_clicker

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> SendMessage:
    await message.answer(
        text=start_text,
        reply_markup=start_markup
    )


@router.callback_query(F.data == 'how_to_earn')
async def how_to_earn(callback: CallbackQuery) -> AnswerCallbackQuery:
    await callback.answer(text='Как заработать на кликере', show_alert=True)
    await callback.answer(text=help_text)


@router.message(Command('help'))
async def cmd_help(message: Message) -> SendMessage:
    await message.answer(text=help_text, reply_markup=help_markup)


@router.callback_query(F.data == 'goto_clicker')
async def goto_clicker(callback: CallbackQuery, message: Message) -> (AnswerCallbackQuery | SendMessage
                                                                      | Generator | Coroutine):
    await callback.answer(text='Играй! Зарабатывай!', show_alert=False)
    await message.reply(text='Играть здесь ↓', reply_markup=await markup_webapp_build_clicker())
