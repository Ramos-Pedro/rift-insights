from src.data_collector.riot_api import RiotAPI


class SummonerService:
    def __init__(self):
        self.api = RiotAPI()

    def get_puuid(self, game_name: str, tag_line: str) -> str:
        account_data = self.api.get_account_by_riot_id(game_name, tag_line)
        return account_data["puuid"]