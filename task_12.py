from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, value):
        self.__flavor = value

    def is_delicious(self):
        return self.__flavor != "black licorice"