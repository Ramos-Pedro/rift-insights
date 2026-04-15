from flask import Flask, render_template, request
from src.data_collector.summoner_service import SummonerService

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    puuid = None
    error = None
    riot_id = None

    if request.method == "POST":
        riot_id = request.form.get("riot_id")

        try:
            game_name, tag_line = [x.strip() for x in riot_id.split("#", 1)]

            service = SummonerService()
            puuid = service.get_puuid(game_name, tag_line)

        except ValueError:
            error = "Formato inválido. Use Nome#TAG"
        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        puuid=puuid,
        error=error,
        riot_id=riot_id
    )


if __name__ == "__main__":
    app.run(debug=True)