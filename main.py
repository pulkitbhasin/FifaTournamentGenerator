import random, os
from Objects import Player, Tournament
import _pickle as cPickle

def createTournament(numPlayers, teamSelectionType):
    playerNames = []
    players = []
    for i in range(1, int(numPlayers) + 1):
        playerName = input("Enter name of player " + str(i) + " ")
        playerNames.append(playerName)
    print("")
    while playerNames:
        playerName = random.choice(playerNames)
        playerTeam = input(str(playerName) + " gets to choose a team: ")
        players.append(Player.Player(playerName, playerTeam))
        playerNames.remove(playerName)
    tournament = Tournament.Tournament(players)

def readTournamentFromFile():
    with open(r"tournament.pickle", "rb") as tournament_file:
        tournament = cPickle.load(tournament_file)
    return tournament

if __name__ == '__main__':
    choiceSelected = False
    while not choiceSelected:
        choice = input("Welcome to the FIFA League Generator!\n" +
                        "'Create League' - Create a new FIFA league tournament\n" +
                        "'Display Schedule' - Display the remaining matches scheduled\n" +
                        "'Display Week Schedule' - Display matches scheduled for a particular week\n" +
                        "'Update Week Results' - Enter results for this week's matches \n" +
                        "'Display Table' - Display current Points Table\n" + 
                        "Enter one of the following options without quotes: ")
        if choice == "Create League":
            numPlayers = input("Enter number of players participating in league: ")
            createTournament(numPlayers, "Draw")
            choiceSelected = True
            print("")
        elif choice == "Display Schedule":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.displayFullRemainingSchedule()
                choiceSelected = True
            else:
                print("")
                print("Please create a tournament first")
                print("")
        elif choice == "Display Week Schedule":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                weekNum = input("Enter week number")
                tournament.displayWeekSchedule(weekNum)
                choiceSelected = True
            else:
                print("")
                print("Please create a tournament first")
                print("")
        elif choice == "Update Week Results":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.updateWeeklyResults()
                choiceSelected = True
            else:
                print("")
                print("Please create a tournament first")
                print("")
        elif choice == "Display Table":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.displayTable()
                choiceSelected = True
            else:
                print("")
                print("Please create a tournament first")
                print("")
        else:
            print("Invalid option selected. Please try again.")
    