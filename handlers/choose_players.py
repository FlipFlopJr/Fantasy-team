from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from config_data.dispatcher import bot
from aiogram.fsm.context import FSMContext
from fsm.comand import TeamState
from difflib import SequenceMatcher
from services.functions import find_player_by_name
from services.parser import Parser
from services.variables import users



router = Router()
parser = Parser()
players = parser.get_players_dict('https://org.infobasket.su/Comp/GetTeamStats/42729')

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
    #Функция обработки наиболее подходящего игрокаЮ даже если в написании были ошибки
    closet_match, max_similarity = find_player_by_name(message.text,players)
    await bot.send_message(message.from_user.id,f'Вы успешно выбрали {closet_match} позиции PG')

    await state.update_data(point_guard=closet_match)
    users[message.from_user.id]['point_guard'] = closet_match

    await state.clear()



#Хэндлер для обработки нажатия кнопки с callback_data SG
@router.callback_query(F.data == 'SG')
async def process_shooting_guard(callback:CallbackQuery, state:FSMContext):
    await callback.answer() #Убрали бесконечную загрузку на кнопке
    await bot.send_message(callback.from_user.id, text='Введите имя и фамилию игрока, которого вы хотите поставить на позиции атакующего защитника')  
    await state.set_state(TeamState.shooting_guard)

#Хэндлер для обработки ввода пользователем shooting guard
@router.message(TeamState.shooting_guard)
async def process_message_shooting_guard(message:Message, state:FSMContext):
    closet_match, max_similarity = find_player_by_name(message.text,players)
    await bot.send_message(message.from_user.id,f'Вы успешно выбрали {closet_match} позиции SG')

    await state.update_data(shooting_guard=closet_match)
    users[message.from_user.id]['shooting_guard'] = closet_match

    await state.clear()


#Хэндлер для обработки нажатия кнопки с callback_data SF
@router.callback_query(F.data == 'SF')
async def process_small_forward(callback:CallbackQuery, state:FSMContext):
    await callback.answer() #Убрали бесконечную загрузку на кнопке
    await bot.send_message(callback.from_user.id, text='Введите имя и фамилию игрока, которого вы хотите поставить на позиции легкого форварда')  
    await state.set_state(TeamState.small_forward)

#Хэндлер для обработки ввода пользователем small forward
@router.message(TeamState.small_forward)
async def process_message_small_forward(message:Message, state:FSMContext):
    closet_match, max_similarity = find_player_by_name(message.text,players)
    await bot.send_message(message.from_user.id,f'Вы успешно выбрали {closet_match} позиции SF')

    await state.update_data(small_forward=closet_match)
    users[message.from_user.id]['small_forward'] = closet_match

    await state.clear()


#Хэндлер для обработки нажатия кнопки с callback_data PF
@router.callback_query(F.data == 'PF')
async def process_power_forward(callback:CallbackQuery, state:FSMContext):
    await callback.answer() #Убрали бесконечную загрузку на кнопке
    await bot.send_message(callback.from_user.id, text='Введите имя и фамилию игрока, которого вы хотите поставить на позиции тяжелого форварда')  
    await state.set_state(TeamState.power_forward)

#Хэндлер для обработки ввода пользователем power forward
@router.message(TeamState.power_forward)
async def process_message_power_forward(message:Message, state:FSMContext):
    closet_match, max_similarity = find_player_by_name(message.text,players)
    await bot.send_message(message.from_user.id,f'Вы успешно выбрали {closet_match} позиции PF')

    await state.update_data(power_forward=closet_match)
    users[message.from_user.id]['power_forward'] = closet_match
    
    await state.clear()


#Хэндлер для обработки нажатия кнопки с callback_data C
@router.callback_query(F.data == 'C')
async def process_center(callback:CallbackQuery, state:FSMContext):
    await callback.answer() #Убрали бесконечную загрузку на кнопке
    await bot.send_message(callback.from_user.id, text='Введите имя и фамилию игрока, которого вы хотите поставить на позиции центрового')  
    await state.set_state(TeamState.center)

#Хэндлер для обработки ввода пользователем center
@router.message(TeamState.center)
async def process_message_center(message:Message, state:FSMContext):
    closet_match, max_similarity = find_player_by_name(message.text,players)
    await bot.send_message(message.from_user.id,f'Вы успешно выбрали {closet_match} позиции C')

    await state.update_data(center=closet_match)
    users[message.from_user.id]['center'] = closet_match
    
    await state.clear()
