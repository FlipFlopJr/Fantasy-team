from difflib import SequenceMatcher
from PIL import Image, ImageDraw, ImageFont

def find_player_by_name(name:str, players:dict):
    name_lower = name.lower()
    max_similarity = 0
    closest_match = None

    for player_name, player_info in players.items():
        similarity = SequenceMatcher(None, name_lower, player_name.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            closest_match = player_name

    return closest_match, max_similarity

def write_player_on_picture(player_name:str, picture:Image,position:str):
    image = Image.open()