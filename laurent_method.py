import constants

nombre_de_personne = constants.personne


class PersonneModel:
    def __init__(self):
        super(PersonneModel, self).__init__()
        self.players = []

    def add_player(self):
        if player in self.players:
            print("This player is already registered.")
            return False
        self.players.append(player)
        return True

    def delete_player(self):
        if player in self:
            self.remove(player)
            return True
    
    def display_player(self):
        for player in self.players:
            print(f" - {player}")

class PersonneController:
    @staticmethod
    def create_personne():
        player = PersonneView.define_player()
        PersonneModel()

class PersonneView:
    @staticmethod
    def define_player():
        """Define the first-name of participants."""
        while True:
            first_name = input("Please enter the player’s first name: ")\
                .capitalize()
            if not first_name.isalpha():
                print("Invalid first name")

            """Define the last_name of participants."""
            last_name = input("Enter the last name: ").capitalize()
            if not last_name.isalpha():
                print("Invalid name")
            return first_name, last_name


if __name__ == '__laurent_method__':

    player = PersonneView()
    print(player)
