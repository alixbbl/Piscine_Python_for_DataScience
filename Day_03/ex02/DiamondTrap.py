from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        self.eyes = new_eyes

    def set_hairs(self, new_hair):
        self.hairs = new_hair

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
