import string
from tinydb import TinyDB, where, table
from typing import List


class Player:
    db = TinyDB(f"data/players.json", indent=4)
    players = db.table('players')

    def __init__(self, first_name: str, last_name: str, birthday: str = None, gender: str = None, ranking: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
    
    def __repr__(self):
        return f"Player: {self.first_name} {self.last_name} is register."
    
    def __str__(self):
        return f"{self.full_name}\n{self.birthday}\n{self.gender}\n" \
               f"{self.ranking}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self) -> table.Document:
        return Player.db.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))
    
    def _checks(self):
        self._check_names()
    
    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("First and last name cannot be blank.")
        
        special_characters = string.punctuation + string.digits
        
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Invalid name {self.full_name}.")
    
    def exists(self):
        return bool(self.db_instance)
    
    def delete(self) -> List[int]:
        if self.exists():
            return Player.db.remove(doc_ids=[self.db_instance.doc_id])
        return []
    
    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()
        
        if self.exists():
            return -1
        else:
            return Player.db.insert(self.__dict__)

if __name__ == "__main__":
    player = Player(first_name="Tierno",
                    last_name="Thiam",
                    birthday="29031993",
                    gender="M",
                    ranking=7)
    print(player.save())
    print(repr(player))
    print(player)

    player._checks()
    laurent = Player("Laurent", "Jouron")
    print(player.db_instance)

    print(laurent.exists())

    laurent.delete()

def get_all_users():
    return [Player(**player) for player in Player.db.all()]
print(get_all_users())

print(player.full_name)
