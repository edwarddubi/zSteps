# zSteps (Discord Bot)
**Take steps before others to attain an object**

Participants would decide on an object they would like to own for themselves. They become players and would compete against themselves. Each player would take random steps between 0-10 (excluding 0 and 10). Before the game begins, the players would decide on the total number of steps needed to take to get to the destination, where the object is located at as well as the object's name. The winner is determined if a player has accumulated the exact or more steps specified by all the players. Tie players would need a rematch (start a new game) until one person wins.
### Note
The object would be given to the winner at the end of the game.

## Rules of the zSteps Game
 - Players should type "play" to be added to the game.
 - Anyone can type "start, n, x" when all participating players have joined. The "n" is the number of steps to be taken by each player to reach the location the object is located at; also, the "x" is the name of the object to be attained by a player. For example, "start, 100, crown".
 - If no steps are specified, the default steps to be taken is a 100. Also, if no object is specified, the default object would be a Crown.
 - To start playing, type "takeStep, y" where "y" represents your previous step(s). In the beginning, since no one has a step count, each player would start with a 0 e.g "takeStep, 0".
 - Players would be penalized by taking 5 steps back if they do not obey rule no.4.
 - The steps made by a player would be a number between 0-10; thus, players must type as fast as they can.
 - This is not a turn based game, but measures how fast a player can gain steps to reach their destination.- The winner is determined when a player has the exact or more "n" steps.

## Init Game on Discord
 - **init zsteps**
## Start Game on Discord
 - **start, 100, pizza**, where 100 is the step count and the pizza is the object to be attained by one player out of all the players

 ## Quit?
 - Type **quit** or **exit**


## Dependencies
 - py -3 -m pip install -U discord.py