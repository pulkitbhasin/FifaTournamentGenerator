import _pickle as cPickle
from tabulate import tabulate

class Tournament:

    def __init__(self, players):
        self.table = players
        self.players = {}

        for player in players:
            self.players[player.name] = player

        schedule = {}

        numPlayers = len(players) 
        weekNum = 1
        top = list(range(numPlayers//2))
        bottom = list(range(numPlayers - 1, numPlayers//2 - 1, -1))
        while weekNum < numPlayers:
            index = 0
            weekSchedule = "Week " + str(weekNum) + " Schedule\n"
            while index < numPlayers//2:
                weekSchedule = weekSchedule + players[top[index]].getName() + " vs " + players[bottom[index]].getName() + "\n"
                index += 1
            lastTop = top[-1]
            for topIndex in range(numPlayers//2 - 1, 2, -1):
                top[topIndex] = top[topIndex-1]
            top[-1] = bottom[0]
            for bottomIndex in range(numPlayers//2 - 1):
                bottom[bottomIndex] = bottom[bottomIndex + 1]
            bottom[-1] = lastTop
            weekSchedule += "\n"
            schedule[weekNum] = weekSchedule
            weekNum+=1

        self.schedule = schedule
        self.currentWeek = 1
        self.writeTournamentToFile()

    def displayFullRemainingSchedule(self):
        if self.currentWeek == len(self.schedule) + 1:
            print("Tournament Over. The winner is " + self.table[0].getName())
        else:
            for weekNum in range(self.currentWeek, len(self.schedule) + 1):
                print(self.schedule[weekNum])
    
    def displayWeekSchedule(self, weekNum):
        if type(weekNum) != int or weekNum > len(self.schedule) or weekNum < 1:
            print("Invalid Week Number. Please try again.")
        else:
            print(self.schedule[weekNum])
    
    def updateWeeklyResults(self):
        if self.currentWeek > len(self.schedule):
            print("Tournament Over. The winner is " + self.table[0].getName())
        else:
            print("Update results for week " + str(self.currentWeek))
            matches = self.schedule[self.currentWeek].splitlines()[1:-1]
            for match in matches:
                print(match)
                player1 = match.split()[0]
                player2 = match.split()[-1]
                player1Score = int(input("Enter number of goals scored by " + player1 + ": "))
                player2Score = int(input("Enter number of goals scored by " + player2 + ": "))
                player1obj = self.players[player1]
                player2obj = self.players[player2]
                player1obj.incrementGoalsScored(player1Score)
                player1obj.incrementGoalsConceded(player2Score)
                player1obj.incrementGoalDifference()
                player2obj.incrementGoalsScored(player2Score)
                player2obj.incrementGoalsConceded(player1Score)
                player2obj.incrementGoalDifference()
                if player1Score > player2Score:
                    player1obj.incrementWins()
                    player2obj.incrementLosses()
                elif player1Score < player2Score:
                    player2obj.incrementWins()
                    player1obj.incrementLosses()
                else:
                    player1obj.incrementDraws()
                    player2obj.incrementDraws()
            self.table = sorted(self.table, key = lambda x: (x.getPoints(), x.getGoalDifference(), x.getGoalsScored()), reverse = True)
            self.currentWeek += 1
            self.displayTable()
            self.writeTournamentToFile()
    
    def displayTable(self):
        table = []
        for row in self.table:
            table.append(row.getPlayerData())
        print(tabulate(table, headers = ["Name", "Points", "Wins", "Draws", "Losses", "Goals Scored", "Goals Against", "Goal Difference"]))

    def writeTournamentToFile(self):
        with open(r"tournament.pickle", "wb") as tournament_file:
            cPickle.dump(self, tournament_file)
    