import string
from tinydb import TinyDB, where, table
from pathlib import Path
from typing import List
from dataclasses import dataclass


@dataclass
class User:
    db = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    players = db.table('players')
    
    first_name: str
    last_name: str
    birthday: str
    gender: str
    ranking: int
    
    def __repr__(self):
        return f"Player: {self.first_name} {self.last_name} is register.)"
    
    def __str__(self):
        return f"{self.full_name}\n{self.birthday}\n{self.gender}\n" \
               f"{self.ranking}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self) -> table.Document:
        return User.db.get((where('first_name') == self.first_name) & (
                    where('last_name') == self.last_name))
    
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
            return User.db.remove(doc_ids=[self.db_instance.doc_id])
        return []
    
    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()
        
        if self.exists():
            return -1
        else:
            return User.db.insert(self.__dict__)


def get_all_users():
    return [User(**user) for user in User.db.all()]


if __name__ == "__main__":
    user = User(first_name="Laurent",
                last_name="Jouron",
                birthday="02061976",
                gender="M",
                ranking=8)
    print(user.save())
    print(repr(user))
    print(user)
    user._checks()
