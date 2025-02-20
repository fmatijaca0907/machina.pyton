from helper_functions import koord_to_tuple,tuple_to_koord

def legal_top (figura:dict[str,str],cilj : str) -> bool:
    """
    Funkcija koja provjerava dali je potez topa legalan, a pravila koja prati su:
        - Top se može pomicati bilo koji broj slobodnih polja vodoravno ili uspravno.
        - Moze izvrsiti i rosadu sa kraljem.
        - Nije dopusteno ostati na mjestu.
        - Funkcija ne testira mogućnost da se "pojede" protivnička figura. To je potrebno dodati.
        - Funkcija ne mijenja položaj figure, samo javlja je li novi položaj legalan.
    Parameters
    ----------
    figura : dict[str, str]
        Dictionary koji nosi podatke o figuri - boja, tip i mjesto.
    cilj : str
        Šahovski zapis položaja
       Returns
    -------
    bool
        Odgovor je li najavljen potez dopušten
    
    Raises
    ------
    None
    """
    polazište = koord_to_tuple(figura["mjesto"])
    odredište = koord_to_tuple(cilj)

    #Ako se figura krece samo po slovima a ne po brjevima (A1 -> D1)
    if polazište[0] != odredište[0] and polazište[1] == odredište[1]:
        return True
    #Ako se figura krece samo po brojevima a ne po slovima (A1 -> A7)
    if polazište[0] == odredište[0] and polazište[1] != odredište[1]:
        return True
    
    #Ako se figura nije pomaknula
    if polazište == odredište:
        return False
    