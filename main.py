from src.data_collector.summoner_service import SummonerService
from src.data_collector.match_service import MatchService


def main():
    print("=== Rift Insights ===")

    riot_id = input("Digite seu Riot ID: ").strip()

    try:
        game_name, tag_line = [x.strip() for x in riot_id.split("#", 1)]

        summoner_service = SummonerService()
        match_service = MatchService()

        puuid = summoner_service.get_puuid(game_name, tag_line)
        print(f"\nPUUID encontrado: {puuid}")

        match_ids = match_service.get_recent_match_ids(puuid, count=5)

        print("\n=== Últimas partidas ===")
        for i, match_id in enumerate(match_ids, start=1):
            print(f"{i}. {match_id}")

        if match_ids:
            first_match = match_service.get_match_details(match_ids[0])

            print("\n=== Primeira partida carregada com sucesso ===")
            print(f"Match ID: {first_match['metadata']['matchId']}")
            print(f"Modo: {first_match['info']['gameMode']}")
            print(f"Duração: {first_match['info']['gameDuration']} segundos")

    except ValueError:
        print("\nErro: digite no formato Nome#TAG")
    except Exception as e:
        print(f"\nErro ao buscar dados: {e}")


if __name__ == "__main__":
    main()