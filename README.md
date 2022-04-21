# GalaxyServers
GalaxyServers Discord Bot


YOU MUST USE discord.py V2.0! Install it in a shell/cmd prompt using the following command "pip install -U git+https://github.com/Rapptz/discord.py"

# What Everything Within The Bot Does

## class PersistentView
This is to show you how buttons work and you can copy and paste this code to implement new buttons with responses.

## class PersistentViewBot
This class handles everything on startup. It changes the activity, initializes buttons, and the prefix(es).

## class Confirm
This class is the code that allows the user to verify and gain a role which gives them access to the rest of the server. This is to prevent servers from being botted.

## class ReactionRoles
This class handles self roles within buttons. You click on a button and you either get the role, or removes the role.

## class Link
This class handles links specific to the this server for voting the server.

## class Dropdown
This class allows the users when they join to determine where they came from.

## class DropdownView
For dropdown selections, you need a View class with it. This handles the timeout to make sure it won't stop working and it also makes the dropdown work overall.

## client = PersistentViewBot()
You can have either "bot" or "client" within the bot, I chose client, this makes commands for example `@client.command` work. If you chose "bot", you would use `@bot.command`

## Prepare Command
```@client.command(aliases=['test1'])
@commands.has_permissions(administrator=True)
async def prepare(ctx: commands.Context):
    await ctx.send("What's your favourite colour?", view=PersistentView())
```
    
This command is the commmand to get the PersistentView buttons which allows the user to click on a certain color and to test the buttons if you choose to update them. You must have administrator permissions to use this command.

## Reaction Roles Command
```@client.command()
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
```

This command displays the self roles ReactionRoles class. It sends an embed that gives you information on what button does what.

## Link Command
```@client.command()
async def link(ctx: commands.Context):
    view = Link()
    embed = discord.Embed(
        title="Voting Sites",
        url="",
        description=
        f"**Click the button to the corresponding vote site!** \n \n \n**Vote Link 1** - https://topg.org/minecraft-servers/server-632444 \n**Vote Link 2** - https://minecraftservers.org/server/620818 \n**Vote Link 3** - https://www.planetminecraft.com/server/galaxy-servers-5235600/ \n**Vote Link 4** - https://minecraft-mp.com/server-s285927 \n**Vote Link 5** - https://www.minecraft-servers-list.org/details/Olly_/",
        color=discord.Color.green())
    await ctx.send(embed=embed, view=view)
```
This command allows sends the Link button that allows the user to choose a button and vote for the Minecraft server associated with this specific bot.

## Verify Command
```@client.command(aliases=['test2'])
@commands.has_permissions(administrator=True)
async def verify(ctx: commands.Context):
    view = Confirm()
    await ctx.send('Click The Button To Verify!', view=view)
    await ctx.message.delete()
    await view.wait()
```
This command displays the Confirm button that gives the user a role to gain access to the rest of the server to prevent bot raids. You need administrator permissions to use this command.

## Question Command
```@client.command(aliases=['test3'])
@commands.has_permissions(administrator=True)
async def question(ctx):
    view = DropdownView()
    await ctx.message.delete()
    await ctx.send('How Did You Find Us?', view=view)
```
This command displays the DropdownView button that allows the user to specify where they found this discord server.

## client.remove_command('help')
This line of code removes the default `help` command from the bot as it's very ugly and no one likes how it looks. We will be adding our own custom help later down in this documentation.

## Reaction Roles
```@client.command()
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
```
In case the server owner didn't like how the buttons looked, I coded actual reaction roles instead as well. This is the same thing as the Self Roles command, but uses reactions rather than buttons. You need administrator permissions to use this command.

## RRAnti Command
```@client.command()
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
```
This code is specific for the staff section of this server. It's a reaction role that gives the user a certain role once they want to recieve notifications of someone hacking within the Minecraft server. You need administrator permissions to use this command.

## RRVerify Command
```@client.command()
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
```
This is once again a repeat of a button code. Instead of having the verification button (Confirm class) as a button, this allows administrators to use this command to use reaction roles rather than buttons. You need administrator permissions to use this command.

## RRTickets Command
```@client.command()
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
```
This command sends out the support ticket embed along with initialize the reactions to open support tickets. You need administrator permissions to use this command.

## Enlarge Command
```@client.command()
async def enlarge(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send("You need to provide an emoji!")
    else:
        await ctx.send(emoji.url)
```
This command makes a Discord Emoji into a PNG/Gif. This is helpful so you can add emojis to your own server if you wish.

## on_raw_reaction_add
All of the code between lines 362 and 1409 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle the reactions portion of this bot. This is specific to adding the reaction.

## on_raw_reaction_remove
All of the code between lines 1412 and 1494 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle the reaction roles portion of the bot. This is specific to removing the reaction.

## New Command
All of the code between lines 1497 and 1645 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle support tickets within a command. This is useful in case the server owner only wants a command to open a support ticket.

## Close Command
All of the code between lines 1648 and 1702 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle closing the support tickets within a command.

## AddAccess Command
All of the code between lines 1705 and 1765 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle adding a specific role to support tickets. This is useful in case the sever owner decides to want more support roles to help with tickets.

## DelAccess Command
All of the code between lines 1768 and 1834 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle removing a specific role from support tickets. This is once again useful in case the server owned wants to remove a support role from helping in tickets.

## AddAdminRole Command
All of the code between lines 1836 and 1866 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle adding an admin role to the ticket system. Some commands have restrictions and require you to have an admin role within the ticket system.

## DelAdminRole Command
All of the code between lines 1869 and 1914 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle deleting an admin role from the ticket system.

## Resolved Command
```@client.command()
@has_permissions(administrator=True)
async def resolved(ctx):
    embed = discord.Embed(
        title='Resolved?',
        description=
        f'If the ticket is resolved, please type `.close` and follow those steps.',
        color=discord.Color.green())
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()
```
This ticket asks the user that created a support ticket to see if there's anything else the support member can help with, if not it mentions the command that they can close the ticket with.

## Clean Command
```@client.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)
    await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)
```
This command deletes the specified number of messages within a channel. This is useful for dealing with spammers.

## clear_error
```@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cannot do that!")
```
These lines of code tell the user if they don't have the required permissions to use the `clean` command.

## SilentClean
```@client.command()
@commands.has_permissions(administrator=True)
async def silentclean(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)
```
This is the same code as the `clean` command, with the same reasons, but it doesn't send a message once it is done deleting the messages.

## ServerPFP Command
```@client.command()
async def serverpfp(ctx):
    await ctx.send(f"{ctx.guild.icon_url}")
```
This command sends the current server profile picture. This is useful to make the profile picture into a gif/png file.

## Suggestion Command
```@client.command(aliases=['suggest'])
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
```
This command sends a suggestion to the specified suggestion channel for admins to review and potentially add to improve the server.

## on_command_error
All of the code between lines 2001 and 2020 of (https://github.com/FroostySnoowman/GalaxyServers/blob/main/main.py) handle errors the bot may encounter. No one likes a messy console, so this negates some errors and prints others. It is also used to show how many seconds left a user has on a specific command's cooldown.

`client.run('')`
This is where you input your bot's secret token. **DO NOT SHARE THIS TOKEN TO ANYONE**. If the token is wrong, it will not run your bot.
