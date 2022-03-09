import constants

nombre_de_personne = constants.personne


class PersonneModel:
    def __init__(self):
        super().__init__()
        self.player_list_name = []
    
    def add_player(self):
        if not isinstance(player, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de"
                             "caractères!")
        if player in self:
            assert f"{player} est déjà dans la liste."
            return False
        self.append(player)
        return True
    
    def del_player(self):
        if player in self:
            self.remove(player)
            return True
        return False
    
    def display_player(self):
        print(f"Dans la liste {self.name} il y a :")
        for player in self:
            print(f" - {player}")


class PersonneController:
    @staticmethod
    def create_personne():
        player = PersonneView.get_information_personne()
        personne = PersonneModel(player)
        return personne


class PersonneView:
    @staticmethod
    def get_information_personne():
        first_name: str = input("Quel est votre prénom? ")
        PersonneModel.add_player(first_name.capitalize())
        
        last_name: str = input("Précisez votre nom de famille: ")
        PersonneModel.add_player(last_name.capitalize())
        return player.first_name, player.last_name


if __name__ == '__main__':
    player = PersonneController()
    print(player)
    
    """Main"""

"""Rajouter un menu ou la personne à le choix 1 rajouter un player, 2,
lister les players, 3 supprimer un player."""