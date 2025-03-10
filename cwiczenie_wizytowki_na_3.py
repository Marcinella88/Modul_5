class buissnes_card:
    def __init__(self, name, surname, company, occupation, email_address):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email_address = email_address
        pass
    pass

wizytowka_1 = buissnes_card(name="Eliasz",surname="Nowak", company="GEX",occupation="Payroll and timekeeping clerk",email_address="EliaszNowak@rhyta.com")
wizytowka_2 = buissnes_card(name="Marcelina",surname="Tomaszewska", company="Security Sporting Goods",occupation="Slaughterer",email_address="MarcelinaTomaszewska@teleworm.us")
wizytowka_3 = buissnes_card(name="Gabrysz",surname="Kwiatkowski", company="Pioneer Chicken",occupation="Cutting",email_address="GabryszKwiatkowski@rhyta.com")
wizytowka_4 = buissnes_card(name="Stefcia",surname="Zielinska", company="Lee Wards",occupation="Gaming surveillance officer",email_address="StefciaZielinska@dayrep.com")
wizytowka_5 = buissnes_card(name="Maryla",surname="Sawicka", company="Integra Design",occupation="New accounts clerk",email_address="MarylaSawicka@rhyta.com")

wizytowki_all = (wizytowka_1,wizytowka_2,wizytowka_3,wizytowka_4,wizytowka_5)

by_name = sorted(wizytowki_all, key=lambda buissnes: buissnes.name)
by_surname = sorted(wizytowki_all, key=lambda buissnes: buissnes.surname)
by_email = sorted(wizytowki_all, key=lambda buissnes: buissnes.email_address)

print("Według imienia:")
for dane in by_name:
    print(dane.name, dane.surname, dane.email_address)

print("Według nazwiska:")
for dane in by_surname:
    print(dane.name, dane.surname, dane.email_address)

print("Według email:")
for dane in by_email:
    print(dane.name, dane.surname, dane.email_address)