import datetime #bibliothiki pou dinei tin imerominia tou upologisti
nowdate = datetime.datetime.now() #imerominia tou upologisti
date = input("Dwse tin imerominia: ") #imerominia pou dinei o xristis
imerominies = date.split("/")  # bazw tin imerominia se array
#xwrizw tin imerominia se xrono, mina, mera
xronosxristi = imerominies[2]
minasxristi = imerominies[1]
imeromaxristi = imerominies[0]
#metatrepw to array me tin xwrismeni imerominia se datetime
datexristi = datetime.datetime(int(xronosxristi),int(minasxristi),int(imeromaxristi))
diafora = datexristi - nowdate #afairw tin mia imerominia apo tin alli
print("Hmerominia pou dwthike: ", datexristi)
print("Simerini imerominia: ", nowdate)
diafmeres = abs(diafora.days)#briskw tis meres pou apexei i imerominia apo tin imerominia pou edwse o xristis
diafhours = diafmeres * 24 #metatropi diaforas se wres
diafseconds = diafmeres * 86400 #metatropi diaforas se deuterolepta
print("H imerominia pou edwses apexei " + str(diafmeres) + " meres, diladi " + str(diafhours)
      + " wres, diladi " + str(diafseconds) + " deuterolepta apo tin simerini.") #output ta apotelesmata
#briskw poses meres exei o minas pou dothike apo ton xristi
if int(minasxristi) == 2:
    print ("O minas pou edwses exei 28 meres.")
elif (int(minasxristi) % 2) == 0:
    print ("O minas pou edwses exei 30 meres.")
else:
    print ("O minas pou edwses exei 31 meres.")
