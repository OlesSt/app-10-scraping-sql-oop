class Guitar:
    def __init__(self, model, form, year):
        self.model = model
        self.form = form
        self.year = year


class Wood:
    def __init__(self, wood_type, year):
        self.wood = wood_type
        self.year = year


class Picks:
    def __init__(self, type, model):
        self.type = type
        self.model = model


class MyGuitar(Guitar):
    def __init__(self, model, form, year):
        super().__init__(model, form, year)
        self.wood = Wood('mahagon', 2000)
        self.picks = Picks('hamb', 'e342')


my_guitar = MyGuitar('gibson', 'sg', '2005')

print(my_guitar.form)
print(my_guitar.model)
print(my_guitar.year)
print(my_guitar.picks.type)
print(my_guitar.picks.model)
print(my_guitar.wood.wood)
print(my_guitar.wood.year)
