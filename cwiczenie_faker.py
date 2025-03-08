from faker import Faker

fake = Faker()


class BusinessCard:
    def __init__(self, name, surname, company, occupation, email_address):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email_address = email_address
        pass
    pass


wizytowki_all = [
    BusinessCard(name=fake.first_name(),
                 surname=fake.last_name(), 
                 company=fake.company(),
                 occupation=fake.job(), 
                 email_address=fake.email())
    for i in range(10)
]

for wizytowka in wizytowki_all:
    print(wizytowka.name, wizytowka.surname, wizytowka.email_address)

print(type(wizytowki_all))