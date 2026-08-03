import asyncio
from nba_api.stats.static import players as nba_p
from nfl_api_client.static import players as nfl_p


async def nba_player():
    name = "Lebron James"  # read the "player_name" field, default to "" if missing
    match = nba_p.find_players_by_full_name(name)  # search the static player list for that name
    await asyncio.sleep(2)
    print(match[0]['full_name'])

async def nfl_player():
    name = "Dak Prescott"
    match = nfl_p.find_players_by_full_name(name)
    print(match[0]['full_name'])


async def main():
    print("Starting Coroutine")
    player1 = asyncio.create_task(nba_player())
    player2 = asyncio.create_task(nfl_player())

    await player1
    await player2

asyncio.run(main())