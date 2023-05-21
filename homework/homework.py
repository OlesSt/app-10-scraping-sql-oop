class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


if __name__ == "__main__":
    new_user = User("jack", 1992)
    print(new_user.age(2023))
    print(new_user.get_name())
