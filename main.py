import discord
import os
try:
    from config import get_bot_token
    token = get_bot_token()
except:
    token = os.getenv("BOT_TOKEN")
    
from model.steps import Steps
import random


client = discord.Client()
init_game_commands = 'init zSteps'
steps = Steps()

@client.event
async def on_ready():
    print("zSteps is online")


@client.event
async def on_message(message):
    channel = message.channel
    command = message.content.lower()
    if command.startswith('init zsteps'):
        if steps.is_awake:
            return await channel.send("You can't start a game that has already been started")
        else:
            msg = 'Thanks for waking me up from my slumber.\nRules for the game are:\n1. Players should type "play" to be added to the game.\n2. Anyone can type "start, n, x" when all participating players have joined. The "n" is the number of steps to be taken by each player to reach the location the object is located at; also, the "x" is the name of the object to be attained by a player. For example, "start, 100, crown".\n3. If no steps are specified, the default steps to be taken is a 100. Also, if no object is specified, the default object would be a Crown.\n4. To start playing, type "takeStep, y" where "y" represents your previous step(s). In the beginning, since no one has a step count, each player would start with a 0 e.g "takeStep, 0".\n5. Players would be penalized by taking 5 steps back if they do not obey rule no.4 \n6. The steps made by a player would be a number between 0-10; thus, players must type as fast as they can.\n6. This is not a turn based game, but how fast a player can gain steps to reach their destination.\n7. The winner is determined when a player has the exact or more "n" steps.\n8. Play away!! And test how good your RNG is...haha'
            #msg = "Thanks for waking me up from my slumber.\nRules for the game are:\n"
            steps.is_awake = True
            return await channel.send(msg)

    if steps.is_awake:
        if command.startswith('quit') or command.startswith('exit'):
            steps.reset()
            msg = 'Aw! ;( Back to sleeping. Lemme know whenever you wanna play with me.'
            return await channel.send(msg)
        if steps.has_started:
            if command.startswith('takestep'):
                args = command.split(",")
                try:
                    _prev_steps_ = args[1]
                except IndexError:
                    _prev_steps_ = None
                    pass
                id = message.author.id
                rand_num = random.randint(1, 9)
                penalized = False
                end_game = False
                for player in steps.players:
                    if player["total_steps"] >= steps.step_count:
                        end_game = True
                        steps.winners.append(player)
                for player in steps.players:
                    if player["id"] == id:
                        player["total_steps"] += rand_num
                        prev_steps = player["prev_steps"]
                        player["prev_steps"] = rand_num
                        try:
                            if _prev_steps_ == None or prev_steps != int(_prev_steps_.strip()):
                                if player["total_steps"] <= 0:
                                    player["total_steps"] = 0
                                else:
                                    player["total_steps"] -= 5
                                    if player["total_steps"] < 0:
                                        player["total_steps"] = 0
                                    penalized = True
                        except ValueError:
                            if player["total_steps"] <= 0:
                                    player["total_steps"] = 0
                            else:
                                player["total_steps"] -= 5
                                if player["total_steps"] < 0:
                                    player["total_steps"] = 0
                                penalized = True
                            pass
                        msg = '{0} took {1} step(s) towards the {2}\nTotal accumulated steps: {3}\n'.format(player["name"], rand_num, steps.price, player["total_steps"])
                        if penalized:
                            msg+="You've been penalized by taking 5 steps back. To know why, please read the rules at the beginning of the game."
                        
                        await channel.send(msg)
                        break
                
                if end_game:
                    steps.players = sorted(steps.players, key=lambda p : p['total_steps'])
                    steps.players.reverse()
                    c = 1
                    msg = "Let's see who got the {0}...\n".format(steps.price)
                    for player in steps.players:
                        msg+="{0}. {1}: {2}.\n".format(c, player["name"], player["total_steps"])
                        c+=1
                    
                    if len(steps.winners) > 1:
                        msg+='There was a tie! Since more than one person won the game, there is no winner. The winners should start a new game and have a rematch until one person wins.'
                    else:
                        player = steps.players[0]
                        msg+='<@{0}> won the game; thus, they deserve the {1}!'.format(player['id'], steps.price)
                    steps.reset()
                        
                    return await channel.send(msg)
        else:
            if command.startswith('play'):
                author = message.author
                name = author.display_name
                id = author.id
                player = {
                    "name": name,
                    "id": id,
                    "total_steps": 0,
                    "prev_steps" : 0,
                }
                
                steps.players.append(player)
                msg = "<@{0}> joined the game.".format(id)
                return await channel.send(msg)
                
            if not steps.has_started and len(steps.players) > 0 and command.startswith('start'):
                args = command.split(",")
                print(args)
                try:
                    steps_count = args[1]
                    steps_count = int(steps_count.strip())
                except IndexError:
                    steps_count = 100
                except ValueError:
                    steps_count = 100
                    
                try:
                    price = args[2]
                    price = price.strip()
                except IndexError:
                    price = "Crown"
                    
               
                steps.price = price
                steps.step_count = steps_count
                steps.has_started = True
                print(price)
                print(steps.step_count)
                msg = 'The game has been started! All players get ready and go!'
                return await channel.send(msg)
        


if __name__ == "__main__":
    client.run(token)
