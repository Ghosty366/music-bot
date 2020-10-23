import discord
from discord.ext import commands, tasks
import time
from bot_resources import api
bot = commands.Bot(command_prefix="gh366!", owner_ids=[609522313150332962, 369686253769195520])
@bot.event
async def on_ready():
  print("bot is now online")
  bot.load_extension("cogs.music")
  loop.start()
@tasks.loop(seconds=300)
async def loop():
  status=discord.Activity(name="music on "+str(len(bot.guilds))+" servers!", type=discord.ActivityType.playing)
  await bot.change_presence(activity=status)
bot.run('NzQ2ODIxNTQ5OTE4NTE5NDE3.X0F5xA.k5YMeuWgbV1F3VT2euMcRP0kmEY')
