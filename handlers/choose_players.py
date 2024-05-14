from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from config_data.dispatcher import bot
from aiogram.fsm.context import FSMContext
from fsm.comand import TeamState



router = Router()
#5 хэндлеров для обработка callback_data и 5 хэндлеров для состояний


#Хэндлер для обработки нажатия кнопки с callback_data PG
@router.callback_query(F.data == 'PG')
async def process_point_guard(callback:CallbackQuery, state:FSMContext):
    await callback.answer() #Убрали бесконечную загрузку на кнопке
    await bot.send_message(callback.from_user.id, text='Введите имя и фамилию игрока, которого вы хотите поставить на позиции разыгрывающего')  
    await state.set_state(TeamState.point_guard)

#Хэндлер для обработки ввода пользователем point guard 
@router.message(TeamState.point_guard)
async def process_message_point_guard(message:Message, state:FSMContext):
    await bot.send_message(message.from_user.id,'Вы успешно ввели игрока на позиции PG')
    await state.update_data(point_guard=message.text)
    await state.clear()
