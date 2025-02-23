def input_int(prompt="Unesi cijeli broj"):
    """
    Funkcija uzima input korisnika sve dok ne unese cijeli broj.

    Parameters
    ---------

    Returns
    ------
    Pretvara broj u int(str -> int)
    """
    while True:
        broj = input(prompt)
        if broj.isnumeric():
            broj = int(broj)
            break
    return broj


def prosjek_5_brojeva():
    """Funkcija uzima 5 brojeva i računa njihov prosjek
    Pretvara sve brojeve u listu,te ih dijeli
    

    Parameters
    ------------

    Returns
    ------------
    Float od tih 5 ocjena
    """    
    broj_brojeva = 0
    brojevi = []
    while broj_brojeva < 5: #broj svih brojeva mora biti manji od 5
        broj_brojeva +=1    
        novi_broj = input_int()
        brojevi.append(novi_broj) #dodaje novi broj u listu
    prosjek = sum(brojevi) / len(brojevi) 
    return prosjek