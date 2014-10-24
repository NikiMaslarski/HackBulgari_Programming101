class Dungeon:

    def __init__(self, dungeon_for_load):
        self.filename = dungeon_for_load
        self.dungeon_map = open(dungeon_for_load, 'r+')
        self.players = []

    def print_map(self):
        print(self.dungeon_map.read())
        self.dungeon_map.seek(0)

    def spawn(self, player_name, entity):
        dungeon = self.__map_dungeon_to_matrix()
        x_must_be_broken = False
        for i in range(len(dungeon)):
            for ii in range(len(dungeon[i])):
                if dungeon[i][ii] == 'S':
                    entity.coordinates = (i, ii)
                    dungeon[i][ii] = str(entity)
                    x_must_be_broken = True
                    break
            if x_must_be_broken:
                break

        self.players.append((player_name, entity))
        self.__map_matrix_to_dungeon(dungeon)

    def __map_dungeon_to_matrix(self):
        dungeon = self.dungeon_map.read()
        dungeon = dungeon.split('\n')
        self.dungeon_map.seek(0)
        split_dungeon = []
        for line in dungeon:
            split_dungeon.append(list(line))
        return split_dungeon

    def __map_matrix_to_dungeon(self, dungeon):
        result = ''
        for sublist in dungeon:
            for letter in sublist:
                result += letter
            result += '\n'
        self.dungeon_map.write(result)
        self.dungeon_map.seek(0)


