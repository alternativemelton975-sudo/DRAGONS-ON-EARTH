from flask import Flask, render_template_string, request
import random
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🐉 Dragons on Earth</title>
    <style>
        body {
            background: #111;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 30px;
        }

        .card {
            background: #222;
            padding: 20px;
            margin: 20px auto;
            border-radius: 15px;
            width: 500px;
            box-shadow: 0 0 15px orange;
        }

        .btn {
            display: inline-block;
            padding: 12px 20px;
            background: orange;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            margin: 10px;
            font-weight: bold;
        }

        .btn:hover {
            background: darkorange;
        }

        h1 {
            color: gold;
        }
    </style>
</head>
<body>

    <h1>🐉 DRAGONS ON EARTH 🐉</h1>

    <div class="card">
        <h2>{{ dragon["name"] }}</h2>
        <p><strong>Color:</strong> {{ dragon["color"] }}</p>
        <p><strong>Size:</strong> {{ dragon["size"] }}</p>
        <p><strong>Age:</strong> {{ dragon["age"] }} years</p>
        <p><strong>Power:</strong> {{ dragon["power"] }}/100</p>
        <p><strong>Ability:</strong> {{ dragon["ability"] }}</p>
    </div>

    {% if winner %}
    <div class="card">
        <h2>⚔️ Battle Result ⚔️</h2>
        <p>{{ winner }}</p>
    </div>
    {% endif %}

    <a class="btn" href="/">Summon Dragon</a>
    <a class="btn" href="/battle">Battle Dragons</a>

</body>
</html>
"""

names = [
    "Inferno",
    "Icewing",
    "Stormfang",
    "Shadowclaw",
    "Goldfire",
    "Nightscale",
    "Thunderjaw"
]

colors = [
    "🔴 Red",
    "🔵 Blue",
    "💚 Green",
    "💛 Gold",
    "⚫ Black",
    "⚪ Silver"
]

sizes = [
    "Small",
    "Medium",
    "Large",
    "Colossal"
]

abilities = [
    "Fire Breath",
    "Frost Breath",
    "Lightning Strike",
    "Mind Control",
    "Time Manipulation"
]


def generate_dragon():
    return {
        "name": random.choice(names),
        "color": random.choice(colors),
        "size": random.choice(sizes),
        "age": random.randint(100, 5000),
        "power": random.randint(1, 100),
        "ability": random.choice(abilities)
    }


@app.route("/")
def home():
    dragon = generate_dragon()

    return render_template_string(
        HTML,
        dragon=dragon,
        winner=None
    )


@app.route("/battle")
def battle():
    dragon1 = generate_dragon()
    dragon2 = generate_dragon()

    if dragon1["power"] >= dragon2["power"]:
        result = f"{dragon1['name']} defeated {dragon2['name']}!"
        winner_dragon = dragon1
    else:
        result = f"{dragon2['name']} defeated {dragon1['name']}!"
        winner_dragon = dragon2

    return render_template_string(
        HTML,
        dragon=winner_dragon,
        winner=result
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
