from tinydb import TinyDB, where
from datetime import date


class ToDoModel:
    db = TinyDB("todo.json", indent=4)

    def __init__(self, to_do_date, category, action):
        self.to_do_date = to_do_date
        self.category = category
        self.action = action

    def __str__(self):
        return f"Create date : {self.to_do_date}\n" \
               f"Category: {self.category}\n" \
               f"Action à réaliser: {self.action}"

    def save(self):
        ToDoModel.db.insert({"Create date": self.to_do_date,
                             "category": self.category,
                             "action": self.action})

    @staticmethod
    def get_all():
        return ToDoModel.db

    def delete(self):
        return ToDoModel.db.remove(where("category") == self.category)


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
        to_do = ToDoModel.get_all()
        for _ in to_do:
            to_do_list = ToDoModel(to_do["date"],
                                   to_do["category"],
                                   to_do["action"])
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
        to_do_date = to_do_date.strftime("%A %d. %B %Y")
        category: str = input("Select the category: ")
        action: str = input("Write the action of you need to do: ")
        return to_do_date, category, action

    @staticmethod
    def display_all(to_do_list):
        for to_do in to_do_list:
            print(to_do)
    
    @staticmethod
    def delete():
        category = input("What category you want deleted ? ")
        return category


if __name__ == '__main__':

    while True:
        """Sentence when opening the game."""
        welcome = " Select: 1-> create  2-> display  3-> delete "
        print(f"\n{welcome.center(90, '-')}\n")
        description = input("What you want to do ? ")
        if description == "1":
            ToDoController.create()
        # if description == "2":
        #     ToDoController.display()
        if description == "3":
            ToDoController.delete()
        else:
            description = False
            if not description:
                print("Input error")