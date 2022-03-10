import constants

nombre_de_personne = constants.personne


class PersonneModel:
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"Bonjour à tous je m'appelle " \
               f"{self.first_name} {self.last_name}.\n"


class PersonneController:
    @staticmethod
    def create_personne():
        first_name, last_name = PersonneView.get_information_personne()
        personne = PersonneModel(first_name, last_name)
        return personne


class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("Quel est votre prénom ? ")
        last_name: str = input("Précisez votre nom de famille : ")
        return first_name.capitalize(), last_name.capitalize()


if __name__ == '__main__':
    """Main"""
personnes = []

while True:
    action = input("1 ajouter , 2 afficher, 3 supprimer : ")
    if action == "1":
        if len(personnes) >= nombre_de_personne:
            print("Les inscriptions sont terminées.")
        else:
            for i in range(1):
                personne = PersonneController.create_personne()
                personnes.append(personne)
                print(personnes[i])

    elif action == "2":
        for i in personnes:
            print(i.first_name, i.last_name)
    elif action == "3":
        first_name = input("Saisissez le prénom de la personne à supprimer : ")
        personnes.remove(f"{first_name}")
    else:
        action = False
        if not action:
            print("Erreur de saisie")
