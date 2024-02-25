import discord
from discord.ext import commmands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ['bot_token']


client = commands.Bot(command_prefix".", intents=discord.Intents.all)


async def on_ready():
  await client.tree.sync()
  print("ur bot is online")

class SelfRoles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)
   
    @discord.ui.button(label="", style=discord.ButtonStyle.green)
    async def green_color(self, interaction: discord.Interaction, button: discord.ui.Button):
      green_role = discord.utils.get(interaction.guild.roles, name="Green")
     
      await interaction.user.add_roles(green_role)

@client.tree.command(name="selfroles", description"")
async def self_roles(interaction: discord.Interaction):
  await interaction.response.send_message(contant="nice one", view=SelfRoles())



async def main():
  async with client:
    await load()
    await client.start(bot_token)

asyncio.run(main())
