#W.I.P

#Imports.
import random
import discord
from discord.ext import commands
import json
import os

#Load Json.
class Plane(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        with open("cogs/planes.json", "r", encoding="utf-8") as f:
            self.planes = json.load(f)
    
    #Hybrid commands.
    @commands.hybrid_command(name="plane", description="Get a random plane embed.")
    async def plane(self, ctx: commands.Context):
        plane = random.choice(self.planes)
        embed = discord.Embed(
            title=plane["title"],
            description=plane["description"]
        )
        await ctx.send(embed=embed)

#Load cog.
async def setup(bot: commands.Bot):
    await bot.add_cog(Plane(bot))