import constants

nombre_de_personne = constants.personne


class PersonneModel:
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"Bonjour à tous je m'appelle " \
               f"{self.first_name} {self.last_name}."


class PersonneController:
    @staticmethod
    def create_personne():
        first_name, last_name = PersonneView.get_information_personne()
        personne = PersonneModel(first_name, last_name)
        return personne


class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("Quel est votre prénom? ")
        last_name: str = input("Précisez votre nom de famille: ")
        return first_name.capitalize(), last_name.capitalize()
    
    @staticmethod
    def add_personne():
        new_personne = input(
            "Voulez-vous saisir une nouvel personne Y/N? ")
        new_personne.upper()
        if new_personne == "Y":
            PersonneView.get_information_personne()
        else:
            new_personne = False
            if not new_personne:
                pass


if __name__ == '__main__':
    """Main"""
personnes = []
liste_personne = len(personnes)
for i in range(nombre_de_personne):
    personne = PersonneController.create_personne()
    PersonneView.add_personne()
    personnes.append(personne)

for i in range(len(personnes)):
    print(personnes[i])

for i in personnes:
    print(i.first_name, i.last_name)

"""Rajouter un menu ou la personne à le choix 1 rajouter un player, 2,
lister les players, 3 supprimer un player."""