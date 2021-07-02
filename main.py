import discord
import random
import json
import emoji
import os
import datetime
import asyncio
import pytz
import traceback
import sys

from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
from discord.ext import commands

from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = [".", "g!"], intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	activity = discord.Game(name="Galaxy Servers", type=3)
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	print('Signed in as {0.user}'.format(client))

@client.event
async def on_message(message):
    galaxyservers = client.get_guild(821595276837781506)
    ticketchannel = client.get_channel(836099435632918528)
    suggestionchannel = client.get_channel(822050268011167764)
    if message.content != "g!new" and (message.channel == ticketchannel) and (message.author.id != 503641822141349888) and (message.author.id != 822328755913359380) and (message.author.id != 211166495781289985):
        await message.delete()
        embed=discord.Embed(title="Message Error", url="", 
        description="You can only type `g!new` here!", 
        color=discord.Color.red())
        await message.author.send(embed=embed, delete_after=10)
    if message.content != "g!suggestion" and (message.channel == suggestionchannel) and (message.author.id != 503641822141349888) and (message.author.id != 822328755913359380) and (message.author.id != 211166495781289985):
        await message.delete()
        embed=discord.Embed(title="Message Error", url="", 
        description="You can only type `g!new` here!", 
        color=discord.Color.red())
        await message.author.send(embed=embed, delete_after=10)
    prefixes = ["!","@","#","$","%","^","&","*","/","~"]  
    if message.content.startswith("prefix"):
      await message.channel.send("My Prefix Is: **g!**")
    for prefix in prefixes:
        if message.content.startswith(prefix + "prefix"):
            await message.channel.send("My Prefix Is: **m!**")
    await client.process_commands(message)

@client.command()
@commands.has_permissions(administrator=True)
async def rr(ctx):
    embed=discord.Embed(title="Roles", url="", 
    description=f"👻 - **Sneak Peaks** \n \n💣 - **Discord Events** \n \n🧨 - **Events** \n \n📣 - **Announcements** \n \n🎁 - **Giveaways** \n \n<:Events:822321553420058665> - **Skyblock** \n \n<:Survival:836263182653063168> - **Survival**", 
    color=discord.Color.purple())
    embed.set_footer(text=f"Reaction Roles")
    x = "[@everyone]"
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
async def rrtickets(ctx):
    embed=discord.Embed(title="Tickets", url="", 
    description=f'For general support, click the "📩" reaction.', 
    color=discord.Color.purple())
    embed.set_footer(text=f"Reaction Roles")
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('📩')
    await ctx.message.delete()
        
@client.event
async def on_raw_reaction_add(payload):
  g = payload.guild_id
  guild = client.get_guild(g)
  member = guild.get_member(payload.user_id)
  if member.bot:
    return
  guild = client.get_guild(payload.guild_id)
  sneakpeak = discord.utils.get(guild.roles, name="Sneak Peak")
  events = discord.utils.get(guild.roles, name="Events")
  devents = discord.utils.get(guild.roles, name="Discord Events")
  announcements = discord.utils.get(guild.roles, name="Announcements")
  giveaways = discord.utils.get(guild.roles, name="Giveaways")
  skyblock = discord.utils.get(guild.roles, name="Skyblock")
  survival = discord.utils.get(guild.roles, name="Survival")
  events = discord.utils.get(guild.roles, name="Events")
  member = guild.get_member(payload.user_id)
    
  if str(payload.emoji) == '👻' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(sneakpeak)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Sneak Peaks role.", 
     color=discord.Color.green())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '💣' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(devents)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Discord Events role.", 
     color=discord.Color.green())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '🧨' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(events)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Events role.", 
     color=discord.Color.green())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '📣' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(announcements)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Announcements role.", 
     color=discord.Color.green())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '🎁' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(giveaways)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Giveaways role.", 
     color=discord.Color.green())
     await member.send(embed=embed)

  if str(payload.emoji) == '<:Events:822321553420058665>' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(skyblock)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Skyblock role.", 
     color=discord.Color.green())
     await member.send(embed=embed)

  if str(payload.emoji) == '<:Survival:836263182653063168>' and (payload.channel_id) == 821641676862521344:
     await member.add_roles(survival)
     embed=discord.Embed(title="Added Roles", url="", 
     description=f"You have succesfully added the Survival role.", 
     color=discord.Color.green())
     await member.send(embed=embed)


  if str(payload.emoji) == '🔒':
    with open('data.json') as f:
      data = json.load(f)

    if payload.channel_id in data["ticket-channel-ids"]:
      channel = client.get_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      user = client.get_user(payload.user_id)
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
        em.add_field(name="Closer", value=f"{payload.member.mention}", inline=True)
        em.add_field(name="Ticket", value=f"{payload.channel_id}", inline=True)
        time = datetime.now(tz=pytz.timezone('America/Denver'))
        formatted = time.strftime("%m/%d/%y, %I:%M %p")
        em.set_footer(text=formatted)

        await ticketlog_channel.send(embed=em)

        await message.reply('Ticket will close in 15 seconds.')

        await asyncio.sleep(15)

        await message.channel.delete()

        index = data["ticket-channel-ids"].index(payload.channel_id)
        del data["ticket-channel-ids"][index]

        with open('data.json', 'w') as f:
          json.dump(data, f)

      except asyncio.TimeoutError:
        await member.send('pp')
  
  if str(payload.emoji) == '📩' and (payload.message_id) == 858167499294900234:

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
      with open ("data.json", 'w') as f:
        json.dump(data, f)

      created_em = discord.Embed(
        title="GalaxyServers Tickets",
        description="Your ticket has been created at {}".format(
          ticket_channel.mention),
        color=0x00a8ff)

      em = discord.Embed(title="Ticket Logs",
                          description=f"",
                          color=0x00a8ff)
      em.add_field(name="Creator", value=f"{payload.member.mention}", inline=True)
      em.add_field(name="Ticket", value=f"{ticket_channel.name}", inline=True)
      time = datetime.now(tz=pytz.timezone('America/Denver'))
      formatted = time.strftime("%m/%d/%y, %I:%M %p")
      em.set_footer(text=formatted)

      await ticketlog_channel.send(embed=em)

      pp = guild.get_channel(payload.channel_id)

      await pp.send(embed=created_em, delete_after=10)

      await ticket_channel.send(
        f'{payload.member.mention}, please answer the following questions.'
      )

      await ticket_channel.send('-----------------------------------------------')

      channel = client.get_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      user = client.get_user(payload.user_id)
      emoji = "📩"
      await message.remove_reaction(emoji, user)


      def check(message):
        return message.channel == ticket_channel and message.author == payload.member

      a = discord.Embed(title="Question 1",
                        description=f"Is your issue with our forums, discord, or an in-game server? (Please specify which server)",
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

      d = discord.Embed(title="Question 4",
                        description=f"Please provide any evidence, if applicable",
                        color=0x00a8ff)

      await ticket_channel.send(embed=d)

      question4 = await client.wait_for('message', check=check)

      staff_role = discord.utils.get(guild.roles, name="Support Team")
      staff_role2 = discord.utils.get(guild.roles, name="Staff Team")

      x = f'Support will be with you shortly.'

      em = discord.Embed(title="Responses:",
                        description=f"**Server**: {question1.content} \n**Name**: {question2.content}\n**Issue**: {question3.content} \n**Evidence**: {question4.content}",
                        color=0x00a8ff)
      
      msg = await ticket_channel.send(content=x, embed=em)

      await msg.add_reaction('🔒')
    
@client.event
async def on_raw_reaction_remove(payload):
  member = payload.member
  guild = client.get_guild(payload.guild_id)
  sneakpeak = discord.utils.get(guild.roles, name="Sneak Peak")
  events = discord.utils.get(guild.roles, name="Events")
  devents = discord.utils.get(guild.roles, name="Discord Events")
  announcements = discord.utils.get(guild.roles, name="Announcements")
  giveaways = discord.utils.get(guild.roles, name="Giveaways")
  skyblock = discord.utils.get(guild.roles, name="Skyblock")
  survival = discord.utils.get(guild.roles, name="Survival")
  member = guild.get_member(payload.user_id)
    
  if str(payload.emoji) == '👻' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(sneakpeak)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Sneak Peaks role.", 
     color=discord.Color.red())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '💣' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(devents)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Discord Events role.", 
     color=discord.Color.red())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '🧨' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(events)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Events role.", 
     color=discord.Color.red())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '📣' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(announcements)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Announcements role.", 
     color=discord.Color.red())
     await member.send(embed=embed)
        
  if str(payload.emoji) == '🎁' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(giveaways)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Giveaways role.", 
     color=discord.Color.red())
     await member.send(embed=embed)

  if str(payload.emoji) == '<:Events:822321553420058665>' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(skyblock)
     embed=discord.Embed(title="Removed Roles", url="", 
     description=f"You have succesfully removed the Skyblock role.", 
     color=discord.Color.red())
     await member.send(embed=embed)

  if str(payload.emoji) == '<:Survival:836263182653063168>' and (payload.channel_id) == 821641676862521344:
     await member.remove_roles(survival)
     embed=discord.Embed(title="Removed Roles", url="", 
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

	em = discord.Embed(title="Ticket Logs",
	                   description=f"",
	                   color=0x00a8ff)
	em.add_field(name="Creator", value=f"{ctx.author.mention}", inline=True)
	em.add_field(name="Ticket", value=f"{ticket_channel.name}", inline=True)
	time = datetime.now(tz=pytz.timezone('America/Denver'))
	formatted = time.strftime("%m/%d/%y, %I:%M %p")
	em.set_footer(text=formatted)

	await ticketlog_channel.send(embed=em)

	await ctx.send(embed=created_em, delete_after=10)
	await ctx.message.delete()
	await ticket_channel.send(
	    f'{ctx.author.mention}, please answer the following questions.'
	)

	await ticket_channel.send('-----------------------------------------------')

	def check (message):
		return message.channel == ticket_channel and message.author == ctx.author

	a = discord.Embed(title="Question 1",
	                   description=f"Is your issue with our forums, discord, or an in-game server? (Please specify which server)",
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

	d = discord.Embed(title="Question 4",
	                   description=f"Please provide any evidence, if applicable.",
	                   color=0x00a8ff)

	await ticket_channel.send(embed=d)

	question4 = await client.wait_for('message', check=check)

	em = discord.Embed(title="Responses:",
	                   description=f"**Server**: {question1.content} \n**Name**: {question2.content}\n**Issue**: {question3.content} \n**Evidence**: {question4.content}",
	                   color=0x00a8ff)

	await ticket_channel.send(embed=em)

	staff_role = discord.utils.get(ctx.guild.roles, name="Support Team")
	staff_role2 = discord.utils.get(ctx.guild.roles, name="Staff Team")

	await ticket_channel.send(f'Support will be with you shortly. \n \n||Tags: {staff_role.mention} {staff_role2.mention}||')

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
			em.add_field(name="Closer", value=f"{ctx.author.mention}", inline=True)
			em.add_field(name="Ticket", value=f"{ctx.channel.name}", inline=True)
			time = datetime.now(tz=pytz.timezone('America/Denver'))
			formatted = time.strftime("%m/%d/%y, %I:%M %p")
			em.set_footer(text=formatted)

			await ticketlog_channel.send(embed=em)

			await ctx.reply('Ticket will close in 15 seconds.', mention_author=False)

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
async def addpingedrole(ctx, role_id=None):

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

		if role_id not in data["pinged-roles"]:

			try:
				role = ctx.guild.get_role(role_id)

				with open("data.json") as f:
					data = json.load(f)

				data["pinged-roles"].append(role_id)

				with open('data.json', 'w') as f:
					json.dump(data, f)

				em = discord.Embed(
				    title="Galaxy Tickets",
				    description=
				    "You have successfully added `{}` to the list of roles that get pinged when new tickets are created!"
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
			    description=
			    "That role already receives pings when tickets are created.",
			    color=0x00a8ff)
			await ctx.send(embed=em)

	else:
		em = discord.Embed(
		    title="Galaxy Tickets",
		    description="Sorry, you don't have permission to run that command.",
		    color=0x00a8ff)
		await ctx.send(embed=em)


@client.command()
async def delpingedrole(ctx, role_id=None):

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

			pinged_roles = data["pinged-roles"]

			if role_id in pinged_roles:
				index = pinged_roles.index(role_id)

				del pinged_roles[index]

				data["pinged-roles"] = pinged_roles

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
				    "That role already isn't getting pinged when new tickets are created!",
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
async def serverpfp(ctx):
  await ctx.send(f"{ctx.guild.icon_url}")

@client.command()
async def apply(ctx):

    await ctx.message.delete()
    embed=discord.Embed(title="Applications", url="", 
    description=f"I have started the application process in your dms.", 
    color=discord.Color.purple())
    await ctx.channel.send(embed=embed, delete_after=10)

    def check(message):
      return message.guild is None and message.author != client.user

    a = discord.Embed(title="Applications", url="", 
    description=f"Would you like to start the application process? `Y` for Yes, `N` for No.", 
    color=discord.Color.green())
    await ctx.author.send(embed=a)

    question1 = await client.wait_for('message', check=check)

    if question1.content in ("Y", "Yes", "y", "yes"):

      b = discord.Embed(title="Applications", url="", 
        description=f"What is your Minecraft IGN?", 
      color=discord.Color.green())
      await ctx.author.send(embed=b)

      question2 = await client.wait_for('message', check=check)

      c = discord.Embed(title="Applications", url="", 
        description=f"What gamemode are you applying for?", 
      color=discord.Color.green())
      await ctx.author.send(embed=c)

      question3 = await client.wait_for('message', check=check)

      d = discord.Embed(title="Applications", url="", 
        description=f"What are your pronouns?", 
      color=discord.Color.green())
      await ctx.author.send(embed=d)

      question4 = await client.wait_for('message', check=check)

      e = discord.Embed(title="Applications", url="", 
        description=f"How old are you?", 
      color=discord.Color.green())
      await ctx.author.send(embed=e)

      question5 = await client.wait_for('message', check=check)

      f = discord.Embed(title="Applications", url="", 
        description=f"What is your timezone?", 
      color=discord.Color.green())
      await ctx.author.send(embed=f)

      question6 = await client.wait_for('message', check=check)

      g = discord.Embed(title="Applications", url="", 
        description=f"What rank are you applying for?", 
      color=discord.Color.green())
      await ctx.author.send(embed=g)

      question7 = await client.wait_for('message', check=check)

      h = discord.Embed(title="Applications", url="", 
        description=f"Why do you think you suit this rank?", 
      color=discord.Color.green())
      await ctx.author.send(embed=h)

      question8 = await client.wait_for('message', check=check)

      i = discord.Embed(title="Applications", url="", 
        description=f"What type of experience do you have?", 
      color=discord.Color.green())
      await ctx.author.send(embed=i)

      question9 = await client.wait_for('message', check=check)

      j = discord.Embed(title="Applications", url="", 
        description=f"Why should we pick you over others?", 
      color=discord.Color.green())
      await ctx.author.send(embed=j)

      question10 = await client.wait_for('message', check=check)

      k = discord.Embed(title="Applications", url="", 
        description=f"Do you have any other hobbies outside of Minecraft?", 
      color=discord.Color.green())
      await ctx.author.send(embed=k)

      question11 = await client.wait_for('message', check=check)

      l = discord.Embed(title="Applications", url="", 
        description=f"How many hours a week can you dedicate to staffing?", 
      color=discord.Color.green())
      await ctx.author.send(embed=l)

      question12 = await client.wait_for('message', check=check)

      m = discord.Embed(title="Applications", url="", 
        description=f"Do you understand that asking an admin to check your application will result in your application being denied?", 
      color=discord.Color.green())
      await ctx.author.send(embed=m)

      question13 = await client.wait_for('message', check=check)

      n = discord.Embed(title="Applications", url="", 
        description=f"Would you like to submit this application? Type `yes` to submit it or `no` to cancel it.", 
      color=discord.Color.green())
      await ctx.author.send(embed=n)

      question14 = await client.wait_for('message', check=check)

      if question14.content in ("yes", "Yes"):
      
        await question14.reply('Thank you, it has been sent.')

        applicationlogs =  client.get_channel(836249012889190500)

        with open("applications.json") as f:
          data = json.load(f)

        application_number = int(data["application-counter"])
        application_number += 1

        embed=discord.Embed(title=f"Application #{application_number} | {ctx.author}", url="", 
        description=f"**Question 1**: What is your Minecraft IGN? \n**Answer**: {question2.content}\n \n**Question 2**: What gamemodes are you applying for? \n **Answer**: {question3.content} \n \n**Question 2**: What are your pronouns? \n**Answer**: {question4.content} \n \n**Question 3**: How old are you? \n**Answer**: {question5.content} \n \n**Question 4**: What is your time zone? \n**Answer**: {question6.content} \n \n**Question 5**: What rank are you applying for? \n**Answer**: {question7.content} \n \n**Question 6**: Why do you think you suite this rank? \n**Answer**: {question8.content} \n \n**Question 7**: What type of experience do you have? \n **Answer**: {question9.content} \n \n**Question 8**: Why should we pick you over others? \n**Answer**: {question10.content} \n \n**Question 9**: Do you have any other hobbies outside of Minecraft? \n**Answer**: {question11.content} \n \n**Question 10**: How many hours a week can you dedicate to staffing? \n**Answer**: {question12.content} \n \n**Question 11**: Do you understand that asking an admin to check your application will result in your application being denied? \n**Answer**: {question13.content}", 
        color=discord.Color.purple())

        data["application-counter"] = int(application_number)
        with open("applications.json", 'w') as f:
          json.dump(data, f)

        await applicationlogs.send(embed=embed)

    if question12.content in ("no", "No"):

      embed=discord.Embed(title="Applications", url="", 
        description=f"The application process has been canceled.", 
      color=discord.Color.green())

      await ctx.author.send(embed=embed)

      await question12.reply('The application process has failed.')

      return
      
@client.command(aliases=['suggest'])
async def suggestion(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Suggestions", url="", 
    description=f"I have started the suggestion process in your dms.", 
    color=discord.Color.purple())
    await ctx.channel.send(embed=embed, delete_after=10)

    def check(message):
      return message.guild is None and message.author != client.user

    a = discord.Embed(title="Suggestions", url="", 
    description=f"What server is this suggestion for?", 
    color=discord.Color.green())
    await ctx.author.send(embed=a)

    question1 = await client.wait_for('message', check=check)

    b = discord.Embed(title="Applications", url="", 
    description=f"What is your suggestion?", 
    color=discord.Color.green())
    await ctx.author.send(embed=b)

    question2 = await client.wait_for('message', check=check)
      
    await question2.add_reaction('✅')

    suggestionslogs =  client.get_channel(822050268011167764)

    embed=discord.Embed(title=f"Suggestion | From {ctx.author}", url="", 
    description=f"**Server**: \n{question1.content} \n \n**Suggestion**: \n{question2.content}", 
    color=discord.Color.purple())

    x = await suggestionslogs.send(embed=embed)

    await x.add_reaction('👍')
    await x.add_reaction('👎')

    return

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
      return
  elif isinstance(error, commands.MemberNotFound):
      return
  elif isinstance(error, commands.CommandOnCooldown):
      await ctx.channel.send(f"Hey {ctx.author.mention}! You can't use that command yet! \n \nTry again in {error.retry_after:.2f}s.", delete_after=10)
      await ctx.message.delete()
  else:
      print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
      traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

client.run('')
