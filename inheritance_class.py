class User():
    def __init__(self, id, user_name, level):
        self._id = id
        self._user_name = user_name
        self._level = ("user")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._user_name

    def get_access_level(self):
        return self._level

    def set_name(self, user_name):
        self._user_name = user_name
class Admin(User):
    def __init__(self, id, user_name):
        super().__init__(id, user_name)
        self._level = 'admin'
        self._users_list = []
    def add_user(self):
        if isinstance(id, User) and id not in self._users_list:
            self._users_list.append(id)
            print(f"Пользователь '{id.get_name()}' успешно добавлен.")
        else:
            print("Не удалось добавить пользователя.")
    def remove_user(self, id):
        if id in self._users_list:
            self._users_list.remove(id)
            print(f"Пользователь '{id.get_name()}' успешно удален.")
        else:
            print("Пользователь не найден.")




