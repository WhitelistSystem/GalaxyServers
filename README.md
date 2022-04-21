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
    
This command
