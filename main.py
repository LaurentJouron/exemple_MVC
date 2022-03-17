from tinydb import TinyDB, Query, where

import constants

nombre_de_personne = constants.personne


class PersonneModel:
    db = TinyDB("personne.json", indent=4)
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"hello, my name is {self.first_name} {self.last_name}."
    
    def save(self):
        PersonneModel.db.insert({"first_name": self.first_name,
                   "last_name": self.last_name})
        
    @staticmethod
    def get_all():
        return PersonneModel.db
    
    # @staticmethod
    # def display_personne():
    #     for personne in PersonneModel.db:
    #         print(personne)
    
    # @staticmethod
    # def delete_personne():
    #     for personne in PersonneModel.db:
    #         PersonneModel.db.remove(where("first_name") == first_name)
    
    # @staticmethod
    # def delete_data():
    #     db.truncate()


class PersonneController:
    @staticmethod
    def create_personne():
        first_name, last_name = PersonneView.get_information_personne()
        personne = PersonneModel(first_name, last_name)
        personne.save()
        return personne
    
    @staticmethod
    def get_all():
        personnes_model = []
        personnes = PersonneModel.get_all()
        for personne in personnes:
            personne_model = PersonneModel(personne["first_name"], personne["last_name"])
            personnes_model.append(personne_model)
        return PersonneView.display_all(personnes_model)
        

class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("What's your first name ? ").capitalize()
        last_name: str = input("what's is your last name : ").capitalize()
        return first_name, last_name
    
    @staticmethod
    def display_all(personnes):
        for personne in personnes:
            print(personne)

if __name__ == '__main__':
    """Main"""

"""Sentence when opening the game."""
welcome = "1 to add , 2 to display, 3 for delete player, 4 for delete all"
print(f"\n{welcome.center(90, ' ')}")

while True:
    action = input("You want Add - Display - Delete player - delete all ? ")
    if action == "1":
        PersonneController.create_personne()
    elif action == "2":
        PersonneController.get_all()
    # elif action == "3":
    #     PersonneModel.delete_personne()
    # elif action == "4":
    #     PersonneModel.delete_data()
    # else:
    #     action = False
    #     if not action:
    #         print("Input error")

"""
faire une application de todo liste
date
categorie
action/description
"""