from pyscript import display, document

# ===== SKILLS TEST =====
def signin(e):
    document.getElementById('passwordalert').innerHTML = ""

    username = document.getElementById('username').value
    password = document.getElementById('password').value

    if len(username) <= 8:
        display("Your username must have at least 8 characters.", target="passwordalert")
        return

    if password.isalpha():
        display("Your password needs at least 2 numbers.", target="passwordalert")
        return

    if password.isdigit():
        display("Your password must have letters.", target="passwordalert")
        return

    if len(password) <= 12:
        display("Password must be at least 12 characters.", target="passwordalert")
        return

    display("✅ Account has been created. You may now login.", target="passwordalert")


# ===== SEATWORK 2 =====
def checkteam(e):
    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""

    register = document.querySelector('input[name="register"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade").value

    if not register or not medical or grade == "":
        display("⚠️ Please complete all fields.", target="output")
        return

    register = register.value
    medical = medical.value

    if register != "yes":
        display("Please register online first.", target="output")
        return

    if medical != "yes":
        display("No medical clearance no game, secure a medical clearance first please.", target="output")
        return

    if grade == "7":
        display("🎉 Congratulations! Your team is Yellow Tigers.", target="output")
        document.getElementById("image").innerHTML = "<img src='Yellow_Tigers.jpg.jpg.jpg' width='350' height='300'>"

    elif grade == "8":
        display("🎉 Congratulations! Your team is Green Hornets.", target="output")
        document.getElementById("image").innerHTML = "<img src='Green_Hornets.jpg.jpg.jpg' width='350' height='300'>"

    elif grade == "9":
        display("🎉 Congratulations! Your team is Red Bulldogs.", target="output")
        document.getElementById("image").innerHTML = "<img src='Red_Bulldogs.jpg.jpg.jpg' width='350' height='300'>"

    elif grade == "10":
        display("🎉 Congratulations! Your team is Blue Bears.", target="output")
        document.getElementById("image").innerHTML = "<img src='Blue_Bears.jpg.webp.webp.jpg' width='350' height='300'>"

    else:
        display("Invalid grade entered.", target="output")


# ===== PLAYERS LIST (PYTHON LOOP) =====
def show_players(e):
    document.getElementById("players").innerHTML = ""

    players = [
        "Agena",
        "Ala",
        "Baring",
        "Brodhagen",
        "Baylon",
        "Cabatingan",
        "Canete",
        "Dimaculangan",
        "Evangelista",
        "Galang",
        "Garabiles",
        "Gonzales",
        "Jamet",
        "Ledesma",
        "Nacino",
        "Nardo",
        "Oliveros",
        "Olmedo",
        "Ong",
        "Rebadulla",
        "Reyes",
        "Sangreo",
        "Villafuerte",
        "Villegas",
        "Yao",
    ]

    for player in players:

        display(player, target="players")