import random

hitodds=.300
pitchodds=.200
leagueodds=.400



def atbat():
    abodds=hitodds*(pitchodds/leagueodds)
    if random.random() <= abodds:
        return 0
    else:
        return 1

def simulate(n):
    strikeout=[]
    bip=[]
    for i in range(n):
        if atbat() == 0:
            strikeout.append(atbat())
        elif atbat() == 1:
            bip.append(atbat())
    return (sum(strikeout)/n), (sum(bip)/n)


x,y=simulate(10000)

print(x)
print(y)
