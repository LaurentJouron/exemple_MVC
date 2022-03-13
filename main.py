from tinydb import TinyDB, Query, where

import constants

nombre_de_personne = constants.personne


class PersonneModel:
    """ In file"""
    name_liste = input("Saisissez le nom de la liste : ") + ".json"
    db = TinyDB(name_liste, indent=4)
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"hello, my name is {self.first_name} {self.last_name}."
    
    @staticmethod
    def add_personne():
        if len(PersonneModel.db) >= nombre_de_personne:
            print("Registration is complete.")
        else:
            personne = PersonneController.create_personne()
            PersonneModel.db.insert({"first_name": personne.first_name,
                                     "last_name": personne.last_name})
            
    @staticmethod
    def display_personne():
        for personne in PersonneModel.db:
            print(personne)

    @staticmethod
    def delete_personne():
        for personne in PersonneModel.db:
            print(personne)
        first_name = input("Enter the first name of the person you want to "
                           "delete: ").capitalize()
        PersonneModel.db.remove(where("first_name") == first_name)


class PersonneController:
    @staticmethod
    def create_personne():
        first_name, last_name = PersonneView.get_information_personne()
        personne = PersonneModel(first_name, last_name)
        return personne


class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("What's your first name ? ")
        last_name: str = input("what's is your last name : ")
        return first_name.capitalize(), last_name.capitalize()


if __name__ == '__main__':
    """Main"""

"""Sentence when opening the game."""
welcome = "Press - 1 to add , 2 to display, 3 for delete"
print(f"\n{welcome.center(90, ' ')}")

while True:
    action = input("You want Add - Display - Delete ? ")
    if action == "1":
        PersonneModel.add_personne()
    elif action == "2":
        PersonneModel.display_personne()
    elif action == "3":
        PersonneModel.delete_personne()
    else:
        action = False
        if not action:
            print("Input error")
