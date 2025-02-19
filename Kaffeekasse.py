import datetime

class Kasse:
    def __init__(self):
        self.saldo_in_cent = 0
        self.gesamtverbrauch = 0
        self.bestenliste = {}

    def einzahlung(self, teilnehmer, betrag_in_cent, datum):
        self.saldo_in_cent += betrag_in_cent
        teilnehmer.einzahlungssumme += betrag_in_cent
        teilnehmer.datum_d_letzten_einzahlung = datum
        self.bestenliste_aktualisieren()

    def einkauf(self, anzahl, betrag_in_cent):
        self.saldo_in_cent -= betrag_in_cent
        self.gesamtverbrauch += anzahl

    def bestenliste_aktualisieren(self):
        self.bestenliste = dict(sorted(self.bestenliste.items(), key=lambda item: item[1], reverse=True))


class Teilnehmer:
    def __init__(self, name):
        self.datum_d_letzten_einzahlung = None
        self.name = name
        self.einzahlungssumme = 0

    def tage_seit_letzter_einzahlung(self):
        if self.datum_d_letzten_einzahlung is None:
            return None
        differenz = datetime.date.today() - self.datum_d_letzten_einzahlung
        return differenz.days