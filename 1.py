f = open("file.txt", "r") #anoigma arxeiou
txt = f.read() #apothikeusi arxeiou se metabliti txt tipou string
arrayfile = txt.split() #apothikeusi kathe leksis tou arxeiou se enan array
arrayfile.sort(key=len)#taksinomisi array me basei to mikos tis kathe leksis
fivelongerwords = arrayfile[-5:] #apothikeusi 5 megaluyervn leksewn se array tipou string
final_array = [] #orizw keno array
vowels = ['a', 'e', 'i', 'o', 'u'] #orizw pinaka me vowels
for word in fivelongerwords:
    word = word.lower() #kanw oles tis lekseis me peza grammata
    for xaraktiras in word: #diabazw kathe xaraktira sti leksi
        if xaraktiras in vowels: #an o xaraktiras einai vowel, to bgazw
            word = word.replace(xaraktiras, "")
    final_array.append(word[::-1]) # bazw tis lekseis antistremenes kai xwris vowels se enan allo pinaka final_array
print(final_array) #tipwnw ton teliko pinaka
f.close() #kleisimo arxeiou