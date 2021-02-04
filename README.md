# Baseball-Game-Simulator


The goal for this project is to generate a method of simulating the outcome of a baseball game utilizing statistics and lineups from teams. The program will generate a final score for the game along with a breakdown of what happens in each inning (write to text file). 

The roadmap is to built it from the inside out:
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
    a) Who makes the out
  2. Makes it to base (Calculated using players OBP)
    b) What players are involved in the play
  
  
