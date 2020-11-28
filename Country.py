#Country class with information
class Country:
    #constructor
    def __init__(self, countryName, population, infectedNum):
        self.name = countryName
        self.population = population
        self.infectedNum = infectedNum

    #getters
    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getInfectNum(self):
        return self.infectedNum

    #Increase infected num every turn
    def infectedIncrease(self):
        numIncrease = self.population * (0.15)
        self.infectedNum += numIncrease
        return numIncrease

    #check whether the infected number is more than the population
    def checkMoreInfected(self):
        if(self.population >= self.infectedNum):
            return False
        else:
            return True

    #Apply selected cure to the country
    def applyCure(self, cureRate):
        curedNum = self.infectedNum * (cureRate / 100)
        self.infectedNum -= curedNum
        return curedNum

    #Check whether the country is cured
    def cured(self):
        return self.infectedNum == 0

    #return information of the country
    def returnInfo(self):
        return "국가: {}\n인구수: {}명\n감염자수: {}명\n".format(self.name, self.population, self.infectedNum)

