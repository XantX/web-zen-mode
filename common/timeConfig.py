class timeConfig(object):

    """Docstring for timeConfig. """
    initHour = 0
    initMin = 0
    finalHour = 0
    finalMin = 0
    breakTime = 0

    def __init__(self):
        self.initHour = 0
        self.initMin = 0
        self.finalHour = 0
        self.finalMinutes = 0
        self.breakTime = 0

    def setTimes(self, times):

        indexInitTime = times[0].find(" ")
        initTime = times[0][indexInitTime + 1: len(times[0]) - 1]
        self.initHour = int(initTime[0:2])
        self.initMin = int(initTime[3:len(initTime)])

        indexfinishTime = times[1].find(" ")
        finishTime = times[1][indexfinishTime + 1: len(times[1]) - 1]
        self.finalHour = int(finishTime[0:2])
        self.finalMin = int(finishTime[3:len(finishTime)])

# Definir un tiempo de break
