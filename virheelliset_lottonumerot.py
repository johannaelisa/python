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

