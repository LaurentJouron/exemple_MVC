from tinydb import TinyDB, where


class PersonneModel:
    db = TinyDB("personne.json", indent=4)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"hello, my name is {self.first_name} {self.last_name}."

    def save(self):
        PersonneModel.db.insert({"first_name": self.first_name,
                                 "last_name": self.last_name})

    @staticmethod
    def get_all():
        return PersonneModel.db

    def delete(self):
        return PersonneModel.db.remove(where("first_name") == self.first_name)


class PersonneController:
    @staticmethod
    def create():
        first_name, last_name = PersonneView.get_information_personne()
        personne = PersonneModel(first_name, last_name)
        personne.save()
        return personne

    @staticmethod
    def get_all():
        personnes_model = []
        personnes = PersonneModel.get_all()
        for personne in personnes:
            personne_model = PersonneModel(personne["first_name"],
                                           personne["last_name"])
            personnes_model.append(personne_model)
        return PersonneView.display_all(personnes_model)

    @staticmethod
    def delete():
        first_name, last_name = PersonneView.delete()
        personne = PersonneModel(first_name, last_name)
        personne.delete()
        return personne


class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("What's the first-name ? ").capitalize()
        last_name: str = input("what's is the last-name : ").capitalize()
        return first_name, last_name

    @staticmethod
    def display_all(personnes):
        for personne in personnes:
            print(personne)

    @staticmethod
    def delete():
        first_name: str = input("Which person first-name you want cancel ? ").capitalize()
        last_name: str = input("Which person last-name you want cancel ? ").capitalize()
        return first_name, last_name


if __name__ == '__main__':
    """Main"""


while True:
    """Sentence when opening the game."""
    welcome = " Select: 1-> Add  2-> display  3-> delete "
    print(f"\n{welcome.center(90, '-')}\n")
    action = input("What you want to do ? ")
    if action == "1":
        PersonneController.create()
    elif action == "2":
        PersonneController.get_all()
    elif action == "3":
        PersonneController.delete()
    else:
        action = False
        if not action:
            print("Input error")
