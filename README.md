# :baseball: Baseball Game Simulator


This is an implementation in Python of a simulation of a baseball game. Eventually I'd like to simulate entire seasons but in order to do that, I first need to simulate a single Major League Baseball game. 

  1. At bat

    a) Handed matchups
    b) Start from pitcher perspective
    c) Assume random pitch types to start (Intelligent choice can be added later)
  2. Half inning
  3. Full inning
  4. Full game

 

Each at bat can end in one of the following ways: 
  1. Strikeout (No distinction between called and swinging)
  2. Walk (Includes hit by ball and 4 balls)
  3. Ball in Play

  

If a ball is put in play:
  1. Caught out

    a) Who makes the out (Where the out is made)
  2. Makes it to base (Calculated using players OBP)

    b) What players are involved in the play

  

