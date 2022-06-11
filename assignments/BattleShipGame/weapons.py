"""
 class definitions specific to Battle related instruments
"""


class BattleShip(object):
    """ class definition for ship management"""

    def __init__(self, ship_type, ship_size, pos):
        """Initialize a new battle ship
                using ship type, position and specified sizes """
        self._type = ship_type or 'P'
        pos_x1, pos_y1 = ord(pos[0]), int(pos[1])
        size_x, size_y = int(ship_size[1]), int(ship_size[0])
        pos_x2, pos_y2 = pos_x1 + size_x, pos_y1 + size_y

        # Initialize the battleship cells
        self._cells = []
        for temp_x in range(pos_x1, pos_x2):
            for temp_y in range(pos_y1, pos_y2):
                if self._type == 'P':
                    self._cells.append((chr(temp_x), temp_y))
                else:
                    self._cells.extend([(chr(temp_x), temp_y), (chr(temp_x), temp_y)])

    def hit_me(self, hit_pos):
        """ Check if the given pos hits the battle cell"""
        if hit_pos in self._cells:
            self._cells.remove(hit_pos)
            return True
        return False

    def destroy_me(self):
        """ Check if the ship is to be destroyed
        ship is destroyed only after all the cells are damaged
        :return: returns if ship is destroyable """
        if len(self._cells):
            return False
        else:
            return True


class Missile(object):
    """ class definition for Missile management"""

    def __init__(self, pos):
        """ Initialize the missile with its target"""
        self._target = pos[0], int(pos[1])

    def get_target(self):
        """
        Read the missile target
        :return:  target of given missile
        """
        return self._target
