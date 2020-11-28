from Country import Country
from Vaccine import  Vaccine
import random

class CovidGame:
    def __init__(self):

        self.playing = True
        self.vaccineList = list()
        self.countryInfectedList = list()
        self.countryCuredList = list()
        self.countryList = list()
        self.countryCuredStr = ""

        self.numVaccine = 3
        self.numCountry = 5
        self.numCountryInfected = 5
        self.numCountryCured = 0
        self.totalInfectIncrease = 0
        self.totalCured = 0

        self.gameSetting()
        self.main()

    #set game
    def gameSetting(self):

        self.vaccineList = list()
        self.countryInfectedList = list()
        self.countryCuredList = list()
        self.countryList = list()
        self.countryCuredStr = ""
        self.numVaccine = 3
        self.numCountry = 5
        self.numCountryInfected = 5
        self.numCountryCured = 0
        self.totalInfectIncrease = 0
        self.totalCured = 0

        southKorea = Country("South Korea", 1500, 300)
        china = Country("China", 3000, 800)
        japan = Country("Japan", 2000, 500)
        US = Country("US", 2500, 750)
        germany = Country("Germany", 2200, 1000)
        self.countryInfectedList.append(southKorea)
        self.countryInfectedList.append(china)
        self.countryInfectedList.append(japan)
        self.countryInfectedList.append(US)
        self.countryInfectedList.append(germany)
        self.countryList = self.countryInfectedList

        vac1 = Vaccine("vaccine 1", 25.0)
        vac2 = Vaccine("vaccine 2", 50.0)
        vac3 = Vaccine("vaccine 3", 100.0)
        self.vaccineList.append(vac1)
        self.vaccineList.append(vac2)
        self.vaccineList.append(vac3)

    #main gain execution
    def main(self):
        while(self.playing):
            print("----------------------------------")
            print("코로나 종식 게임")
            print("----------------------------------")
            print("1. 백신 정보")
            print("2. 감염된 국가 정보")
            print("3. 게임 시작")
            print("4. 게임 종료")
            userInput = input()
            self.gameInput(userInput)
            self.gameSetting()

    #get user input
    def gameInput(self, input):
        switcher = {
            "1": self.vaccineInfo,
            "2": self.countryInfo,
            "3": self.startGame,
            "4": self.quitGame,
        }.get(input, self.invalidInput)()

    def vaccineInfo(self):
        for vaccine in self.vaccineList:
            print(vaccine.returnInfo())

    def countryInfo(self):
        for country in self.countryList:
            print(country.returnInfo())

    def startGame(self):
        print("사용할 백식(1-3)과 백신을 적용할 국가(1-5)의 번호를 자례대로 입력하세요")
        userInput = input()
        userInput = [ i for i in userInput.split(" ")]
        if(self.processInput(userInput)):
            self.gameResult()
        else:
            print("Invalid Vaccine Number/ Country Number")

    def quitGame(self):
        print("Quit Game")
        self.playing = False

    def invalidInput(self):
        print("Invalid Command/Number")

    #process input when user input is valid
    def processInput(self, inputList):

        #Check user input to make sure we get int type as inputs. If not, ask for input again.
        if(len(inputList) == 2):
            try:
                inputList = [int(i) for i in inputList]
            except ValueError:
                pass
            if(isinstance(inputList[0], int) and isinstance(inputList[1], int)):
                if((inputList[0] <= 0) or (inputList[0] > self.numVaccine)
                        or (inputList[1] <= 0) or (inputList[1] > self.numCountryInfected)):
                    return False
            else:
                return False
        else:
            return False
        vacNum = inputList[0]-1
        countryNum = inputList[1]-1
        i = 1
        while(True):
            vaccine = self.vaccineList[vacNum]
            country = self.countryInfectedList[countryNum]

            print(i, "번째 시도.")
            print("선택된 백신: ", vaccine.returnInfo())
            print("선택된", country.returnInfo())
            self.applyCure(vaccine, country)
            self.checkCured()
            self.printResult(i)

            if(i >= 5):
                break

            self.infectedIncrease()
            if (self.checkFinished()):
                return True

            #get random number
            vacNum = random.randint(0, self.numVaccine-1)
            countryNum = random.randint(0, self.numCountryInfected-1)
            i += 1
        return True

    #Apply vaccine to selected country
    def applyCure(self, selectedVaccine, selectedCountry):
        self.totalCured += selectedCountry.applyCure(selectedVaccine.getCureRate())

    #print result of the round
    def printResult(self, i):
        print("============================================")
        if(self.numCountryCured):
            print("완치된 나라: " + self.countryCuredStr)
        print(i, "차 백신 투여 후 감염된 나라에 대한 정보")
        print("============================================")
        for i in range(0, self.numCountryInfected):
            print(self.countryInfectedList[i].returnInfo())

    #check cured country and update country lists
    def checkCured(self):
        for country in self.countryInfectedList:
            if(country.cured()):
                self.countryCuredList.append(country)
                self.countryCuredStr += country.getName() + ' ';
                self.numCountryCured += 1

        self.countryInfectedList = [x for x in self.countryInfectedList if not x.cured()]
        self.numCountryInfected = len(self.countryInfectedList)

    #Quit game if all country is cured or numInfect > population
    def checkFinished(self):
        if(len(self.countryInfectedList) == 0):
            return True

        for i in range(0, self.numCountryInfected):
            if(self.countryInfectedList[i].checkMoreInfected()):
                print("감염자 수가 인구 수보다 많은 국가가 발생했습니다 게임을 중단합니다!")
                return True
        return False;

    #Increment number of infected each round
    def infectedIncrease(self):
        for i in range(0, self.numCountryInfected):
            self.totalInfectIncrease += self.countryInfectedList[i].infectedIncrease()

    #Print game result
    def gameResult(self):
        print("============================================")
        print("Result")
        print("============================================")
        print("라운드마다 추가로 감염된 수: {}".format(self.totalInfectIncrease))
        print("백신으로 치료된 감염자 수: {}".format(self.totalCured))
        print("백신으로 완치된 국가: {} ({}개)".format(self.countryCuredStr, self.numCountryCured))
        self.countryList.sort(key=lambda x: x.getInfectNum(), reverse = True)
        n = 1
        for country in self.countryList:
            print("{}위".format(n))
            print(country.returnInfo())
            n += 1

a = CovidGame()
