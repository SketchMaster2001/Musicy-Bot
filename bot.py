from discord.ext import commands
from discord_components import DiscordComponents

bot = commands.Bot(command_prefix="/", help_command=None)

bot.load_extension("src.music")
DiscordComponents(bot)

bot.run("TOKEN_HERE")
