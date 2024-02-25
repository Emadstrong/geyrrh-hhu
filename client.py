import discord
import discord.ext
import discord.ui
from discord.ext import commands
import os
from dotenv import load_dotenv 

load_dotenv()
bot_token = os.environ['bot_token']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

async def on_ready():
  print('System rebooted.')
  bot.add_view(MyView())

@bot.command() 
async def nice(ctx, arg): 
  embed=discord.Embed(title="Hello ViTK", description="nice man")
  await ctx.send(embed = embed, view=MyView)
  
class MyView(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
 
  @discord.ui.button(label="hello", style=discord.ButtonStyle.green)
  async def MyView(self, interaction:discord.Interaction, button:discord.ui.Button):
    role=1203956999239368738 
    user=interaction.user
    if type(bot.role) is not discord.Role:
      bot.role=interaction.guild.get_role(1205160396701442098)
    if bot.role not in interaction.user.roles:
      await interaction.user.add_roles(bot.role)
      await interaction.response.send_message(f"EMAD VITK", ephemeral=True)
    else: await interaction.response.send_message(f"Emad vitk already pressed the button", ephemeral=True)

async def button(interaction: discord.Interaction):
  await interaction.response.send_message(view=button_view())

bot.run(bot_token)
