from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from keyboards.start_kb import start_keyboard, welcome_keyboard
from config_data.dispatcher import bot
from services.variables import users




router = Router()


async def remove_chat_buttons(chat_id: int, 
                              msg_text: str = r"_It is not the message you are looking for\.\.\._"):
    """Deletes buttons below the chat.
    For now there are no way to delete kbd other than inline one, check
    """
    msg = await bot.send_message(chat_id,
                                 msg_text,
                                 reply_markup=ReplyKeyboardRemove(),
                                 parse_mode="MarkdownV2")
    await msg.delete()

# Handler for command /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    users[message.from_user.id] = {}
    await bot.send_message(message.from_user.id, text=LEXICON_RU['/start'],reply_markup=start_keyboard)

    

@router.message(Command(commands=['team']))
@router.message(F.text =='Старт' )
async def process_welcome_query(message:Message):
    await remove_chat_buttons(message.from_user.id)
    await bot.send_message(message.from_user.id,text = LEXICON_RU['welcome'],reply_markup=welcome_keyboard)


