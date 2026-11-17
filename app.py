from flask import Flask, jsonify, request
import random
from enum import Enum
import os

app = Flask(__name__)

class DragonColor(Enum):
    RED = "🔴 Red"
    BLUE = "🔵 Blue"
    GREEN = "💚 Green"
    GOLD = "💛 Gold"
    BLACK = "⚫ Black"
    SILVER = "⚪ Silver"

class DragonSize(Enum):
    SMALL = "Small (30ft)"
    MEDIUM = "Medium (50ft)"
    LARGE = "Large (80ft)"
    COLOSSAL = "Colossal (150ft+)"

def dragon_story(location: str) -> str:
    templates = [
        f"A dragon rises over {location}, bringing wonder and flame.",
        f"The skies darken as an ancient dragon awakens above {location}.",
        f"From the depths emerges a mighty dragon, casting shadow upon {location}.",
        f"Legend speaks of a dragon that dwells near {location}, and today it takes flight.",
    ]
    return random.choice(templates)

def create_dragon_profile(name, location, color, size):
    return {
        "name": name,
        "location": location,
        "color": color.value,
        "size": size.value,
        "power_level": random.randint(1, 100),
        "age": random.randint(50, 5000),
        "special_ability": random.choice([
            "Frost breath",
            "Fire breath",
            "Lightning strike",
            "Mind control",
            "Time manipulation"
        ])
    }

def dragon_battle_stats(dragon1, dragon2):
    winner = dragon1 if dragon1["power_level"] > dragon2["power_level"] else dragon2
    loser = dragon2 if winner == dragon1 else dragon1

    return {
        "winner": winner["name"],
        "winner_power": winner["power_level"],
        "loser": loser["name"],
        "loser_power": loser["power_level"],
        "result": f"{winner['name']} would likely defeat {loser['name']}"
    }

def generate_dragon_lore(dragon):
    abilities_desc = {
        "Frost breath": "freezes anything in its path",
        "Fire breath": "consumes everything with eternal flames",
        "Lightning strike": "commands the very storms themselves",
        "Mind control": "bends the will of those who gaze upon it",
        "Time manipulation": "moves between moments as it pleases"
    }

    ability_desc = abilities_desc.get(
        dragon["special_ability"],
        "possesses ancient magic"
    )

    return (
        f"{dragon['name']}, a {dragon['age']}-year-old "
        f"{dragon['color'].split()[-1].lower()} dragon, dwells near "
        f"{dragon['location']}. This magnificent creature "
        f"{ability_desc}. Beware its power!"
    )

@app.route("/")
def home():
    return """
    <h1>🐉 Dragons on Earth API</h1>

    <h3>Story</h3>
    <a href="/story?location=Miami">/story?location=Miami</a>

    <h3>Dragon Profile</h3>
    <a href="/profile?name=Inferno&location=Volcano">
    /profile?name=Inferno&location=Volcano
    </a>

    <h3>Battle</h3>
    <a href="/battle?location=DragonPeak">
    /battle?location=DragonPeak
    </a>
    """

@app.route("/story")
def story():
    location = request.args.get("location", "the mountain")

    return jsonify({
        "location": location,
        "story": dragon_story(location)
    })

@app.route("/profile")
def profile():
    name = request.args.get("name", "Inferno")
    location = request.args.get("location", "the mountain")

    dragon = create_dragon_profile(
        name,
        location,
        random.choice(list(DragonColor)),
        random.choice(list(DragonSize))
    )

    return jsonify({
        "dragon": dragon,
        "lore": generate_dragon_lore(dragon)
    })

@app.route("/battle")
def battle():
    location = request.args.get("location", "the mountain")

    dragon1 = create_dragon_profile(
        "Inferno",
        location,
        random.choice(list(DragonColor)),
        random.choice(list(DragonSize))
    )

    dragon2 = create_dragon_profile(
        "Icewing",
        location,
        random.choice(list(DragonColor)),
        random.choice(list(DragonSize))
    )

    return jsonify({
        "dragon1": dragon1,
        "dragon2": dragon2,
        "battle": dragon_battle_stats(dragon1, dragon2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
