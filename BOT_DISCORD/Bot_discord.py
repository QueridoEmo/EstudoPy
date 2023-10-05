import discord
from discord import app_commands
import random

id_do_servidor = 997261680251764828

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.sinced = False
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild= discord.Object(id=id_do_servidor))
            self.synced = True
        pint(f"Entramos como {self.user}.")
        
aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild= discord.Object(id=id_do_servidor), name = "test", description="testing bot")
async def testcmd (interaction: discord.Integration):
    await interaction.response.send_menssage(f"estou funcionando cara!", ephemeral = False)


@tree.command(guild= discord.Object(id=id_do_servidor), name = "d20", description="Número de um dado aleatório")
async def dado (interaction: discord.Integration):
    numero = random.randint(1, 20)
    await interaction.response.send_menssage(f"Dado Número: {numero}", ephemeral = False)


aclient.run("")