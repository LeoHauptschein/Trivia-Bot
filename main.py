import discord
from discord import app_commands
import os
import commands
import trivia
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user} is now online!')
    await client.change_presence(activity=discord.Game('Roblox'))

    try:
        synced = await tree.sync()
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    print(f"{username} said '{user_message}'")

    response = commands.handle_command(user_message)
    if "roblox" in user_message.lower() or "rablax" in user_message.lower():
        await message.add_reaction('<:roblox:1125263896261963787>')
    if response:
        print("yes")
        await message.reply(response)


@tree.command(name = "what", description = "test")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(f"what da hell")


@tree.command(name = "trivia", description = "play trivia game")
async def help(interaction: discord.Interaction):
    await trivia.run_trivia(client, interaction)
    """print(interaction.user, 'started trivia')
    await interaction.response.send_message(f"Starting trivia... How many questions? (1-50)")
    question = await interaction.original_response()

    def check(m):
        return m.author == interaction.user
    try:
        response = await client.wait_for('message', timeout=60.0, check=check)
        questions = int(response.content)
        if questions < 1 or questions > 50:
            raise ValueError 
    except:
        await question.reply('None or invalid response')
    else:
        await response.reply(f"Selected {response.content} questions!")
        await interaction.channel.send(Select a category (Type 'Any' for all of them): 
    General Knowledge, Books, Film, Music, Theatre, Television, Video Games, Board Games, Science & Nature, Computers, Math, 
    Mythology, Sports, Geography, History, Politics, Art, Celebrities, Animals, Vehicles, Comics, Gadgets, Anime/Manga, Cartoons/Animation)
    try:
        category = await client.wait_for('message', timeout=60.0, check=check)
    except:
        print("Error")
    """

client.run(TOKEN)
