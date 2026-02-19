from pyscript import document, window
import random

def signUp(*args):
    Username = document.getElementById("Username")
    Password = document.getElementById("Password")
    result = document.getElementById("result")

    if Username is None or Password is None:
        result.innerHTML = "❌ An unexpected error occurred."
        result.style.color = "red"
        return

    if Username.value.strip() == "" or Password.value.strip() == "":
        result.innerHTML = "❌ Please fill in all fields."
        result.style.color = "red"
        return

    result.innerHTML = f""" ✅ Account created. You may now log in using your credentials, {Username.value}.""" 
    result.style.color = "green"

window.signUp = signUp