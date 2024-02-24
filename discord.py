import discotd
from discord import app_commands

class button_view(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout = None)
 
  @discord.ui.button(label = "hello")
  async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
    if type(client.role) is not discord.Role:
      client.role = interaction.guild.get_role(55537364)
    if client.role not in interaction.user.roles:
      await interaction.user.add_roles(client.role)
      await interaction.response.send_message(f"EMAD VITK", ephemeral = True)
    else: await interaction.response.send_message(f"Emad vitk already pressed the button", ephemeral = True)

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = discord.Intents.default())
    self.synced = False
    self.role = 26737346
    self.added = False

async def on_ready(self):
  await self.wait_until_ready
  if not self.synced:

    self.synced = True
    if not self.added:
      self.add_view(button_view())
      self.added = True
print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=733464646), name = 'button', description='Launches role button')
async def button(interaction: discord.Interaction):
  await interaction.response.send_message(view = button_view())

client.run('YOUR BOT TOKEN')
