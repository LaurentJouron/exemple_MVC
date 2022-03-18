from tinydb import TinyDB, where
from datetime import date


class ToDoModel:
    db = TinyDB("todo.json", indent=4)

    def __init__(self, date, category, action):
        self.date = date
        self.category = category
        self.action = action

    def __str__(self):
        return f"Create date : {self.date}\n" \
               f"Category: {self.category}\n" \
               f"Action à réaliser: {self.action}"

    def save(self):
        ToDoModel.db.insert({"Date": self.date,
                             "Category": self.action,
                             "Action": self.action})

    @staticmethod
    def list_to_do():
        return ToDoModel.db


class ToDoController:
    @staticmethod
    def create():
        date, category, action = ToDoView.create()
        to_do_list = ToDoModel(date, category, action)
        to_do_list.save()
        return to_do_list

    @staticmethod
    def get_all():
        list_to_do = []
        to_do_list = ToDoModel.list_to_do()
        for to_do in to_do_list:
            to_do_model = ToDoModel(to_do["Date"], to_do["Category"], to_do["Action"])
            list_to_do.append(to_do_model)
        return ToDoView.display_all(list_to_do)


class ToDoView:
    @staticmethod
    def create():
        date.today()
        category: str = input("Select the category: ")
        action: str = input("Write the action of you need to do: ")
        return date, category, action

    @staticmethod
    def display_all(to_do_list):
        for to_do in to_do_list:
            print(to_do)


if __name__ == '__main__':

    while True:
        """Sentence when opening the game."""
        welcome = " Select: 1-> create  2-> display  3-> delete "
        print(f"\n{welcome.center(90, '-')}\n")
        description = input("What you want to do ? ")
        if description == "1":
            ToDoController.create()
        else:
            description = False
            if not description:
                print("Input error")
