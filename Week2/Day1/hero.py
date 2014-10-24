from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):
        Entity.__init__(self, name, health)
        self.nickname = nickname

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

    def __str__(self):
        return 'H'

