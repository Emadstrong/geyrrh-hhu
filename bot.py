import discord
import discord.ui
import discord.ext
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ['bot_token']


client = commands.Bot(command_prefix="!", intents=discord.Intents.default(), help_command=None) 


async def on_ready():
  await client.tree.sync()
  print("ur bot is online")

class SelfRoles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)
   
    

@client.tree.command(name="selfroles", description="ggyyg")
async def self_roles(interaction: discord.Interaction):
  await interaction.response.send_message(contant="nice one", view=SelfRoles())

@discord.ui.button(label="green", style=discord.ButtonStyle.green)
    async def self_roles(self, interaction: discord.Interaction, button: discord.ui.Button):
      green_role = discord.utils.get(interaction.guild.roles, name="Green")
     
      await interaction.user.add_roles(green_role) 



async def main():
  async with client:
    await load()
    await client.start(bot_token)

asyncio.run(main())
