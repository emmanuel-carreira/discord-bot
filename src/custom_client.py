import discord


class CustomClient(discord.Client):

    async def on_ready(self):
        print('{} has connected to Discord!'.format(self.user))

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send('Bem-vindx companheirx {}!'.format(member.name))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if '!hello' in message.content:
            await message.channel.send('Hello to you!')

    async def on_error(self, event, *args, **kwargs):
        with open('error.log', 'a') as f:
            if event == 'on_message':
                f.write('Unhandled message: {}\n'.format(args[0]))
            else:
                raise
