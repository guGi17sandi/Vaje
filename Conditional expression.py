

starost = 22
naklučna_besedila = ["Kako si danes","Kako živiš?", "Kaj novega?"]

if starost > 18:
    print(random.choice(naklučna_besedila))

elif starost > 0:
    print("You are young")
else:
    print("You arent even born yet lol")
