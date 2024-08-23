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
    "6.Baterie grawitacyjne - Przechowywują energię elektryczną, Zazwyczaj są w postaci wielkiego dźwigu z obciążnikami rzadziej występują w starych kopalniach ",
    "7.Odnawialne źródła energii – źródła energii, których wykorzystywanie nie wiąże się z długotrwałym ich deficytem, ponieważ ich zasób odnawia się w relatywnie krótkim czasie",
    "8.Nieodnawialne źródła energii, czyli źródła, których zasoby odtwarzają się bardzo powoli bądź wcale: ropa naftowa, węgiel, gaz ziemny i uran pozyskiwany z kopalni.",
    "9.Link dla osób które chciałyby uzupełnić swoją wiedze na temat energi odnawialnej: https://www.eea.europa.eu/pl/sygna142y/sygnaly-2022/artykuly/przyszlosc-oparta-na-energii-odnawialnej"
    "10.Bardzo Interesujący pomysł reaktorów IV generacji: https://pl.wikipedia.org/wiki/Reaktor_post%C4%99puj%C4%85cej_fali"
]




def Random_Question():
    try:
        x = random.choice(List)
        List.remove(x)
        return x
    except :
        return "Brak ciekawostek"
    

questions = {
        '1.Co oznacz skrót ESP?' : 'elektrownia szczytowo-pompowa',
        '2.Jak nazywamy : źródła energii, których wykorzystywanie nie wiąże się z długotrwałym ich deficytem, ponieważ ich zasób odnawia się w relatywnie krótkim czasie' : 'odnawialne źródła energii',
        '3.jaki jest synonim do nazwy elektrownia jądrowa?' : 'elektrownia atomowa',
        '4.czy elektrownie jądrowe są odnawialnym źródłem energi?' : 'Nie , Uran podobnie jak węgiel jest wydobywany z kopalni.',
        '5.Podaj przykład nowoczesnej formy przetrzymywania energi' : 'np. Baterie grawitacyjne',
        '6.Podaj 4 przykłady odnawialnych źródeł energi' : 'np. elektrownia - słoneczna - wiatrowa - wodna - geotermalna'

}

def Quiz():
    keys = questions.keys()
    key = list(keys)
    key = random.choice(key)
    return key
    
def The_End():
    answer = questions
    return answer

def Valut(key):
    return(questions.get(key))    












