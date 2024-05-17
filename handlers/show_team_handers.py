from aiogram import Router
from aiogram.types import Message, InputFile
from lexicon.lexicon_ru import LEXICON_RU
from config_data.dispatcher import bot
from aiogram.filters import Command,StateFilter
from aiogram.fsm.state import default_state
from PIL import Image, ImageDraw, ImageFont
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from fsm.comand import TeamState
from services.variables import users
import os

router = Router()

def draw_picture(user_id):
    colors ={'point_guard':(290, 170),
             'shooting_guard':(142,325),
             'small_forward':(672,383),
             'power_forward':(619,197),
             'center':(404,343)}

    picture = Image.open('C:/Users/Andrey/УЧЕБА/прога/Fantasy team/bot/pictures/general_pictures/rasstanovka.png')
    font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", size=25)
    idraw = ImageDraw.Draw(picture)

    for position in ['point_guard','shooting_guard','small_forward','power_forward','center']:
        if users[user_id].get(position):
            full_name = users[user_id][position] 
            last_name = full_name.split(' ')[0]
            first_name = full_name.split(' ')[1]

            lenght = max(idraw.textlength(last_name,font),idraw.textlength(first_name,font))
            idraw.text((colors[position][0] - lenght//2, colors[position][1]), last_name + '\n' + first_name, font=font,align='center',fill=(0,0,0))

    picture.save(f'C:/Users/Andrey/УЧЕБА/прога/Fantasy team/bot/pictures/users_pictures/rasstanovka_{user_id}.png')  

#Хэндлер для обработки нажатия  команды show_team
@router.message(Command(commands=['show_team']))
async def process_show_team_command(message:Message):
    draw_picture(message.from_user.id)
    photo = FSInputFile(f'C:/Users/Andrey/УЧЕБА/прога/Fantasy team/bot/pictures/users_pictures/rasstanovka_{message.from_user.id}.png')
    await bot.send_photo(message.from_user.id,photo)
    os.remove(f'C:/Users/Andrey/УЧЕБА/прога/Fantasy team/bot/pictures/users_pictures/rasstanovka_{message.from_user.id}.png')
