import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Configuration
API_KEY = "<YOUR_STEAM_API_KEY>"  # Insert your Steam API Key
STEAM_ID = "<YOUR_STEAM_ID>"  # Insert your Steam ID
OUTPUT_FILE = "steam_badges_log.txt"

# Functions

def get_owned_games(api_key, steam_id):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {"key": api_key, "steamid": steam_id, "include_appinfo": True}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("response", {}).get("games", [])
    else:
        print(f"API Error: {response.status_code}")
        return []

def get_game_badge(api_key, steam_id):
    url = f"https://api.steampowered.com/IPlayerService/GetBadges/v1/"
    params = {"key": api_key, "steamid": steam_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        badges = response.json().get("response", {}).get("badges", [])
        badge_apps = {badge.get("appid"): badge.get("level", 0) for badge in badges}
        return badge_apps
    else:
        print(f"API Error while checking badges: {response.status_code}")
        return {}

def log_results(results):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for status, games in results.items():
            f.write(f"{status} ({len(games)}):\n")
            for game in games:
                f.write(f"- {game}\n")
            f.write(f"End of category: {status}\n\n")

def main():
    print("Starting the script...")

    all_games = get_owned_games(API_KEY, STEAM_ID)
    if not all_games:
        print("Failed to retrieve the list of games.")
        return

    badge_apps = get_game_badge(API_KEY, STEAM_ID)

    results = {"Badge Missing": [], "Badge Available": []}

    def process_game(game):
        appid = game["appid"]
        name = game["name"]

        # Check badge availability
        badge_level = badge_apps.get(appid, 0)
        if badge_level >= 1:
            results["Badge Available"].append(name)
        else:
            results["Badge Missing"].append(name)

    with ThreadPoolExecutor() as executor:
        executor.map(process_game, all_games)

    # Sort results
    for key in results:
        results[key].sort()

    # Log results to file
    log_results(results)

    print("Script completed. Results saved to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
