import random, os
from Objects import Player, Tournament
import _pickle as cPickle

def createTournament(numPlayers, teamSelectionType):
    playerNames = []
    players = []
    for i in range(1, numPlayers + 1):
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
    print("\nWelcome to the FIFA League Generator!\n")
    while not choiceSelected:
        choice = input("\n" +
                        "'Create League' - Create a new FIFA league tournament\n" +
                        "'Display Schedule' - Display the remaining matches scheduled\n" +
                        "'Display Week Schedule' - Display matches scheduled for a particular week\n" +
                        "'Update Week Results' - Enter results for this week's matches \n" +
                        "'Display Table' - Display current Points Table\n" + 
                        "'Delete League' - Delete existing league\n" +
                        "'Close Generator' - Close this generator script\n" +
                        "\n"
                        "Enter one of the following options without quotes: ")
        if choice == "Create League":
            print("")
            numPlayers = int(input("Enter number of players participating in league: "))
            while numPlayers%2 == 1:
                numPlayers = int(input("Number of players participating must be even. Please re-enter number of players participating in league: "))
            createTournament(numPlayers, "Draw")
            print("")
        elif choice == "Display Schedule":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.displayFullRemainingSchedule()
            else:
                print("")
                print("Please create a league first")
                print("")
        elif choice == "Display Week Schedule":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                print("")
                weekNum = input("Enter week number")
                print("")
                tournament.displayWeekSchedule(weekNum)
            else:
                print("")
                print("Please create a league first")
                print("")
        elif choice == "Update Week Results":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.updateWeeklyResults()
            else:
                print("")
                print("Please create a league first")
                print("")
        elif choice == "Display Table":
            if os.path.isfile('tournament.pickle'):
                tournament = readTournamentFromFile()
                tournament.displayTable()
            else:
                print("")
                print("Please create a league first")
                print("")
        elif choice == "Delete League":
            if os.path.isfile('tournament.pickle'):
                os.remove('tournament.pickle')
            else:
                print("")
                print("No league exists.")
        elif choice == "Close Generator":
            choiceSelected = True 
        else:
            print("")
            print("Invalid option selected. Please try again.")
    