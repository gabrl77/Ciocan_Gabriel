import string

Articol_Stire= """  In cadrul unui briefing organizat săptămâna aceasta, Kremlinul a negat că Rusia se amestecă în Moldova. Cu toate acestea, a afirmat că mulţi moldoveni doresc legături bune cu Moscova şi că li se refuză dreptul de a avea presa şi politicienii pe care îi doresc.
Printre cele mai importante figuri pro-Kremlin se numără Ilan Şor, un magnat condamnat în lipsă la închisoare pentru fraudă, care trăieşte în Rusia. Două dintre partidele sale politice au fost interzise sau li s-a interzis să candideze pe motiv de neconstituţionalitate sau de securitate naţională.  """

impartire=len(Articol_Stire)
impartittextla2=impartire//2

impartit_text1=Articol_Stire[:impartittextla2].upper().strip()
impartit_Text2=Articol_Stire[impartittextla2:].strip()

inversattext2=impartit_Text2[::-1]

punctuatie=str.maketrans('', '', string.punctuation)
punctuatietext2=impartit_Text2.translate(punctuatie).capitalize()

print(impartit_text1,punctuatietext2)





