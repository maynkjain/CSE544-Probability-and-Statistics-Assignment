import numpy

def games():
    """
    This function performs 7 games and calculate the wins of each team based on the win probabilities.
    The win probabilities for both the teams are equal (=0.5).

    args: None

    return:
    - [eventA_Occured, eventBA_Occured]
        where,
        eventA_Occured: LAC is 3-1 after 4 games 
        eventBA_Occured: DEN won 4-3 after event A had occured.

    """
    lacWins = 0
    denWins = 0
    eventA_Occured = False
    eventBA_Occured = False
    for i in range (7):
        lacWon = numpy.random.binomial(1, 0.5)
        if (lacWon):
            lacWins = lacWins+1;
        else:
            denWins = denWins + 1;
        
        if (i == 3):
            if (lacWins == 3):
                eventA_Occured = True;

    if (denWins == 4 and eventA_Occured):
        eventBA_Occured = True

    return [eventA_Occured, eventBA_Occured]

def homeGames(homes):
    """
    This function performs 7 games and calculate the wins of each team based on the win probabilities.
    The win probability depends on the list (homes) (0.75 if homeground, 0.25 otherwise).
    
    args:
    - homes: This list tells the home for ith game

    return:
    - [eventA_Occured, eventBA_Occured]
        where,
        eventA_Occured: LAC is 3-1 after 4 games 
        eventBA_Occured: DEN won 4-3 after event A had occured.
        
    """
    lacWins = 0
    denWins = 0
    eventA_Occured = False
    eventBA_Occured = False
    for i in range (7):
        p = 0.75 if homes[i] == "LAC" else 0.25
        lacWon = numpy.random.binomial(1, p)
        if (lacWon):
            lacWins = lacWins+1;
        else:
            denWins = denWins + 1;
        
        if (i == 3):
            if (lacWins == 3):
                eventA_Occured = True;

    if (denWins == 4 and eventA_Occured):
        eventBA_Occured = True

    return [eventA_Occured, eventBA_Occured]

def gamesHelper(N):
    """
    This function runs the 7 games with equal win probability, "N" number of times
    and prints the calculated probabilities.
    This function calls the games() function to calculate the probabilities.

    args:
    - N : it is the number of times the experiment is performed.

    return: None

    """
    eventA_Occurrences = 0
    eventBA_Occurrences = 0
    for i in range(N):
        occurence = games()
        if (occurence[0]):
            eventA_Occurrences = eventA_Occurrences + 1
        
        if (occurence[1]):
            eventBA_Occurrences = eventBA_Occurrences + 1

    
    probA = eventA_Occurrences/N
    probBA = eventBA_Occurrences/N

    print("FOR N = " + str(N) + ", the simulated value for part (a) is " + str(probA))
    print("FOR N = " + str(N) + ", the simulated value for part (c) is " + str(eventBA_Occurrences/eventA_Occurrences))


def homeGamesHelper(N):
    """
    This function runs the 7 games with home-based win probability, "N" number of times
    and prints the calculated probabilities. 
    This function calls the homeGames() function with a list, homes, where home[i] 
    is the home for game i.

    args:
    - N : it is the number of times the experiment is performed.

    return: None

    """
    eventA_Occurrences = 0
    eventBA_Occurrences = 0

    homes = ["LAC", "LAC", "DEN", "DEN", "LAC", "DEN", "LAC"]
    for i in range(N):
        occurence = homeGames(homes)
        if (occurence[0]):
            eventA_Occurrences = eventA_Occurrences + 1
        
        if (occurence[1]):
            eventBA_Occurrences = eventBA_Occurrences + 1

    
    probA = eventA_Occurrences/N
    probBA = eventBA_Occurrences/N

    print("FOR N = " + str(N) + ", the simulated value for part (e) is " + str(eventBA_Occurrences/eventA_Occurrences))

if __name__ == "__main__":
    """
    This function is the driver for performing the experiments.
    It iterates over n (=3,4,5,6,7) to call the below helper functions which
    repeat the experiments for N ( = 10^n) times and print the probabilities: 

    1. 7 games with equal win probability (N times) - gamesHelper()
    2. 7 games with home based win probability (N times) - homeGamesHelper()

    """
    for n in range(3, 8):
        print ("Calculating... \n")
        N = pow(10, n)
        gamesHelper(N)
        homeGamesHelper(N)
        print("\n")
        