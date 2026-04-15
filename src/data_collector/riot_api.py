import os
import requests
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()


class RiotAPI:
    def __init__(self):
        self.api_key = os.getenv("RIOT_API_KEY")

        if not self.api_key:
            raise ValueError("RIOT_API_KEY não encontrada no arquivo .env")

        self.account_base_url = "https://americas.api.riotgames.com"
        self.match_base_url = "https://americas.api.riotgames.com"

        self.headers = {
            "X-Riot-Token": self.api_key
        }

    def get_account_by_riot_id(self, game_name: str, tag_line: str) -> dict:
        encoded_game_name = quote(game_name.strip())
        encoded_tag_line = quote(tag_line.strip())

        url = (
            f"{self.account_base_url}/riot/account/v1/accounts/"
            f"by-riot-id/{encoded_game_name}/{encoded_tag_line}"
        )

        response = requests.get(url, headers=self.headers, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Erro {response.status_code}: {response.text}")

        return response.json()

    def get_match_ids_by_puuid(self, puuid: str, count: int = 5) -> list[str]:
        url = f"{self.match_base_url}/lol/match/v5/matches/by-puuid/{puuid}/ids"

        params = {
            "start": 0,
            "count": count
        }

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"Erro {response.status_code}: {response.text}")

        return response.json()

    def get_match_details(self, match_id: str) -> dict:
        url = f"{self.match_base_url}/lol/match/v5/matches/{match_id}"

        response = requests.get(url, headers=self.headers, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Erro {response.status_code}: {response.text}")

        return response.json()