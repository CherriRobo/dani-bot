#Greeting.
print("Welcome back Dani :)")

#Imports.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

#Env.
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = int(os.getenv("GUILD"))

#Hybrid commands.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)
bot.synced = False

#Start-up commands.
@bot.event
async def on_ready():
    await bot.change_presence(
        status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.listening, name = "Dani's commands."))

    #Sync commands.
    if not bot.synced:
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)! :D")
            for cmd in synced:
                bot.synced = True
        except Exception as e:
            print(f"Slash sync failed :( see: {e}")

#Load cogs.
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename} :3")
            except Exception as e:
                print(f"Failed to load {filename} :( see: {e}")

#Run bot.
if __name__ == "__main__":
    import asyncio

    async def main():
        await load_extensions()
        await bot.start(TOKEN)

    asyncio.run(main())