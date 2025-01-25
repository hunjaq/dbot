import discord
from discord.ext import commands
import keys

client = discord.Client()
client = commands.Bot(command_prefix="|")
is_client_running = False

# runs when bot ir ready
@client.event
async def on_ready():
    global is_client_running

    # only run on first call of function
    if not is_client_running:
        is_client_running = True
        print(f"Bot {client.user.name} ready!")


#process the message -- pass to process command if command
@client.event
async def on_message(message):
    #prevent bot from responding to itself
    if message.author == client.user:
        return
    
    await client.process_commands(message)


# Bot shutdown
@client.command()
async def terminate(ctx):
    await ctx.send("Terminating...")
    await client.logout()

# play song from youtube
@client.command()
async def play(url):
    # check if url is youtube
    # get it?

client.run(keys.TOKEN)
