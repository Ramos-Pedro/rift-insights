from src.data_collector.riot_api import RiotAPI


class MatchService:
    def __init__(self):
        self.api = RiotAPI()

    def get_recent_match_ids(self, puuid: str, count: int = 5) -> list[str]:
        return self.api.get_match_ids_by_puuid(puuid, count)

    def get_match_details(self, match_id: str) -> dict:
        return self.api.get_match_details(match_id)