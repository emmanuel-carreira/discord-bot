import discord


class CustomClient(discord.Client):

    async def on_ready(self):
        print("{} has connected to Discord!".format(self.user))

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send("Bem-vindx companheirx {}!".format(member.name))
