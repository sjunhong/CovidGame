class Vaccine:
    def __init__(self, name, cureRate):
        self.name = name
        self.cureRate = cureRate

    #getters
    def getName(self):
        return self.name

    def getCureRate(self):
        return self.cureRate

    def returnInfo(self):
        return  "{}, 치료율: {}%".format(self.name, self.cureRate)