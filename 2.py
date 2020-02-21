f = open("file.txt", "r") #anoigma arxeiou
txt = f.read()  # apothikeusi arxeiou se metabliti txt tipou string
#bgazw ta simeia stiksis apo to keimeno
txt = txt.replace('.', '')
txt = txt.replace(',', '')
txt = txt.replace(':', '')
arrayfile = txt.split() #apothikeusi kathe leksis tou arxeiou se enan array
vowels = ['a', 'e', 'i', 'o', 'u']
kaka_simfona = ['f', 'c', 'k', 'r']
for word in arrayfile:
    word = word.lower()  # kanw oles tis lekseis me peza grammata
    sum_simfonwn = 0
    sum_kakwn_simfonwn = 0
    for xaraktiras in word:  # diabazw kathe xaraktira sti leksi
        if xaraktiras not in vowels:  # elegxw an o xaraktiras den anikei sta vowels
            sum_simfonwn =  sum_simfonwn + 1 #an den anikei tote einai simfono kai to metraw
        if xaraktiras in kaka_simfona: # elegxw an o xaraktiras anikei sta kaka simfona
            sum_kakwn_simfonwn = sum_kakwn_simfonwn + 1 #an anikei ton metraw
    kala_simfona = sum_simfonwn - sum_kakwn_simfonwn #briskw posa einai ta kala simfona
    if sum_kakwn_simfonwn > kala_simfona: #apotelesmata
        print("H leksi " + word + " einai kaki, giati exei " + str(sum_kakwn_simfonwn)
              + " kaka simfona, ta opoia einai perissotera apo ta kala simfona: " + str(kala_simfona) + ".")
    else:
        print("H leksi " + word + " einai kali, giati exei " + str(sum_kakwn_simfonwn)
              + " kaka simfona, ta opoia einai ligotera apo ta kala simfona: " + str(kala_simfona) + ".")
f.close() #kleisimo arxeiou

