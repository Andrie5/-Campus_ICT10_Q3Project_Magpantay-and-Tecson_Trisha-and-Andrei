from pyscript import document, window
import random

def validateAndCheck(*args):
    result = document.getElementById("result")
    grade_value = document.getElementById("grade").value
    
    if not grade_value:
        result.innerHTML = "❌ Please select your grade level."
        result.style.color = "red"
        return
    
    grade = int(grade_value)
    
    if grade < 7 or grade > 10:
        result.innerHTML = "❌ Sorry! You must be Grade 7-10 in order to participate in Intramurals."
        result.style.color = "red"
        return
    
    check_eligibility()

def check_eligibility(*args):
    result = document.getElementById("result")
    
    reg_el = document.querySelector('input[name="registered"]:checked')
    med_el = document.querySelector('input[name="medical"]:checked')
    section = document.getElementById("section").value.strip()
    grade_value = document.getElementById("grade").value

    if not grade_value:
        result.innerHTML = "❌ Please enter your grade level."
        result.style.color = "red"
        return

    if not section:
        result.innerHTML = "❌ Please enter your section."
        result.style.color = "red"
        return

    grade = int(grade_value)

    if reg_el.value != "yes":
        result.innerHTML = "❌ Please complete your online registration."
        result.style.color = "red"
        return

    if med_el.value != "yes":
        result.innerHTML = "❌ Please secure a medical clearance."
        result.style.color = "red"
        return

    if grade < 7 or grade > 10:
        result.innerHTML = "❌ Only Grades 7–10 may join Intramurals."
        result.style.color = "red"
        return

    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]
    team = random.choice(teams)

    result.innerHTML = f"""
    Yay! You are eligible!<br>
    Whoa! Your Intramurals Team is <br><br> <b>{team}</b> <br><br> Congrats! 🎉
    """

    if team == "Blue Bears":
        result.style.color = "blue"

    elif team == "Green Hornets":
        result.style.color = "green"

    elif team == "Red Bulldogs":
        result.style.color = "red"

    elif team == "Yellow Tigers":
        result.style.color = "orange"

window.check_eligibility = check_eligibility
window.validateAndCheck = validateAndCheck
