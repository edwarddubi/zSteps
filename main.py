import discord
from config import get_bot_token
from model.steps import Steps

client = discord.Client()
init_game_commands = 'init zSteps'
steps = Steps()


@client.event
async def on_ready():
    print("zSteps is online")


@client.event
async def on_message(message):
    command = message.content.lower()
    if command.startswith('init zsteps'):
        if steps.is_awake:
            return await message.channel.send("You can't start a game that has already been started")
        else:
            msg = 'Thanks for waking me up from my slumber.\nRules for the game are:\n1. Players should type "play" to be added to the game.\n2. Anyone can type "start, n, x" when all participating players have joined. The "n" is the number of steps to be taken by each player to reach the location the object is located at; also, the "x" is the name of the object to be attained by a player. For example, "start, 100, crown".\n3. If no steps are specified, the default steps to be taken is a 100. Also, if no object is specified, the default object would be a Crown.\n4. To start playing, type "takeStep, y" where "y" represents your previous step(s). In the beginning, since no one has a step count, each player would start with a 0 e.g "takeStep, 0".\n5. Players would be penalized by taking 5 steps back if they do not obey rule no.4 \n6. The steps made by a player would be a number between 0-10; thus, players must type as fast as they can.\n6. This is not a turn based game, but how fast a player can gain steps to reach their destination.\n7. The winner is determined when a player has the exact or more "n" steps.\n8. Play away!! And test how good your RNG is...haha'
            steps.is_awake = True
            return await message.channel.send(msg)

    if steps.is_awake:
        if steps.has_started:
            print(command)
        else:
            if command.startswith('play'):
                author = message.author
                player = {
                    "name": author.username,
                    "id": author.id,
                    "total_steps": 0,
                }
                steps.players.append(player)


if __name__ == "__main__":
    client.run(get_bot_token())
