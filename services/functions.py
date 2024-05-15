from difflib import SequenceMatcher

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