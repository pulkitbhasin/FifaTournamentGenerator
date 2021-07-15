class Player:

    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goalsScored = 0
        self.goalsConceded = 0
        self.goalDifference =  0
        self.points = 0
    
    def incrementWins(self):
        self.wins += 1
        self.points += 3
    
    def incrementDraws(self):
        self.draws += 1
        self.points += 1

    def incrementLosses(self):
        self.losses += 1
    
    def incrementGoalsScored(self, goalsScored):
        self.goalsScored += goalsScored

    def incrementGoalsConceded(self, goalsConceded):
        self.goalsConceded += goalsConceded

    def incrementGoalDifference(self):
        self.goalDifference = self.goalsScored - self.goalsConceded
    
    def getName(self):
        return self.name
    
    def getPoints(self):
        return self.points
    
    def getGoalDifference(self):
        return self.goalDifference
    
    def getGoalsScored(self):
        return self.goalsScored

    def getPlayerData(self):
        playerData = []
        playerData.append(self.name)
        playerData.append(self.points)
        playerData.append(self.wins)
        playerData.append(self.draws)
        playerData.append(self.losses)
        playerData.append(self.goalsScored)
        playerData.append(self.goalsConceded)
        playerData.append(self.goalDifference)
        return playerData
