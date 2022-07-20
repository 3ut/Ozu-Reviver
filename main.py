'''Copyright, you are not authorized to resell/skid this tool

don't skid this tool, learn to program and make one yourself nerd 🤓'''

from concurrent.futures import ThreadPoolExecutor
import discord, json, time, os
import logging
from colorama import Fore
from swaps_library import discord_api
from discord.ext import commands


logging.basicConfig(level=logging.INFO, format=f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} %(message)s{Fore.RESET}", datefmt=f"%H:%M:%S")

with open('config.json', 'r') as f:
    config = json.load(f)

# variables from config.json
token = config['token']
prefix = config['prefix']
webhooks_name = config['webhooks_name']
channels_name = config['channels_name']
guild_name = config['guild_name']
roles_name = config['roles_name']
tts = config['tts']
check = False
# get your ping (ms)
before = time.monotonic()
ping = (time.monotonic() - before) * 1000

# multi threading library
multi_thread = ThreadPoolExecutor(max_workers=int(10000))

# bot variable
swaps = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True)
swaps.remove_command('help')


def start():
      if token == "":
        logging.info("insert your token in config.json (user token)")
        input()
      else:
       try:
        swaps.run(token, bot=False)
       except discord.errors.LoginFailure:
          logging.info("Error, invalid token!")
       except discord.errors.PrivilegedIntentsRequired:
          logging.info("Error, enable intents in the developer portal https://discord.com/developers/applications/")
       except discord.HTTPException:
          logging.info("Error, ratelimited")

@swaps.event
async def on_ready():
   logging.info(f"Token: {token[:10]}********* | Status: Connected | Username: {swaps.user}")

@swaps.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(f'''```
                           SwapsNuker V1
    ╔══════════════════════════════════════════════════════════════╗
    ║ {prefix}nuke     -> destroy a server                                ║     
    ║ {prefix}hookspam -> create and spam webhooks                        ║             
    ║ {prefix}cs       -> spam 250 channels                               ║             
    ║ {prefix}cr       -> spam 250 roles                                  ║    
    ║ {prefix}cls      -> clear console logs                              ║                                
    ╚══════════════════════════════════════════════════════════════╝
               [Logged in as: {swaps.user} | Ping: {int(ping)}ms]```''', delete_after=20)

@swaps.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system('cls')

@swaps.command()
async def cs(ctx):
    await ctx.message.delete()
    guild_id = ctx.guild.id
    for i in range(8):
        try:
         multi_thread.submit(discord_api.channel_spam, token, guild_id)
        except:
            logging.info("Thread error: channel_spammer")
    await ctx.send(f'''```
                           SwapsNuker V1
    ╔══════════════════════════════════════════════════════════════╗
    ║                        Task Finished!                        ║
    ╚══════════════════════════════════════════════════════════════╝
               [Logged in as: {swaps.user} | Ping: {int(ping)}ms]```''', delete_after=20)

@swaps.command()
async def cr(ctx):
    await ctx.message.delete()
    guild_id = ctx.guild.id
    for i in range(8):
        try:
            multi_thread.submit(discord_api.roles_spam, token, guild_id)
        except:
            logging.info("Thread error: roles_spammer")
    await ctx.send(f'''```
                              SwapsNuker V1
    ╔══════════════════════════════════════════════════════════════╗
    ║                         Task finished!                       ║     
    ╚══════════════════════════════════════════════════════════════╝
               [Logged in as: {swaps.user} | Ping: {int(ping)}ms]```''', delete_after=20)        


@swaps.command()
async def hookspam(ctx):
    await ctx.message.delete()
    for channels in ctx.guild.channels:
        try:
            channel_id = channels.id
            multi_thread.submit(discord_api.webhook_spam, token, channel_id)
        except:
            logging.info("Thread error: webhook_spam")
    await ctx.send(f'''```
                           SwapsNuker V1
    ╔══════════════════════════════════════════════════════════════╗
    ║                      Task finished!                          ║
    ╚══════════════════════════════════════════════════════════════╝
               [Logged in as: {swaps.user} | Ping: {int(ping)}ms]```''', delete_after=20)    

@swaps.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild_id = ctx.guild.id
    discord_api.change_guild_name(token, guild_id)
    for i in range(8):
        try:
         multi_thread.submit(discord_api.channel_spam, token, guild_id)
        except:
            logging.info("Thread error: channel_spammer")
    for i in range(8):
        try:
            multi_thread.submit(discord_api.roles_spam, token, guild_id)
        except:
            logging.info("Thread error: roles_spammer")


@swaps.event
async def on_guild_channel_create(channel):
        try:
            channel_id = channel.id
            multi_thread.submit(discord_api.webhook_spam, token, channel_id)
        except:
            logging.info("Thread error: webhook_spam")



if __name__ == '__main__':
    start()

    