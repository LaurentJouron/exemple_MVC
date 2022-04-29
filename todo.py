from tinydb import TinyDB, where
from datetime import date


class ToDoModel:
    db = TinyDB("todo.json", indent=4)

    def __init__(self, to_do_date, category, action):
        self.to_do_date = to_do_date
        self.category = category
        self.action = action

    def __str__(self):
        return f"Create date: {self.to_do_date}\n" \
               f"Category: {self.category}\n" \
               f"Action: {self.action}"

    def __repr__(self):
        return f"{self.to_do_date}\n {self.category}\n {self.action}"

    def save(self):
        ToDoModel.db.insert({"Create date:": self.to_do_date,
                             "Category:": self.category,
                             "Action:": self.action})

    @staticmethod
    def get_all():
        return ToDoModel.db

    def delete(self):
        return ToDoModel.db.remove(where("Category:") == self.category)


class ToDoController:
    @staticmethod
    def create():
        to_do_date, category, action = ToDoView.create()
        to_do_list = ToDoModel(to_do_date, category, action)
        to_do_list.save()
        return to_do_list

    @staticmethod
    def get_all():
        list_to_do = []
        to_does = ToDoModel.get_all()
        for to_do in to_does:
            to_do_list = ToDoModel(to_do["Create date:"],
                                   to_do["Category:"],
                                   to_do["Action:"])
            list_to_do.append(to_do_list)
        return ToDoView.display_all(list_to_do)

    @staticmethod
    def delete():
        to_do_date, category, action = ToDoView.delete()
        description = ToDoModel(to_do_date, category, action)
        description.delete()
        return description


class ToDoView:
    @staticmethod
    def create():
        to_do_date = date.today()
        to_do_date = to_do_date.strftime("%A %d %B %Y")
        category: str = input("Select the category: ")
        action: str = input("Write the action of you need to do: ")
        return to_do_date, category, action

    @staticmethod
    def display_all(todo):
        for to_do in todo:
            print(to_do)
    
    @staticmethod
    def delete():
        to_do_date = date.today()
        category: str = input("What category you want deleted? ")
        action: str = input("What action you want delete? ")
        return to_do_date, category, action


if __name__ == '__main__':

    while True:
        """Sentence when opening the game."""
        welcome = " Select: 1-> create  2-> display  3-> delete "
        print(f"\n{welcome.center(90, '-')}")
        description = input("What you want to do ? ")
        if description == "1":
            ToDoController.create()
        if description == "2":
            ToDoController.get_all()
        if description == "3":
            ToDoController.delete()
        else:
            description = False
