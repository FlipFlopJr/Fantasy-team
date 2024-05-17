import requests as rq
from bs4 import BeautifulSoup as bs



class Parser:
    def __init__(self) -> None:
        self.players1= {}
        self.players2= {}
        

    def get_players_dict(self,url) -> dict[str:dict]:
        self.response = rq.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'})
        self.response_json = self.response.json()
        for team in self.response_json['Stats']:
            team_name = team['TeamName']['CompTeamNameRu']
            for player in team['Players']:
                personInfo = player['PersonInfo']
                age = personInfo['Age']
                birth_date = personInfo['PersonBirth']
                full_name = personInfo['PersonFullNameRu']
                first_name = personInfo['PersonFirstNameRu']
                last_name = personInfo['PersonLastNameRu']
                position = personInfo['Players'][0]['PlayerPosition']

                assists = personInfo['Assist']
                blocks = personInfo['Blocks']
                rebound = personInfo['Rebound']
                fouls = personInfo['Foul']
                points = personInfo['Points']
                steals = personInfo['Steal']
                shots = personInfo['Shot23']
                plus_minus = personInfo['PlusMinus']
                turnovers = personInfo['Turnover']

                position_word = ''
                match position:
                    case 1:
                        position_word = 'Разыгрывающий защитник (PG)'
                    case 2:
                        position_word = 'Атакующий защитник (SG)'
                    case 3:
                        position_word = 'Лёгкий форвард (SF)'
                    case 4:
                        position_word = 'Мощный форвард (PF)'
                    case 5:
                        position_word = 'Центровой (C)'

                self.players1[full_name] = {'first name':first_name,
                                            'last name':last_name,
                                            'team':team_name,
                                            'age':age,
                                            'birth date':birth_date,
                                            'position':position, 
                                            'position_word':position_word,
                                            'assists':assists,
                                            'blocks':blocks,
                                            'rebounds':rebound,
                                            'fouls':fouls,
                                            'points':points,
                                            'steals':steals,
                                            'shots':shots,
                                            'plus_minus':plus_minus,
                                            'turnovers':turnovers}
        
        return self.players1
    
    def get_players_dict_bs(self,url) -> dict[str: dict]:
        response = rq.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'})
        soup = bs(response.text, 'lxml')
        players = soup.find_all('tr',attrs={'class':'ng-scope'})
        print(response.text)
        

    

# parser = Parser()
# players = parser.get_players_dict('https://org.infobasket.su/Comp/GetTeamStats/42729')
# # players2 = parser.get_players_dict_bs('https://www.championat.com/basketball/_vtbleague/tournament/5671/statistic/player/point/#')
# print(players)