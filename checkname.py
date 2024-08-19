import random
import os


last_name = ["JPG", "BMP", "GIF"," PNG", "PSD", "TIFF", "RAW", "HEIF","JFIF"
           ]

def check_extention(attachment):
    attachment = attachment.split(".")
    for name in last_name:
        if attachment[-1] == name.lower() :
            return True
     
List = [
    "1.Elektrownia jądrowa, nazywana elektrownią atomową – obiekt przemysłowo-energetyczny , wytwarzający energię elektryczną poprzez wykorzystanie energii pochodzącej z rozszczepienia jąder atomów.",
    "2.Elektrownia słoneczna – zespół urządzeń przekształcających energię promieniowania słonecznego zaliczaną do odnawialnych źródeł energii, na energię użytkową: cieplną lub elektryczną.",
    "3.Elektrownia wodna – zakład przemysłowy zamieniający energię potencjalną wody na elektryczną.",
    "4.Elektrownia wiatrowa – elektrownia wytwarzająca energię elektryczną przy pomocy generatorów (turbin wiatrowych) napędzanych energią wiatru",
    "5.Elektrownia szczytowo-pompowa (ESP) – zakład przemysłowy, którego zadaniem jest przemiana energii elektrycznej w energię grawitacyjną wody pompowanej do górnego zbiornika oraz proces odwrotny.",
    "6.Baterie grawitacyjne - Przechowywuje energię elektryczną, Zazwyczaj są w postaci wielkiego dźwigu z obciążnikami rzadziej występują w starych kopalniach ",
    "7.Odnawialne źródła energii – źródła energii, których wykorzystywanie nie wiąże się z długotrwałym ich deficytem, ponieważ ich zasób odnawia się w relatywnie krótkim czasie",
    "8.nieodnawialne źródła energii, czyli źródła, których zasoby odtwarzają się bardzo powoli bądź wcale: ropa naftowa, węgiel, gaz ziemny i uran pozyskiwany z kopalin.",
    "9.TU BĘDZIE LINK DO QUIZU"







]


def Random_Question():
    random.shuffle(List)

    return List[1]

        

level1 = {
        'Co oznacz skrót ESP?' : 'elektrownia szczytowo-pompowa',
        'Jak nazywamy : źródła energii, których wykorzystywanie nie wiąże się z długotrwałym ich deficytem, ponieważ ich zasób odnawia się w relatywnie krótkim czasie' : 'odnawialene źródła energi'






}

def Quiz():
    levelend = level1.keys()
    x = random.randint(0,1)
    levelland = list(levelend)
    return {levelland[x]}
    
print(Quiz())
    
# def Answering(answer):    
#     levelend = level1.keys()
#     levelland = list(levelend)
#     if answer == level1[levelland[0]]:
#          botanswer = "Gratulacje zdobyłeś 1 punkt"
#          return botanswer
#     else :
#          botanswer = "Zła odpowiedź"








