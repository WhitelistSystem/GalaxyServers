import discord
import random
import json
import os
import datetime
import asyncio
import traceback
import sys

from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True


class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('This is red.', ephemeral=True)

    @discord.ui.button(label='Grey', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('This is grey.', ephemeral=True)

class PersistentViewBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('g!'))
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistentView())
            self.add_view(Confirm())
            self.add_view(ReactionRoles())
            self.add_view(DropdownView())
            self.persistent_views_added = True
            activity = discord.Game(name="play.galaxyservers.xyz", type=3)
            await self.change_presence(status=discord.Status.online,
                                        activity=activity)

        print(f'Signed in as {self.user}')

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(emoji='<a:Smoothie:861446075876638720>', style=discord.ButtonStyle.green, custom_id='pp1')
    async def test1(self, button: discord.ui.Button, interaction: discord.Interaction):
        member = interaction.guild.get_role(821639145910173757)
        await interaction.user.add_roles(member)
        self.value = False
        try:
            await interaction.user.send('Thank you very much for verifying! Have a nice day :)')
        except:
            return

class ReactionRoles(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        super().__init__(timeout=None)

    @discord.ui.button(label='Sneak Peaks', style=discord.ButtonStyle.green, row=1, custom_id='hfiuwa:sp')
    async def sneakpeaks(self, button: discord.ui.Button, interaction: discord.Interaction):
        sneakpeaks = interaction.guild.get_role(822313530077609994)
        if sneakpeaks in interaction.user.roles:
            await interaction.user.remove_roles(sneakpeaks)
            await interaction.response.send_message('You have removed the Sneak Peaks role!', ephemeral=True)
        else:
            await interaction.user.add_roles(sneakpeaks)
            await interaction.response.send_message('You have gotten the Sneak Peaks role!', ephemeral=True)

    @discord.ui.button(label='D-Events', style=discord.ButtonStyle.green, row=1, custom_id='hfiuwa:devents')
    async def devents(self, button: discord.ui.Button, interaction: discord.Interaction):
        devents = interaction.guild.get_role(850041679465021461)
        if devents in interaction.user.roles:
            await interaction.user.remove_roles(devents)
            await interaction.response.send_message('You have removed the Discord Events role!', ephemeral=True)
        else:
            await interaction.user.add_roles(devents)
            await interaction.response.send_message('You have gotten the Discord Events role!', ephemeral=True)

    @discord.ui.button(label='Events', style=discord.ButtonStyle.green, row=1, custom_id='hfiuwa:events')
    async def events(self, button: discord.ui.Button, interaction: discord.Interaction):
        events = interaction.guild.get_role(822313532749774908)
        if events in interaction.user.roles:
            await interaction.user.remove_roles(events)
            await interaction.response.send_message('You have removed the Events role!', ephemeral=True)
        else:
            await interaction.user.add_roles(events)
            await interaction.response.send_message('You have gotten the Events role!', ephemeral=True)

    @discord.ui.button(label='Giveaways', style=discord.ButtonStyle.green, row=2, custom_id='hfiuwa:giveaways')
    async def giveaways(self, button: discord.ui.Button, interaction: discord.Interaction):
        giveaways = interaction.guild.get_role(822313535324946432)
        if giveaways in interaction.user.roles:
            await interaction.user.remove_roles(giveaways)
            await interaction.response.send_message('You have removed the Giveaways role!', ephemeral=True)
        else:
            await interaction.user.add_roles(giveaways)
            await interaction.response.send_message('You have gotten the Giveaways role!', ephemeral=True)

    @discord.ui.button(label='Skyblock‎‎‏‏‎', style=discord.ButtonStyle.green, row=2, custom_id='hfiuwa:skyblock')
    async def skyblock(self, button: discord.ui.Button, interaction: discord.Interaction):
        skyblock = interaction.guild.get_role(822313534934351887)
        if skyblock in interaction.user.roles:
            await interaction.user.remove_roles(skyblock)
            await interaction.response.send_message('You have removed the Skyblock role!', ephemeral=True)
        else:
            await interaction.user.add_roles(skyblock)
            await interaction.response.send_message('You have gotten the Skyblock role!', ephemeral=True)

    @discord.ui.button(label='Survival', style=discord.ButtonStyle.green, row=2, custom_id='hfiuwa:survival')
    async def survival(self, button: discord.ui.Button, interaction: discord.Interaction):
        survival = interaction.guild.get_role(836261560686870569)
        if survival in interaction.user.roles:
            await interaction.user.remove_roles(survival)
            await interaction.response.send_message('You have removed the Survival role!', ephemeral=True)
        else:
            await interaction.user.add_roles(survival)
            await interaction.response.send_message('You have gotten the Survival role!', ephemeral=True)

class Link(discord.ui.View):
    def __init__(self):
        super().__init__()
        url1 = f'https://topg.org/minecraft-servers/server-632444'
        url2 = f'https://minecraftservers.org/server/620818'
        url3 = f'https://www.planetminecraft.com/server/galaxy-servers-5235600/'
        url4 = f'https://minecraft-mp.com/server-s285927'
        url5 = f'https://www.minecraft-servers-list.org/details/Olly_/'
        self.add_item(discord.ui.Button(label='Vote Link 1', url=url1, row=1))
        self.add_item(discord.ui.Button(label='Vote Link 2', url=url2, row=1))
        self.add_item(discord.ui.Button(label='Vote Link 3', url=url3, row=1))
        self.add_item(discord.ui.Button(label='Vote Link 4', url=url4, row=2))
        self.add_item(discord.ui.Button(label='Vote Link 5', url=url5, row=2))

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(emoji='📷', label='Instagram'),
            discord.SelectOption(emoji='📋', label='Server List/Voting Website'),
            discord.SelectOption(emoji='🧑', label='A Friend'),
            discord.SelectOption(emoji='❓', label='Other')
        ]
        super().__init__(placeholder='Please tell us how you found us!', min_values=1, max_values=1, options=options, custom_id='pp2')

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'You chose "{self.values[0]}", this really helps our advertising team. Thank you very much!', ephemeral=True)
        adchannel = interaction.guild.get_channel(879076281902317668)
        await adchannel.send(f'{interaction.user.mention} chose "{self.values[0]}" on how they found us!')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        super().__init__(timeout=None)
        self.add_item(Dropdown())

client = PersistentViewBot()

@client.command(aliases=['test1'])
@commands.has_permissions(administrator=True)
async def prepare(ctx: commands.Context):
    await ctx.send("What's your favourite colour?", view=PersistentView())

@client.command()
@commands.has_permissions(administrator=True)
async def reactionroles(ctx: commands.Context):
    view = ReactionRoles()
    embed = discord.Embed(
        title="Reaction Roles",
        url="",
        description=
        f"**Click the following button to get/remove the role!** \n \n \n👻 **Sneak Peaks** \n \n💣 **Discord Events** \n \n🧨 **Events**\n \n🎁 **Giveaways** \n \n<:Skyblock:822324193693401128> **Skyblock** \n \n<:Survival:836263182653063168> **Survival**",
        color=discord.Color.purple())
    await ctx.send(embed=embed, view=view)
    await ctx.message.delete()

@client.command()
async def link(ctx: commands.Context):
    view = Link()
    embed = discord.Embed(
        title="Voting Sites",
        url="",
        description=
        f"**Click the button to the corresponding vote site!** \n \n \n**Vote Link 1** - https://topg.org/minecraft-servers/server-632444 \n**Vote Link 2** - https://minecraftservers.org/server/620818 \n**Vote Link 3** - https://www.planetminecraft.com/server/galaxy-servers-5235600/ \n**Vote Link 4** - https://minecraft-mp.com/server-s285927 \n**Vote Link 5** - https://www.minecraft-servers-list.org/details/Olly_/",
        color=discord.Color.green())
    await ctx.send(embed=embed, view=view)

@client.command(aliases=['test2'])
@commands.has_permissions(administrator=True)
async def verify(ctx: commands.Context):
    view = Confirm()
    await ctx.send('Click The Button To Verify!', view=view)
    await ctx.message.delete()
    await view.wait()

@client.command(aliases=['test3'])
@commands.has_permissions(administrator=True)
async def question(ctx):
    view = DropdownView()
    await ctx.message.delete()
    await ctx.send('How Did You Find Us?', view=view)

client.remove_command('help')

@client.event
async def on_message(message):
    galaxyservers = client.get_guild(821595276837781506)
    ticketchannel = client.get_channel(836099435632918528)
    suggestionchannel = client.get_channel(822050268011167764)
    punishmentchannel = client.get_channel(851993263857991731)
    bugschannel = client.get_channel(838294002109120553)
    guild = client.get_guild(831930252296585287)
    staff = discord.utils.get(guild.roles, name="AntiCheat Pings")
    if (message.channel == punishmentchannel) and (
            message.author.id
            == 822328755913359380) and message.content != f"{staff.mention}":
        await message.channel.send(f'{staff.mention}')

    if (message.channel
            == bugschannel) and (message.author.id != 50364182214134988) and (
                message.author.id != 822328755913359380):
        staff = discord.utils.get(guild.roles, name="Owner")
        thread = await message.create_thread(name='New Bug Found!')
        thread2 = await thread.send(
            f'**Information:** \n{message.content} \n \n**Author:** \n{message.author.mention}'
        )
        await thread2.add_reaction('🔒')

    if message.content != "g!new" and (message.channel == ticketchannel) and (
            message.author.id != 503641822141349888) and (
                message.author.id != 822328755913359380) and (
                    message.author.id != 211166495781289985):
        await message.delete()
        embed = discord.Embed(title="Message Error",
                              url="",
                              description="You can only type `g!new` here!",
                              color=discord.Color.red())
        await message.author.send(embed=embed, delete_after=10)
    if message.content != "g!suggestion" and (
            message.channel == suggestionchannel) and (
                message.author.id != 503641822141349888) and (
                    message.author.id != 822328755913359380) and (
                        message.author.id != 211166495781289985):
        await message.delete()
        embed = discord.Embed(title="Message Error",
                              url="",
                              description="You can only type `g!new` here!",
                              color=discord.Color.red())
        await message.author.send(embed=embed, delete_after=10)
    prefixes = ["!", "@", "#", "$", "%", "^", "&", "*", "/", "~"]
    if message.content.startswith("prefix"):
        await message.channel.send("My Prefix Is: **g!**")
    for prefix in prefixes:
        if message.content.startswith(prefix + "prefix"):
            await message.channel.send("My Prefix Is: **m!**")
    await client.process_commands(message)


@client.command()
@commands.has_permissions(administrator=True)
async def rr(ctx):
    embed = discord.Embed(
        title="Roles",
        url="",
        description=
        f"👻 - **Sneak Peaks** \n \n💣 - **Discord Events** \n \n🧨 - **Events** \n \n📣 - **Announcements** \n \n🎁 - **Giveaways** \n \n<:Events:822321553420058665> - **Skyblock** \n \n<:Survival:836263182653063168> - **Survival**",
        color=discord.Color.purple())
    embed.set_footer(text=f"Reaction Roles")
    x = "[@every]"
    msg = await ctx.channel.send(content=x, embed=embed)
    await msg.add_reaction('👻')
    await msg.add_reaction('💣')
    await msg.add_reaction('🧨')
    await msg.add_reaction('📣')
    await msg.add_reaction('🎁')
    await msg.add_reaction('<:Events:822321553420058665>')
    await msg.add_reaction('<:Survival:836263182653063168>')
    await ctx.message.delete()


@client.command()
@commands.has_permissions(administrator=True)
async def rranti(ctx):
    embed = discord.Embed(
        title="AntiCheat pings",
        url="",
        description=
        f'Click the "<a:Diamond:867875555582803970>" reaction to get anticheat punishment pings.',
        color=discord.Color.purple())
    x = "[@everyone]"
    msg = await ctx.channel.send(content=x, embed=embed)
    await msg.add_reaction('<a:Diamond:867875555582803970>')
    await ctx.message.delete()


@client.command()
@commands.has_permissions(administrator=True)
async def rrverify(ctx):
    embed = discord.Embed(
        title="Verification",
        url="",
        description=
        f'Please click the "<a:Smoothie:861446075876638720>" reaction to be verified and view the rest of the channels.',
        color=discord.Color.green())
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('<a:Smoothie:861446075876638720>')
    await ctx.message.delete()


@client.command()
@commands.has_permissions(administrator=True)
async def rtickets(ctx):
    embed = discord.Embed(
        title="Tickets",
        url="",
        description=f'Please click the reaction to your corresponding problem.',
        color=discord.Color.purple())
    embed.add_field(name="General", value="📩", inline=True)
    embed.add_field(name="Appeal",
                    value="<:ThinkingBan:861446127924674611>",
                    inline=True)
    embed.add_field(name="Reports",
                    value="<a:VoteBan:861446399131385916>",
                    inline=True)
    embed.add_field(name="Bugs",
                    value="<a:CatGlitch:861446879657459742>",
                    inline=True)
    embed.add_field(name="Donation",
                    value="<a:Money:861451984376692777>",
                    inline=True)
    embed.add_field(name="Other",
                    value="<a:Other:861447459828924436>",
                    inline=True)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('📩')
    await msg.add_reaction('<:ThinkingBan:861446127924674611>')
    await msg.add_reaction('<a:VoteBan:861446399131385916>')
    await msg.add_reaction('<a:CatGlitch:861446879657459742>')
    await msg.add_reaction('<a:Money:861451984376692777>')
    await msg.add_reaction('<a:Other:861447459828924436>')
    await ctx.message.delete()


@client.command()
async def enlarge(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send("You need to provide an emoji!")
    else:
        await ctx.send(emoji.url)


@client.event
async def on_raw_reaction_add(payload):
    g = payload.guild_id
    guild = await client.fetch_guild(821595276837781506)
    member = await client.fetch_user(payload.user_id)
    if member.bot:
        return
    guild = client.get_guild(payload.guild_id)
    member_role = discord.utils.get(guild.roles, name="Galaxy Servers Member")
    sneakpeak = discord.utils.get(guild.roles, name="Sneak Peak")
    events = discord.utils.get(guild.roles, name="Events")
    devents = discord.utils.get(guild.roles, name="Discord Events")
    announcements = discord.utils.get(guild.roles, name="Announcements")
    giveaways = discord.utils.get(guild.roles, name="Giveaways")
    skyblock = discord.utils.get(guild.roles, name="Skyblock")
    survival = discord.utils.get(guild.roles, name="Survival")
    events = discord.utils.get(guild.roles, name="Events")
    anticheat = discord.utils.get(guild.roles, name="AntiCheat Pings")
    member = await guild.fetch_member(payload.user_id)

    if str(payload.emoji) == '👻' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(sneakpeak)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Sneak Peaks role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '💣' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(devents)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Discord Events role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '<a:Smoothie:861446075876638720>' and (
            payload.channel_id) == 836465733579046922:
        await member.add_roles(member_role)
        try:
            embed = discord.Embed(
                title="Verification Passed",
                url="",
                description=
                f"You have succesfully been verified! You may view the rest of the channels now!",
                color=discord.Color.green())
            await member.send(embed=embed)
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            user = client.get_user(payload.user_id)
            emoji = "<a:Smoothie:861446075876638720>"
            await message.remove_reaction(emoji, user)
        except:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            user = client.get_user(payload.user_id)
            emoji = "<a:Smoothie:861446075876638720>"
            await message.remove_reaction(emoji, user)

    if str(payload.emoji) == '🧨' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(events)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Events role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '📣' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(announcements)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Announcements role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '🎁' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(giveaways)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Giveaways role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '<:Events:822321553420058665>' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(skyblock)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Skyblock role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '<:Survival:836263182653063168>' and (
            payload.channel_id) == 821641676862521344:
        await member.add_roles(survival)
        embed = discord.Embed(
            title="Added Roles",
            url="",
            description=f"You have succesfully added the Survival role.",
            color=discord.Color.green())
        await member.send(embed=embed)

    if str(payload.emoji) == '🔒':
        with open('data.json') as f:
            data = json.load(f)

        if payload.channel_id in data["ticket-channel-ids"]:
            channel = await client.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            user = await client.fetch_user(payload.user_id)
            emoji = "🔒"
            await message.remove_reaction(emoji, user)

            def check(message):
                return message.author == payload.member and message.channel == message.channel and message.content.lower(
                ) == "close"

            try:
                ticketlog_channel = guild.get_channel(836102113892761671)
                em = discord.Embed(
                    title="Galaxy Tickets",
                    description=
                    "are you sure you want to close this ticket? Reply with `close` if you are sure.",
                    color=0x00a8ff)

                await message.channel.send(embed=em)
                await client.wait_for('message', check=check)
                em = discord.Embed(title="Ticket Logs",
                                   description=f"",
                                   color=0x00a8ff)
                em.add_field(name="Closer",
                             value=f"{payload.member.mention}",
                             inline=True)
                em.add_field(name="Ticket",
                             value=f"{payload.channel_id}",
                             inline=True)

                await ticketlog_channel.send(embed=em)

                await message.channel.send('Ticket will close in 15 seconds.')

                await asyncio.sleep(15)

                await message.channel.delete()

                index = data["ticket-channel-ids"].index(payload.channel_id)
                del data["ticket-channel-ids"][index]

                with open('data.json', 'w') as f:
                    json.dump(data, f)

            except asyncio.TimeoutError:
                await member.send('pp')

    if str(payload.emoji) == '📩' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "📩"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(
            title="Question 1",
            description=
            f"Is your issue with our forums, discord, or an in-game server? (Please specify which server)",
            color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(title="Question 2",
                          description=f"What is your IGN? (Forums username)",
                          color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        c = discord.Embed(title="Question 3",
                          description=f"Please explain your issue.",
                          color=0x00a8ff)

        await ticket_channel.send(embed=c)

        question3 = await client.wait_for('message', check=check)

        d = discord.Embed(
            title="Question 4",
            description=f"Please provide any evidence, if applicable",
            color=0x00a8ff)

        await ticket_channel.send(embed=d)

        question4 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**Server**: {question1.content} \n**Name**: {question2.content}\n**Issue**: {question3.content} \n**Evidence**: {question4.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')

    if str(payload.emoji) == '<:ThinkingBan:861446127924674611>' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []


        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "<:ThinkingBan:861446127924674611>"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(title="Question 1",
                          description=f"What is your IGN?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(title="Question 2",
                          description=f"Why should you be unbanned/unmuted?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        c = discord.Embed(
            title="Question 3",
            description=f"Please provide any evidence, if applicable.",
            color=0x00a8ff)

        await ticket_channel.send(embed=c)

        question3 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**IGN**: {question1.content}\n**Reasoning**: {question2.content} \n**Evidence**: {question3.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')

    if str(payload.emoji) == '<a:VoteBan:861446399131385916>' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "<a:VoteBan:861446399131385916>"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(title="Question 1",
                          description=f"What is your IGN?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(title="Question 2",
                          description=f"Who are you reporting?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        c = discord.Embed(title="Question 3",
                          description=f"Why should we punish this player?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=c)

        question3 = await client.wait_for('message', check=check)

        d = discord.Embed(
            title="Question 4",
            description=f"Please provide any evidence, if applicable.",
            color=0x00a8ff)

        await ticket_channel.send(embed=d)

        question4 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**IGN**: {question1.content}\n**Player**: {question2.content} \n**Reason**: {question3.content} \n**Evidence**: {question4.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')

    if str(payload.emoji) == '<a:CatGlitch:861446879657459742>' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "<a:CatGlitch:861446879657459742>"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(title="Question 1",
                          description=f"What is your IGN?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(title="Question 2",
                          description=f"What server is the bug from?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**IGN**: {question1.content}\n**Bug**: {question2.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')

    if str(payload.emoji) == '<a:Money:861451984376692777>' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "<a:Money:861451984376692777>"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(title="Question 1",
                          description=f"What is your IGN?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(title="Question 2",
                          description=f"What did you purchase?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        c = discord.Embed(title="Question 3",
                          description=f"What issue are you facing?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=c)

        question3 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**IGN**: {question1.content}\n**Purchase**: {question2.content} \n**Issue**: {question3.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')

    if str(payload.emoji) == '<a:Other:861447459828924436>' and (
            payload.message_id) == 861459457442447370:

        await client.wait_until_ready()

        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        category_channel = guild.get_channel(836099144984035348)
        ticketlog_channel = guild.get_channel(836102113892761671)
        ticket_channel = await category_channel.create_text_channel(
            "ticket-{}".format(ticket_number))
        await ticket_channel.set_permissions(guild.get_role(guild.id),
                                             send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = guild.get_role(role_id)

            await ticket_channel.set_permissions(role,
                                                 send_messages=True,
                                                 read_messages=True,
                                                 embed_links=True,
                                                 attach_files=True,
                                                 read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(payload.member,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

        staff_role = discord.utils.get(guild.roles, name="Support")

        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] != []:

            for role_id in data["pinged-roles"]:
                role = payload.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(
            title="GalaxyServers Tickets",
            description="Your ticket has been created at {}".format(
                ticket_channel.mention),
            color=0x00a8ff)

        em = discord.Embed(title="Ticket Logs",
                           description=f"",
                           color=0x00a8ff)
        em.add_field(name="Creator",
                     value=f"{payload.member.mention}",
                     inline=True)
        em.add_field(name="Ticket",
                     value=f"{ticket_channel.name}",
                     inline=True)

        await ticketlog_channel.send(embed=em)

        pp = guild.get_channel(payload.channel_id)

        await pp.send(embed=created_em, delete_after=10)

        await ticket_channel.send(
            f'{payload.member.mention}, please answer the following questions.'
        )

        await ticket_channel.send(
            '-----------------------------------------------')

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await client.fetch_user(payload.user_id)
        emoji = "<a:Other:861447459828924436>"
        await message.remove_reaction(emoji, user)

        def check(message):
            return message.channel == ticket_channel and message.author == payload.member

        a = discord.Embed(title="Question 1",
                          description=f"What is your IGN?",
                          color=0x00a8ff)

        await ticket_channel.send(embed=a)

        question1 = await client.wait_for('message', check=check)

        b = discord.Embed(
            title="Question 2",
            description=
            f"Please give us a description on why you made this ticket.",
            color=0x00a8ff)

        await ticket_channel.send(embed=b)

        question2 = await client.wait_for('message', check=check)

        staff_role = discord.utils.get(guild.roles, name="Support Team")
        staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

        x = f'Support will be with you shortly.'

        em = discord.Embed(
            title="Responses:",
            description=
            f"**IGN**: {question1.content}\n**Issue**: {question2.content}",
            color=0x00a8ff)

        msg = await ticket_channel.send(content=x, embed=em)

        await msg.add_reaction('🔒')


@client.event
async def on_raw_reaction_remove(payload):
    member = payload.member
    guild = await client.fetch_guild(payload.guild_id)
    sneakpeak = discord.utils.get(guild.roles, name="Sneak Peak")
    events = discord.utils.get(guild.roles, name="Events")
    devents = discord.utils.get(guild.roles, name="Discord Events")
    announcements = discord.utils.get(guild.roles, name="Announcements")
    giveaways = discord.utils.get(guild.roles, name="Giveaways")
    skyblock = discord.utils.get(guild.roles, name="Skyblock")
    survival = discord.utils.get(guild.roles, name="Survival")
    member = await guild.fetch_member(payload.user_id)

    if str(payload.emoji) == '👻' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(sneakpeak)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Sneak Peaks role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '💣' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(devents)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=
            f"You have succesfully removed the Discord Events role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '🧨' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(events)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Events role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '📣' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(announcements)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Announcements role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '🎁' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(giveaways)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Giveaways role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '<:Events:822321553420058665>' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(skyblock)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Skyblock role.",
            color=discord.Color.red())
        await member.send(embed=embed)

    if str(payload.emoji) == '<:Survival:836263182653063168>' and (
            payload.channel_id) == 821641676862521344:
        await member.remove_roles(survival)
        embed = discord.Embed(
            title="Removed Roles",
            url="",
            description=f"You have succesfully removed the Survival role.",
            color=discord.Color.red())
        await member.send(embed=embed)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def new(ctx, *, args=None):

    await client.wait_until_ready()

    if args == None:
        message_content = "Please be patient while I ask a few questions."

    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    category_channel = ctx.guild.get_channel(836099144984035348)
    ticketlog_channel = ctx.guild.get_channel(836102113892761671)
    ticket_channel = await category_channel.create_text_channel(
        "ticket-{}".format(ticket_number))
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id),
                                         send_messages=False,
                                         read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role,
                                             send_messages=True,
                                             read_messages=True,
                                             add_reactions=True,
                                             embed_links=True,
                                             attach_files=True,
                                             read_message_history=True,
                                             external_emojis=True)

    await ticket_channel.set_permissions(ctx.author,
                                         send_messages=True,
                                         read_messages=True,
                                         add_reactions=True,
                                         embed_links=True,
                                         attach_files=True,
                                         read_message_history=True,
                                         external_emojis=True)

    staff_role = discord.utils.get(ctx.guild.roles, name="Support Team")

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)

        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

    created_em = discord.Embed(
        title="Galaxy Tickets",
        description="Your ticket has been created at {}".format(
            ticket_channel.mention),
        color=0x00a8ff)

    em = discord.Embed(title="Ticket Logs", description=f"", color=0x00a8ff)
    em.add_field(name="Creator", value=f"{ctx.author.mention}", inline=True)
    em.add_field(name="Ticket", value=f"{ticket_channel.name}", inline=True)

    await ticketlog_channel.send(embed=em)

    await ctx.send(embed=created_em, delete_after=10)
    await ctx.message.delete()
    await ticket_channel.send(
        f'{ctx.author.mention}, please answer the following questions.')

    await ticket_channel.send('-----------------------------------------------'
                              )

    def check(message):
        return message.channel == ticket_channel and message.author == ctx.author

    a = discord.Embed(
        title="Question 1",
        description=
        f"Is your issue with our forums, discord, or an in-game server? (Please specify which server)",
        color=0x00a8ff)

    await ticket_channel.send(embed=a)

    question1 = await client.wait_for('message', check=check)

    b = discord.Embed(title="Question 2",
                      description=f"What is your IGN? (Forums username)",
                      color=0x00a8ff)

    await ticket_channel.send(embed=b)

    question2 = await client.wait_for('message', check=check)

    c = discord.Embed(title="Question 3",
                      description=f"Please explain your issue.",
                      color=0x00a8ff)

    await ticket_channel.send(embed=c)

    question3 = await client.wait_for('message', check=check)

    d = discord.Embed(
        title="Question 4",
        description=f"Please provide any evidence, if applicable.",
        color=0x00a8ff)

    await ticket_channel.send(embed=d)

    question4 = await client.wait_for('message', check=check)

    em = discord.Embed(
        title="Responses:",
        description=
        f"**Server**: {question1.content} \n**Name**: {question2.content}\n**Issue**: {question3.content} \n**Evidence**: {question4.content}",
        color=0x00a8ff)

    await ticket_channel.send(embed=em)

    staff_role = discord.utils.get(ctx.guild.roles, name="Support Team")
    staff_role2 = discord.utils.get(ctx.guild.roles, name="Staff Team")

    await ticket_channel.send(
        f'Support will be with you shortly. \n \n||Tags: {staff_role.mention} {staff_role2.mention}||'
    )


@client.command()
async def close(ctx):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower(
            ) == "close"

        try:
            ticketlog_channel = ctx.guild.get_channel(836102113892761671)
            em = discord.Embed(
                title="Galaxy Tickets",
                description=
                "Are you sure you want to close this ticket? Reply with `close` if you are sure.",
                color=0x00a8ff)

            await ctx.reply(embed=em)
            await client.wait_for('message', check=check, timeout=60)
            em = discord.Embed(title="Ticket Logs",
                               description=f"",
                               color=0x00a8ff)
            em.add_field(name="Closer",
                         value=f"{ctx.author.mention}",
                         inline=True)
            em.add_field(name="Ticket",
                         value=f"{ctx.channel.name}",
                         inline=True)

            await ticketlog_channel.send(embed=em)

            await ctx.reply('Ticket will close in 15 seconds.',
                            mention_author=False)

            await asyncio.sleep(15)

            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

        except asyncio.TimeoutError:
            em = discord.Embed(
                title="Galaxy Tickets",
                description=
                "You have run out of time to close this ticket. Please run the command again.",
                color=0x00a8ff)
            await ctx.send(embed=em)


@client.command()
async def addaccess(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(
                    title="Galaxy tickets",
                    description=
                    "You have successfully added `{}` to the list of roles with access to tickets."
                    .format(role.name),
                    color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(
                    title="Galaxy Tickets",
                    description=
                    "That isn't a valid role ID. Please try again with a valid role ID."
                )
                await ctx.send(embed=em)

        else:
            em = discord.Embed(
                title="Galaxy Tickets",
                description="That role already has access to tickets!",
                color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(
            title="Galaxy Tickets",
            description="Sorry, you don't have permission to run that command.",
            color=0x00a8ff)
        await ctx.send(embed=em)


@client.command()
async def delaccess(ctx, role_id=None):
    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            valid_roles = data["valid-roles"]

            if role_id in valid_roles:
                index = valid_roles.index(role_id)

                del valid_roles[index]

                data["valid-roles"] = valid_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(
                    title="Galaxy Tickets",
                    description=
                    "You have successfully removed `{}` from the list of roles with access to tickets."
                    .format(role.name),
                    color=0x00a8ff)

                await ctx.send(embed=em)

            else:

                em = discord.Embed(
                    title="Galaxy Tickets",
                    description=
                    "That role already doesn't have access to tickets!",
                    color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(
                title="Galaxy Tickets",
                description=
                "That isn't a valid role ID. Please try again with a valid role ID."
            )
            await ctx.send(embed=em)

    else:
        em = discord.Embed(
            title="Galaxy Tickets",
            description="Sorry, you don't have permission to run that command.",
            color=0x00a8ff)
        await ctx.send(embed=em)

@client.command()
@has_permissions(administrator=True)
async def addadminrole(ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        em = discord.Embed(
            title="Galaxy Tickets",
            description=
            "You have successfully added `{}` to the list of roles that can run admin-level commands!"
            .format(role.name),
            color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(
            title="Galaxy Tickets",
            description=
            "That isn't a valid role ID. Please try again with a valid role ID."
        )
        await ctx.send(embed=em)


@client.command()
@has_permissions(administrator=True)
async def deladminrole(ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)

            em = discord.Embed(
                title="Galaxy Tickets",
                description=
                "You have successfully removed `{}` from the list of roles that get pinged when new tickets are created."
                .format(role.name),
                color=0x00a8ff)

            await ctx.send(embed=em)

        else:
            em = discord.Embed(
                title="Galaxy Tickets",
                description=
                "That role isn't getting pinged when new tickets are created!",
                color=0x00a8ff)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(
            title="Galaxy Tickets",
            description=
            "That isn't a valid role ID. Please try again with a valid role ID."
        )
        await ctx.send(embed=em)


@client.command()
@has_permissions(administrator=True)
async def resolved(ctx):
    embed = discord.Embed(
        title='Resolved?',
        description=
        f'If the ticket is resolved, please type `.close` and follow those steps.',
        color=discord.Color.green())
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()


@client.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)
    await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)


@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cannot do that!")


@client.command()
@commands.has_permissions(administrator=True)
async def silentclean(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)


@client.command()
async def serverpfp(ctx):
    await ctx.send(f"{ctx.guild.icon_url}")


@client.command(aliases=['suggest'])
async def suggestion(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Suggestions",
        url="",
        description=f"I have started the suggestion process in your dms.",
        color=discord.Color.purple())
    await ctx.channel.send(embed=embed, delete_after=10)

    def check(message):
        return message.guild is None and message.author != client.user

    a = discord.Embed(title="Suggestions",
                      url="",
                      description=f"What server is this suggestion for?",
                      color=discord.Color.green())
    await ctx.author.send(embed=a)

    question1 = await client.wait_for('message', check=check)

    b = discord.Embed(title="Applications",
                      url="",
                      description=f"What is your suggestion?",
                      color=discord.Color.green())
    await ctx.author.send(embed=b)

    question2 = await client.wait_for('message', check=check)

    await question2.add_reaction('✅')

    suggestionslogs = client.get_channel(822050268011167764)

    embed = discord.Embed(
        title=f"Suggestion | From {ctx.author}",
        url="",
        description=
        f"**Server**: \n{question1.content} \n \n**Suggestion**: \n{question2.content}",
        color=discord.Color.purple())

    x = await suggestionslogs.send(embed=embed)

    await x.add_reaction('👍')
    await x.add_reaction('👎')

    return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        return
    elif isinstance(error, commands.MemberNotFound):
        return
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(
            f"Hey {ctx.author.mention}! You can't use that command yet! \n \nTry again in {error.retry_after:.2f}s.",
            delete_after=10)
        await ctx.message.delete()
    else:
        print('Ignoring exception in command {}:'.format(ctx.command),
              file=sys.stderr)
        traceback.print_exception(type(error),
                                  error,
                                  error.__traceback__,
                                  file=sys.stderr)


client.run('')
