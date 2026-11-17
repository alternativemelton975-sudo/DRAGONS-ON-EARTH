from flask import Flask, render_template_string
import random
import os

app = Flask(__name__)

colors = ["🔴 Red", "🔵 Blue", "💚 Green", "💛 Gold", "⚫ Black", "⚪ Silver"]
sizes = ["Small", "Medium", "Large", "Colossal"]
abilities = [
    "Frost Breath",
    "Fire Breath",
    "Lightning Strike",
    "Mind Control",
    "Time Manipulation"
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🐉 Dragons On Earth</title>
    <style>
        body {
            background:#1a1a1a;
            color:white;
            text-align:center;
            font-family:Arial;
            padding:40px;
        }

        .dragon {
            background:#2a2a2a;
            padding:20px;
            border-radius:15px;
            width:400px;
            margin:auto;
        }

        button {
            padding:15px 25px;
            font-size:18px;
            border:none;
            border-radius:10px;
            background:#ff6600;
            color:white;
            cursor:pointer;
        }

        button:hover {
            background:#ff8800;
        }
    </style>
</head>
<body>

<h1>🐉 DRAGONS ON EARTH 🐉</h1>

<div class="dragon">
    <h2>{{name}}</h2>
    <p><b>Color:</b> {{color}}</p>
    <p><b>Size:</b> {{size}}</p>
    <p><b>Power:</b> {{power}}</p>
    <p><b>Age:</b> {{age}} years</p>
    <p><b>Ability:</b> {{ability}}</p>
</div>

<br>

<form method="get">
    <button type="submit">
