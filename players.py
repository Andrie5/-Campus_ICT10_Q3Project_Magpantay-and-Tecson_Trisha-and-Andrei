from pyscript import document, window

NAMES = [ # need this list so that the loop can print it
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
    result = document.getElementById("result") #so that it knows what and where to print the result/list in
    lines = [] 
    for i, name in enumerate(NAMES, start=1): # a for loop that prints out the NAME list, the enumerate makes it so that it is automatically numbered
        lines.append(f"{i}. {name}")
    result.innerHTML = "<br>".join(lines)


window.players = players # this is so that the function will work when the button is pressed
