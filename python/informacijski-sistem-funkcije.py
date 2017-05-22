class Shramba:

    def narocilo(zivilo, kolicina):
        pomnozen = {}
        for kljuc in zivilo:
            pomnozen[kljuc] = zivilo[kljuc] * kolicina
        return pomnozen

    def vrni_zivilo(niz):
        rezultat = []
        niz.split(",")
        for x in niz.split(","):
            rezultat.append(int(x))
        return rezultat

    def dnevna_poraba(ime_vhodne, ime_izhodne):
        with open(ime_vhodne) as f:
            with open(ime_izhodne, "w") as g:
                for vrstica in f:
                    danasnje_kalorije = vrni_kalorije(vrstica.strip())
                    

    def povprecna_poraba(ime_vhodne, ime_izhodne):
        with open(ime_vhodne) as f:
            with open(ime_izhodne, "w") as g:
                stevilka_dneva = 1
                kalorije_po_dnevih = []
                for vrstica in f:
                    danasnje_kalorije = vrni_kalorije(vrstica.strip())
                    danasnje_povprecje = sum(danasnje_kalorije)/len(danasnje_kalorije)
                    kalorije_po_dnevih.append(sum(danasnje_kalorije))
                    podatek = "{} {:.2f}".format(stevilka_dneva, danasnje_povprecje)
                    print(podatek, file=g)
                    stevilka_dneva += 1
                povprecje_po_dnevih = sum(kalorije_po_dnevih)/len(kalorije_po_dnevih)
                print("{:.2f}".format(povprecje_po_dnevih), file = g)

    def zaloga(zivilo, kolicina):
        for sestavina in zivilo:
            if zivilo[sestavina] > kolicina.get(sestavina, 0):
                return False
        return True 

    def opozori(zivilo, zaloga):
        dokup = {}
        for sestavina, vrednost in zivilo.items():
            na_zalogi = zaloga.get(sestavina, 0)
            if vrednost > na_zalogi:
                dokup[sestavina] = vrednost - na_zalogi
                print ('Pozor, necesa primanjkuje!')
        return dokup


