from datetime import datetime
from os import environ

import discord
import json

token = environ["DISCORD_TOKEN"]
channel_id = int(environ["DISCORD_CHANNEL_ID"])
default_ping = environ["DISCORD_DEFAULT_PING"]
easy_ping = environ["DISCORD_EASY_PING"]
medium_ping = environ["DISCORD_MEDIUM_PING"]
hard_ping = environ["DISCORD_HARD_PING"]
start_date = datetime.fromisoformat(environ["STUDY_PLAN_START_DATE"])

difficultyPings = {"Easy": easy_ping, "Medium": medium_ping, "Hard": hard_ping}

discord.utils.setup_logging()
intents = discord.Intents.default()
client = discord.Client(intents=intents)


def create_message_body():
    message_body = f"<{url}>"
    print(f"Message body: '{message_body}'")
    return message_body


def create_thread_title(problem_number, problem_name):
    thread_title = f"{problem_number} - {problem_name}"
    print(f"Thread title: '{thread_title}'")
    return thread_title


def create_thread_message_body():
    message_body = f"<@&{default_ping}>, <@&{difficultyPings.get(difficulty)}>"
    print(f"Thread message body: '{message_body}'")
    return message_body


def calculate_day_number(start):
    today = datetime.utcnow()
    days = (today - start).days
    return days


json_file_path = "problems.json"
json_file = open(json_file_path)
json_data = json.load(json_file)
day = calculate_day_number(start_date)
index = day - 1
problem = json_data["problems"][index]

url = problem["url"]
name = problem["name"]
difficulty = problem["difficulty"]


async def send_message():
    message_body = create_message_body()
    thread_title = create_thread_title(day, name)
    thread_body = create_thread_message_body()
    channel = client.get_channel(channel_id)
    message = await channel.send(message_body)
    thread = await message.create_thread(name=thread_title)
    await thread.send(thread_body)
    await client.close()


@client.event
async def on_ready():
    await send_message()


client.run(token)

