import random


class Fight:

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def simulate_fight(self):
        hero_attack_first = random.choice([True, False])
        if hero_attack_first:
            print("Your hero attacks first.\n")
        else:
            print("The orc attacks first.\n")

        while self.hero.is_alive() and self.orc.is_alive():
            if hero_attack_first:
                self.__hero_attack()

                if self.orc.is_alive():
                    self.__orc_attack()

            else:
                self.__orc_attack()

                if self.hero.is_alive():
                    self.__hero_attack()

        if self.hero.is_alive():
            print("{} won the fight".format(self.hero.known_as()))
        else:
            print("The orc won")

    def __hero_attack(self):
        damage = self.hero.attack()
        print("Your hero delt {} damage".format(damage))
        self.orc.take_damage(damage)
        print("Orc has {} health".format(self.orc.get_health()))
        print()

    def __orc_attack(self):
        damage = self.orc.attack()
        print("The orc dealt {} damage".format(damage))
        self.hero.take_damage(damage)
        print("Hero's helth is {}".format(self.hero.get_health()))
        print()

