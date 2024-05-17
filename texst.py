from PIL import Image, ImageDraw, ImageFont


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

            lenght = idraw.textlength(surname,font)
            idraw.text((colors[position][0] - lenght//2, colors[position][1]), last_name + '\n' + first_name, font=font,align='center',fill=(0,0,0))

    picture.save(f'C:/Users/Andrey/УЧЕБА/прога/Fantasy team/bot/pictures/users_pictures/rasstanovka1.png')  

