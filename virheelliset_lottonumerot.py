#Ohjelmoinnin perusteet -kurssin tehtävä osa 6, tehtävä 3.3.

#TEHTÄVÄNANTO:
#Tiedostoon lottonumerot.csv on tallennettu lottonumeroita seuraavan esimerkin mukaisesti:
#Esimerkkidata
#viikko 1;5,7,11,13,23,24,30
#viikko 2;9,13,14,24,34,35,37
#...jne...

#Aluksi pitäisi olla siis otsikko viikko x, ja sen jälkeen seitsemän numeroa väliltä 1...39.
#Tiedosto on kuitenkin osittain korruptoitunut. Seuraavat rivit ovat esimerkkejä virheellisistä riveistä (huomaa, että tehtäväpohjassa olevassa tiedostossa ei ole juuri näitä virheitä):

#Viikkonumero pielessä:
#Esimerkkidata: viikko zzc;1,5,13,22,24,25,26

#Numero tai numeroita pielessä:
#Esimerkkidata: viikko 22;1,**,5,6,13,2b,34

#Liian vähän numeroita:
#Esimerkkidata: viikko 13;4,6,17,19,24,33

#Liian pieniä tai suuria numeroita:
#Esimerkkidata viikko 39;5,9,15,35,39,41,105

#Rivissä esiintyy sama numero kahdesti:
#Esimerkkidata viikko 41;5,12,3,35,12,14,36

#Kirjoita funktio suodata_virheelliset(), joka luo tiedoston korjatut_numerot.csv. Tiedostoon on kopioitu kelvolliset rivit alkuperäisestä tiedostosta.



def suodata_virheelliset():
    with open("korjatut_numerot.csv", "w") as tiedosto:
        pass
    with open("lottonumerot.csv", "r") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";") #jaetaan tieto kahtia: viikon nro ja lottonumerot
            viikko = osat[0].split(" ")
            try:
                if viikko[0] != "viikko":
                    continue
                if not viikko[1].isdigit():
                    continue
                viikonnro = int(viikko[1])
                if viikonnro < 1 or 53 < viikonnro:
                    continue
                #tarkistetaan lottonumerot
                lottonumerot = osat[1].strip()
                lottonumerot = lottonumerot.split(",")
                if len(lottonumerot) != 7:
                    continue
                luvut = []
                for luku in lottonumerot:
                    if luku.isdigit():
                        luku = int(luku)
                        if 1 <= luku and luku <= 39:
                            if luku not in luvut:
                                luvut.append(luku)
                if len(luvut) == 7:
                    with open("korjatut_numerot.csv", "a") as tiedosto:
                        tiedosto.write(rivi)
            except ValueError:
                raise ValueError("")
    return "korjatut_numerot.csv"

if __name__ == "__main__":
    suodata_virheelliset()

