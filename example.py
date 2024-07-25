import os
from datetime import datetime

# Personalized Greeting
print(f"Greetings, {os.environ.get('GITHUB_ACTOR', 'friend')}! 👋 This is your custom GitHub Action speaking.")  # Use 'friend' if GITHUB_ACTOR is not set
print("     _   _                _            _   _  _____ \n    | | | |              | |          | \ | |/ ____|\n    | |_| |__   ___  _ __| | ___ _   _|  \| | | (___ \n    | __| '_ \ / _ \| '__| |/ _ \ | | | . ` | \___ \ \n    | |_| | | | (_) | |  | |  __/ |_| | |\  | ____) |\n     \__|_| |_|\___/|_|  |_|\___|\__, |_| \_|/_____/\n                                  __/ |             \n                                 |___/              ")

# Date and Time
now = datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"\nCurrent date and time: {formatted_datetime}")
