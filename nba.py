import json  # used to write/read the player data as JSON

from flask import Flask, render_template, request  # Flask app, HTML templating, and access to form data
from nba_api.stats.static import players as p  # static lookup table for player names -> IDs
from nba_api.stats.endpoints import commonplayerinfo  # live API call for a single player's details

app = Flask(__name__)  # create the Flask application
@app.route("/", methods=["GET", "POST"])  # home page; GET shows the form, POST handles a search
def player_page():
    player_info = None  # will hold the looked-up player's data (dict) once a search succeeds
    player_stats = None  # will hold the player's headline stats once a search succeeds
    error = None  # will hold an error message if the search finds no match

    if request.method == "POST":  # a name was submitted via the form
        name = request.form.get("player_name", "").strip()  # read the "player_name" field, default to "" if missing
        match = p.find_players_by_full_name(name)  # search the static player list for that name

        if not match:  # no player matched the entered name
            error = f'No player found matching "{name}"'  # message shown to the user on the page
        else:
            players_id = match[0]["id"]  # take the first match's NBA player ID
            nba_player = commonplayerinfo.CommonPlayerInfo(player_id=players_id, timeout=100)  # fetch full player info from the API
            player_info = nba_player.get_normalized_dict()["CommonPlayerInfo"][0]  # pull out the single player record as a plain dict
            player_stats = nba_player.get_normalized_dict()["PlayerHeadlineStats"][0]  # pull out that same player's headline stats
            with open("nba_data.json", "w") as file:  # save the latest lookup to disk
                json.dump({"info": player_info, "stats": player_stats}, file, indent=2)  # write both as one valid JSON document

    return render_template("player.html", player_info=player_info, player_stats=player_stats, error=error)  # render the page, passing in whatever we found (or None)


if __name__ == "__main__":  # only run the server when this file is executed directly
    app.run(debug=True, port=5001)  # start Flask's dev server with auto-reload on port 5001 (5000 is taken by AirPlay)
