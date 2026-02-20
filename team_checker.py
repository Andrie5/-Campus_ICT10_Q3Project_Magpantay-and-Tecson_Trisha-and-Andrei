from pyscript import document, window
import random

def validateAndCheck(*args): # this is the first function of the main.py and it checks the grade
    result = document.getElementById("result")
    grade_value = document.getElementById("grade").value
    
    if not grade_value: # if theres nothing in the grade input this will run
        result.innerHTML = "❌ Please select your grade level."
        result.style.color = "red"
        return
    
    grade = int(grade_value)
    
    if grade < 7 or grade > 10: # this checks if the grade level is at least 7-10, if not this will run.
        result.innerHTML = "❌ Sorry! You must be Grade 7-10 in order to participate in Intramurals."
        result.style.color = "red"
        return
    
    check_eligibility()

def check_eligibility(*args): # a 2nd function which executes after validateAndCheck
    result = document.getElementById("result")
    reg_el = document.querySelector('input[name="registered"]:checked')
    med_el = document.querySelector('input[name="medical"]:checked')
    section = document.getElementById("section").value.strip()
    grade_value = document.getElementById("grade").value # a bunch of variables so it knows what we are talking about

    if not grade_value: # if theres nothing in the grade level input this will run
        result.innerHTML = "❌ Please enter your grade level."
        result.style.color = "red"
        return

    if not section: #if theres nothing in the section input this will run
        result.innerHTML = "❌ Please enter your section."
        result.style.color = "red"
        return

    grade = int(grade_value) # this makes it so that the grade value will be an integer

    if reg_el.value != "yes": # this checks if the value is yes or not yes, if its not yes, this will run
        result.innerHTML = "❌ Please complete your online registration."
        result.style.color = "red"
        return

    if med_el.value != "yes": # this checks if the value is yes or not yes, if its not yes, this will run
        result.innerHTML = "❌ Please secure a medical clearance."
        result.style.color = "red"
        return

    if grade < 7 or grade > 10: # this checks if the grade level is at least 7-10, if not this will run.
        result.innerHTML = "❌ Only Grades 7–10 may join Intramurals."
        result.style.color = "red"
        return

    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"] # these are the teams it will pick from
    team = random.choice(teams) # this causes the result to be completely random so you won't know what team you will get

    result.innerHTML = f""" 
    Yay! You are eligible!<br>
    Whoa! Your Intramurals Team is <br><br> <b>{team}</b> <br><br> Congrats! 🎉
    """ # this plays out when everything and all the inputs are in order

    if team == "Blue Bears":
        result.style.color = "blue"

    elif team == "Green Hornets":
        result.style.color = "green"

    elif team == "Red Bulldogs":
        result.style.color = "red"

    elif team == "Yellow Tigers":
        result.style.color = "orange" # these are so that the text can be colored in their own team colors

window.check_eligibility = check_eligibility
window.validateAndCheck = validateAndCheck # these codes are so that the functions can run

