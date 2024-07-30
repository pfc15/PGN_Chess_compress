from chessdotcom import client, Client
from datetime import datetime

def import_games(userName):
   try:
      Client.request_config["headers"]["User-Agent"] = (
         "My Python Application."
         "Contact me at email@example.com"
      )
      agora = datetime.now()
      eu = client.get_player_games_by_month_pgn(userName, datetime_obj=agora)
      with  open(f"jogos_{userName}.pgn", 'w') as fp:
         fp.write(eu.text)
      return True
   except:
      return False
   
