import discord
import os
import random
import asyncio
from discord.ext.commands import Bot
from dotenv import load_dotenv

# Load .env file
load_dotenv()

bot = Bot(command_prefix='!')

# Vars from .env
auth_token = os.getenv('AUTH_TOKEN')
room_id = int(os.getenv('ROOM_ID'))
counter = int(os.getenv('START_COUNTER'))

# Function for scheduled sending of messages to the channel


async def scheduled_messages():

    # Main loop (sending messages)
    while True:
        channel = bot.get_channel(room_id)
        sending_time = random.uniform(5, 30)
        await asyncio.sleep(sending_time)
        await channel.send(f"{counter} МаЛеНьКиХ ЯрЧе")


@bot.event
async def on_message(message):
    channel = bot.get_channel(room_id)
    if message.channel == channel:
        msg = str(message.content)
        global counter
        counter = int(msg.split()[0]) + 1


@bot.event
async def on_ready():
    print(f"Logged as {bot.user.name}")
    await scheduled_messages()

if __name__ == '__main__':
    bot.run(auth_token)
