from pyscript import document, window
import random

def signUp(*args): # this is the fuction that causes the python in the first page to work
    Username = document.getElementById("Username")
    Password = document.getElementById("Password")
    result = document.getElementById("result") # so first we just have to assign the variables so it knows what we are talking about

    if Username is None or Password is None: 
        result.innerHTML = "❌ An unexpected error occurred." #if the value is absent or null then this condition will happen
        result.style.color = "red"
        return

    if Username.value.strip() == "" or Password.value.strip() == "": #if there is nothing inputted in the input slots, this will happen
        result.innerHTML = "❌ Please fill in all fields."
        result.style.color = "red"
        return

    result.innerHTML = f""" ✅ Account created. You may now log in using your credentials, {Username.value}.""" #if both inputs are filled out, the following will play out
    result.style.color = "green"


window.signUp = signUp # this is so that the button can trigger the signUp function
