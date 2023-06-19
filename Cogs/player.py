import discord
from discord import app_commands
from discord.ext import commands

class player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print("Cog load")

    @app_commands.command(name = "userinfo", description= "userinfo porra")
    async def userinfo(self, interaction:discord.Interaction, member:discord.Member=None):
        if member == None:
            member = interaction.user
        embed = discord.Embed(title=f"User Info: {member.id}", description=f"Descrição do perfil de {member.mention}", color= discord.Color.green())
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Nickname", value= f"`{member.display_name}`")
        embed.add_field(name="lvl", value= "**1**", inline= True)
        embed.add_field(name="Grupo", value= "`Robertinho, Frederico, Roberta`", inline= False)
        embed.add_field(name="Gold", value= 426, inline= False)
        embed.add_field(name="Localização", value= "`Plato Altos`", inline= True)
        embed.add_field(name="Em perigo?", value= "False", inline= True)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(player(bot))