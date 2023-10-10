import questions
import discord
from discord import app_commands

category_list = """Select a category (Type 'Any' for all of them): 
    General Knowledge, Books, Film, Music, Theatre, Television, Video Games, Board Games, Science & Nature, Computers, Math, 
    Mythology, Sports, Geography, History, Politics, Art, Celebrities, Animals, Vehicles, Comics, Gadgets, Anime/Manga, Cartoons/Animation"""

category_codes = {'any' : 0, 'general knowledge' : 9, 'books' : 10, 'film' : 11, 'music' : 12, 'theatre' : 13, 'television' : 14, 'video games' : 15,
                      'board games' : 16, 'science & nature' : 17, 'computers' : 18, 'math' : 19, 'mythology' : 20, 'sports' : 21, 'geography' : 22,
                      'history' : 23, 'politics' : 24, 'art' : 25, 'celebrities' : 26, 'animals' : 27, 'vehicles' : 28, 'comics' : 29, 'gadgets' : 30,
                      'anime/manga' : 31, 'cartoons/animation' : 32 }

async def run_trivia(client, interaction):
    def check(m):
        return m.author == interaction.user
    print(interaction.user, 'started trivia')
    count = await select_questions(client, interaction, check)
    await interaction.channel.send(category_list)
    category = await select_category(client, interaction, check)
    print(category)


async def select_questions(client, interaction, check) -> int:
    await interaction.response.send_message(f"Starting trivia... How many questions? (1-50)")
    question = await interaction.original_response()
    try:
        response = await client.wait_for('message', timeout=60.0, check=check)
        questions = int(response.content)
        if questions < 1 or questions > 50:
            raise ValueError 
    except:
        await question.reply('None or invalid response')
    else:
        await response.reply(f"Selected {response.content} questions!")
        return questions


async def select_category(client, interaction, check) -> str:
    try:
        response = await client.wait_for('message', timeout=60.0, check=check)
        category = response.content.lower()
        if not category_codes.get(category):
            raise NameError
    except:
        await interaction.channel.send('None or invalid response')
    else:
        await category.reply(f"Selected {category}!")
        return category_codes.get(category)


def select_difficulty() -> str:
    difficulty = input("Select difficulty (Easy, Medium, Hard, or Any): ").lower()
    while difficulty not in ('easy', 'medium', 'hard', 'any'):
        difficulty = input("Select a valid difficulty (Easy, Medium, Hard, or Any): ").lower()
    return difficulty
