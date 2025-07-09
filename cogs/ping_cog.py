#Imports.
import discord
from discord.ext import commands

#Hybrid commands.
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="ping", description="Latency.")
    async def ping(self, ctx: commands.Context):
        latency_ms = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! `{latency_ms}ms`")

#Load cog.
async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))