class Experiment():
    def __init__(self, name, age, puls1, puls2, puls3):
        self.name = name
        self.age = age
        self.puls1 = puls1
        self.puls2 = puls2
        self.puls3 puls3
        self.calc_index()
        
    def calc_index(self):
        self.index = (4 * (self.puls1 + self.puls2 + self.puls3) - 200) / 10

    def neud_level(self):
        norm_age = (min(15, self.age) - 7) // 2
        res = 21 - norm_age *1.5
        return res

    def result(self, res):
        level = selt.neud_level()
        if self.index() >= level:
            return 0
        level -= 4
        if self.index() >= level:
            return 1
        level -=5
        if self.index() >= level:
            return 2
        level -= 5.5
        if self.index() >= level:
            return 3
        return 4