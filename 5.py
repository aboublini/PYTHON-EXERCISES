f = open("file.txt", "r") #anoigma arxeiou
txt = f.read() #apothikeusi arxeiou se metabliti txt tipou string
#bgazw ta simeia stiksis apo to keimeno
txt = txt.replace('.', '')
txt = txt.replace(',', '')
txt = txt.replace(':', '')
arrayfile = txt.split() #apothikeusi kathe leksis tou arxeiou se enan array
for word in arrayfile: #elegxw kathe leksi me for loop
    if len(word) > 3: #an i leksi exei mikos panw apo 3xaraktires
        prwtogramma = word[0] #kratw to prwto gramma
        word = word[1:] #afairw to prwto gramma
        word = word + prwtogramma + "ay" #prosthetw to prwto gramma kai to 'ay'
    print(word) #output i leksi
f.close() #kleisimo arxeiou