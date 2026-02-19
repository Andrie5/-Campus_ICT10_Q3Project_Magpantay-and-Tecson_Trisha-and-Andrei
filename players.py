from pyscript import document, window

NAMES = [
    "Nathan Abaca",
    "Thea Alavado",
    "Maiah Arenal",
    "Anxela Aventajado",
    "Gab Buhain",
    "Joo Carpio",
    "Athena Cruz",
    "Caiomey Cenon",
    "Nikolo De Leon",
    "Chelsea De Peralta",
    "Jercey Del Barrio",
    "Sittie Dida-Agun",
    "Jarett Dumlao",
    "Jacob Estapia",
    "Chloe Galope",
    "Uriel Galura",
    "Aaron Guevarra",
    "Gelo Gurango",
    "Ezra Lazo",
    "Jacob Liwag",
    "Trisha Magpantay",
    "Kaila Moyaen",
    "Xander Panuncialman",
    "Samantha Prowel",
    "Pio Ramos",
    "Katelyn Sannino",
    "Andrei Tecson",
    "Hans Ulit",
]

def players(*args):
    result = document.getElementById("result")
    lines = []
    for i, name in enumerate(NAMES, start=1):
        lines.append(f"{i}. {name}")
    result.innerHTML = "<br>".join(lines)

window.players = players