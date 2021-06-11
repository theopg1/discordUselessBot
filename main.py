import os
import random
import pypokedex
import discord
from discord.ext import commands
from dotenv import load_dotenv

from banWord import banWord

load_dotenv(dotenv_path='config')


class UselessBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='=')
        self.add_command(self.ping)
        self.add_command(self._8ball)
        self.add_command(self.pokeRandom)
        self.add_command(self.pokedex)
        self.add_command(self.pokeName)

    async def on_ready(self):
        print('Logged on as', self.user.display_name)

        guild_count = 0

        for guild in self.guilds:
            print(f"- Server ID: {guild.id} (name: {guild.name})")
            guild_count = guild_count + 1

        print(self.user.display_name + " is in " + str(guild_count) + " guilds.")

        await self.change_presence(activity=discord.Game('chercher à être utile'))

    @commands.command(name='ping')
    async def ping(ctx):
        await ctx.send('pong')

    @commands.command(name='8ball')
    async def _8ball(ctx):
        responses = ['Oui',
                     'Non',
                     'Probablement',
                     'Il semblerait bien',
                     'Sans aucun doute',
                     'Flemme de répondre à cette question idiote',
                     'Je ne saurais dire',
                     'Demande plus tard',
                     'Je ne pense pas',
                     'Ça me paraît peu probable'
                     ]
        await ctx.send(random.choice(responses))

    @commands.command(name='pokeRandom')
    async def pokeRandom(ctx):
        DEX = random.randint(0, 898)
        p = pypokedex.get(dex=int(DEX))
        embed = discord.Embed(
            title=p.name.capitalize(),
            description=f'Hauteur : {p.height / 10}m | Poids : {p.weight / 10}kg',
            colour=discord.Colour.red()
        )

        embed.add_field(name='Type(s) : ',
                        value=f'{p.types}'.replace('[', '').replace(']', '').replace('\'', '').title(), inline=False)
        embed.add_field(name='Talent(s) : ', value=f'{p.abilities}'
                        .replace('[', '').replace(']', '')
                        .replace('(', '').replace(')', '')
                        .replace('\'', '').replace('=', '').replace('-', ' ')
                        .replace('Ability', '')
                        .replace(', is_hidden', '')
                        .replace('name', '')
                        .replace('True', '').replace('False', '')
                        .title(), inline=False)
        embed.add_field(name='Hp : ', value=f'{p.base_stats.hp}', inline=True)
        embed.add_field(name='Atk : ', value=f'{p.base_stats.attack}', inline=True)
        embed.add_field(name='Def : ', value=f'{p.base_stats.defense}', inline=True)
        embed.add_field(name='SpAtk : ', value=f'{p.base_stats.sp_atk}', inline=True)
        embed.add_field(name='SpDef : ', value=f'{p.base_stats.sp_def}', inline=True)
        embed.add_field(name='Spd : ', value=f'{p.base_stats.speed}', inline=True)
        embed.set_footer(text=f'{p.dex}/898')
        embed.set_image(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p.dex}.png')

        await ctx.send(embed=embed)

    @commands.command(name='pokedex')
    async def pokedex(ctx, DEX):
        if 0 < int(DEX) <= 898:
            p = pypokedex.get(dex=int(DEX))
            embed = discord.Embed(
                title=p.name.capitalize(),
                description=f'Hauteur : {p.height / 10}m | Poids : {p.weight / 10}kg',
                colour=discord.Colour.red()
            )

            embed.add_field(name='Type(s) : ',
                            value=f'{p.types}'.replace('[', '').replace(']', '').replace('\'', '').title(),
                            inline=False)
            embed.add_field(name='Talent(s) : ', value=f'{p.abilities}'
                            .replace('[', '').replace(']', '')
                            .replace('(', '').replace(')', '')
                            .replace('\'', '').replace('=', '').replace('-', ' ')
                            .replace('Ability', '')
                            .replace(', is_hidden', '')
                            .replace('name', '')
                            .replace('True', '').replace('False', '')
                            .title(), inline=False)
            embed.add_field(name='Hp : ', value=f'{p.base_stats.hp}', inline=True)
            embed.add_field(name='Atk : ', value=f'{p.base_stats.attack}', inline=True)
            embed.add_field(name='Def : ', value=f'{p.base_stats.defense}', inline=True)
            embed.add_field(name='SpAtk : ', value=f'{p.base_stats.sp_atk}', inline=True)
            embed.add_field(name='SpDef : ', value=f'{p.base_stats.sp_def}', inline=True)
            embed.add_field(name='Spd : ', value=f'{p.base_stats.speed}', inline=True)
            embed.set_footer(text=f'{p.dex}/898')
            embed.set_image(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p.dex}.png')

            await ctx.send(embed=embed)

        else:
            await ctx.send('Numéro national incorrect')

    @commands.command(name='pokeName')
    async def pokeName(ctx, NAME):
        p = pypokedex.get(name=NAME)
        embed = discord.Embed(
            title=p.name.capitalize(),
            description=f'Hauteur : {p.height / 10}m | Poids : {p.weight / 10}kg',
            colour=discord.Colour.red()
        )

        embed.add_field(name='Type(s) : ',
                        value=f'{p.types}'.replace('[', '').replace(']', '').replace('\'', '').title(),
                        inline=False)
        embed.add_field(name='Talent(s) : ', value=f'{p.abilities}'
                        .replace('[', '').replace(']', '')
                        .replace('(', '').replace(')', '')
                        .replace('\'', '').replace('=', '').replace('-', ' ')
                        .replace('Ability', '')
                        .replace(', is_hidden', '')
                        .replace('name', '')
                        .replace('True', '').replace('False', '')
                        .title(), inline=False)
        embed.add_field(name='Hp : ', value=f'{p.base_stats.hp}', inline=True)
        embed.add_field(name='Atk : ', value=f'{p.base_stats.attack}', inline=True)
        embed.add_field(name='Def : ', value=f'{p.base_stats.defense}', inline=True)
        embed.add_field(name='SpAtk : ', value=f'{p.base_stats.sp_atk}', inline=True)
        embed.add_field(name='SpDef : ', value=f'{p.base_stats.sp_def}', inline=True)
        embed.add_field(name='Spd : ', value=f'{p.base_stats.speed}', inline=True)
        embed.set_footer(text=f'{p.dex}/898')
        embed.set_image(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p.dex}.png')

        await ctx.send(embed=embed)

    async def on_message(self, message):

        if message.author == self.user:
            return

        messageContent = message.content.lower()
        if len(messageContent) > 0:
            if '851365360027566090' in messageContent:
                ping_list = ['La calotte de tes morts', 'Mange tes morts', 'Rafale tes morts', 'Stop',
                             'Je vais te goumer']
                await message.channel.send(random.choice(ping_list) + ', me ping pas.')

        messageContent = message.content.lower()
        if len(messageContent) > 0:
            word_list = banWord
            for word in word_list:
                if word in messageContent:
                    response_list = ['Pour qui tu te prends ?', 'Ptdr t ki', 'Chut', 'D\'ou tu parles ?',
                                     'Parle mieux']
                    await message.delete()
                    await message.channel.send(random.choice(response_list))

        messageContent = message.content.lower()
        if len(messageContent) > 0:
            if 'j\'ai faim' in messageContent:
                await message.channel.send('Bah mange tes morts sale gros')

        messageAttachments = message.attachments
        if len(messageAttachments) > 0:
            for attachment in messageAttachments:

                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    await message.channel.send("Fichiers .dll Interdits !")

                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    await message.channel.send("Fichiers .exe Interdits !")

                else:
                    break

        await self.process_commands(message)

    def run(self):
        super().run(os.getenv('TOKEN'))


if __name__ == "__main__":
    uselessBot = UselessBot()
    uselessBot.run()
