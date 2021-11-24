from discord.ext import commands
from discord_components import DiscordComponents

bot = commands.Bot(command_prefix="/")

bot.load_extension("src.music")
DiscordComponents(bot)

bot.run("TOKEN_GOES_HERE")
