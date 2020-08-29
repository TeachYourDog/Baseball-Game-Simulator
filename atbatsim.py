import random


#Hitter, Pitcher and League probability of strikeouts
hitodds=.230
pitchodds=.60
leagueodds=.50


#Determines whether or not a strikeout occurs
def atbat():
    ks=0
    abodds=hitodds*(pitchodds/leagueodds)
    for i in range(1000):
        if random.random() <= abodds:
            ks += 1
        return ks


#simulates at bats n number of times, returning probability of strikeout
def simulate(n):
    trials=[]
    for i in range(n):
        trials.append(atbat())
    return(sum(trials)/n)



print(simulate(10000))
