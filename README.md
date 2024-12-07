# Steam Badge Checker

## Description
The **Steam Badge Checker** is a Python script that helps Steam users analyze their game library and categorize games based on badge availability. It leverages Steam's public API to retrieve data about owned games and associated badges, organizing them into two categories:

1. **Badge Available**: Games where the user has at least one badge.
2. **Badge Missing**: Games that have no earned badges.

The results are logged into a text file for easy reference and future analysis.

## Features
- **Automated Game Categorization**: Automatically fetches all owned games and their badge statuses.
- **Badge-Level Analysis**: Categorizes games into "Badge Available" or "Badge Missing" based on badge presence.
- **Multi-Threaded Processing**: Uses threading to optimize the speed of API requests for large libraries.
- **Output Logging**: Results are saved to a structured text file (`steam_badges_log.txt`) for convenience.
- **Minimal Dependencies**: Requires only the `requests` library for API interactions.

## How to Use

### Setup
1. Obtain your Steam API key from the [Steam Community API page](https://steamcommunity.com/dev/apikey).
2. Replace `<YOUR_STEAM_API_KEY>` and `<YOUR_STEAM_ID>` in the script with your API key and Steam ID.

### Run the Script
Execute the script in a Python environment:
```bash
python steam_badge_tracker.py
```

### View Results
Check the output in the `steam_badges_log.txt` file, organized into "Badge Available" and "Badge Missing" categories.

## Requirements
- Python 3.8 or higher
- `requests` library: Install with
  ```bash
  pip install requests
  ```

## Use Cases
- **Badge Collectors**: Identify games missing badges for completion.
- **Game Tracking**: Maintain an organized view of badge achievements across your library.
- **Efficiency**: Quickly analyze large libraries with minimal effort.

## License
This project is licensed under the MIT License. Contributions and improvements are welcome!

