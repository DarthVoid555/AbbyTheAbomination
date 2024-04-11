from templatebot import Bot
from discord import AllowedMentions, Activity, Game
from os import environ as env
from dotenv import load_dotenv
import discord
from discord.ext import fancyhelp, commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = Bot(
    name="Coffee",
    command_prefix=";;",
    allowed_mentions=AllowedMentions(
        everyone=False, roles=False, users=True
    ),
    help_command=fancyhelp.EmbeddedHelpCommand(color=0x2F3136),
    intents=intents
)

bot.VERSION = "2.0.0"


list = ["cogs.logs", "cogs.mod", "cogs.setup", "cogs.top-gg"]
for item in list:
    bot.load_extension(item)


'''
bot.load_initial_cogs(
    "cogs.logs", "cogs.mod", "cogs.setup", "cogs.top-gg"
)
'''

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"💥 {error}")
    # Lazy error_handling, will be changed soon!


bot.run("MTIyNDMzNDQ0MTgwNDA3NTE1MA.G8e5I9.4cYr7bIx6Zn-X-mmY-RJZ3Dnl9N68ip5raUqyY")
