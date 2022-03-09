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
        for play in self.players:
            print(f" - {play}")


class PersonneController:
    @staticmethod
    def create_personne():
        player = PersonneView.get_all_information()
        PersonneModel(player)
        return player

class PersonneView:
    @staticmethod
    def define_first_name():
        """Define the first-name of participants."""
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                print("Invalid first name")
            return first_name.capitalize()

    @staticmethod
    def define_last_name():
        """Define the last_name of participants."""
        while True:
            last_name = input("Enter the last name: ")
            if not last_name.isalpha():
                print("Invalid name")
            return last_name.capitalize()

    def get_all_information(self):
        first_name = self.define_first_name()
        last_name = self.define_last_name()
        return first_name, last_name


if __name__ == '__laurent_method__':

    player = PersonneView()
    print(player)
