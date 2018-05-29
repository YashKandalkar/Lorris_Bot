#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
print("Strarting")
import discord
from discord.ext import commands
import asyncio
import random
import itertools 
import urllib.request
from bs4 import BeautifulSoup as bs
import re 
import urllib 
from imagesoup import ImageSoup
from random import randint
import requests 
import os 
import aiohttp
from PIL import Image, ImageDraw, ImageFont 
import googlesearch 
import math 
from Paginator import Paginator

    
bot = commands.Bot(description="just another bot", command_prefix=["L+","lorris, ", "Lorris, "] )
    
#tic tac toe 
channels_with_gameON = {}
coordinates = {1 : (40, 0), 2 : (210, 0), 3 : (370, 0), 4 : (40, 160), 5 : (210, 160), 6 : (370, 160), 7 : (40, 320), 8 : (210, 320), 9 : (370, 320)}
sessions = {}                     #1st is list of players, 2nd is 2 list of player's choices, 3rd is image object, 4th is turn
session_ids = []
   
#welcome msg
welcome_messages = {}
    
def is_owner(ctx):
     if ctx.message.author.id == "388984732156690433":
           return True
     return False
    
    
jokes = 'https://icanhazdadjoke.com/'
     
server_id = {}
    
'''
@bot.event
async def on_command_error(error, ctx):
  if isinstance(error, commands.CommandOnCooldown):
    await bot.send_message(ctx.message.channel, ":x:Sorry, you are on a cooldown. Try again in " + str(round(int(error.retry_after), 2)) + "s")
  else: 
    print(error)
'''
    
@bot.event
async def on_message_edit(before, after):
  await bot.process_commands(after)

@bot.event
async def on_ready():
  bot.load_extension("repl") 
  print("Ready")
    
@bot.event
async def on_message(msg):
 if not msg.author.bot: 
  if "lorris" in msg.content.lower():
     await bot.send_message(msg.channel, "Someone called me?") 
  if "<@388984732156690433>" in msg.content: 
    await bot.add_reaction(msg, emoji= ":candy:")
      
  #block invites
  if msg.server.id in server_id:                                                                                
    if msg.channel.id in server_id[msg.server.id][0]:
      if 'blockInvites' in server_id[msg.server.id][1]:
        if 'https://discord.gg/' in msg.content: 
          await bot.delete_message(msg)
          em = discord.Embed(title='Warning!', description="Sorry, {}, invites links in this channel are prohobited.".format(msg.author.mention), colour=discord.Colour.red())
          await bot.send_message(msg.channel, embed=em)
 await  bot.process_commands(msg)
    
    
    
class Fun:
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def spoonerism(self, x, y):
     '''Change the first character of two words'''
     p=list(x)
     q=list(y)
     p[0],q[0]=q[0],p[0]
     x = ''.join(p)
     y = ''.join(q)
     await bot.say(x+"\n"+y)
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def angry(self, x:int=1): 
    '''Show your anger in a better way'''
    if x>5:
      await bot.say("Angry? Grab a snickers")
    elif x <=0:
      await bot.say("Use some brain")
    else: 
      await bot.say(":rage:"*x)
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def laugh(self, x:int=1): 
    '''Laugh'''
    if x>5:
      await bot.say("You'll die laughing")
    elif x <=0:
      await bot.say("Use some brain")
    else: 
      await bot.say(":joy:"*x)
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def facepalm(self, x:int=1): 
    '''Tell how stupid they are'''
    if x>5:
      await bot.say("I know the world is stupid")
    elif x <=0:
      await bot.say("Use some brain")
    else: 
      await bot.say(":facepalm:"*x)

  
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def kys(self, *, text): 
    """The kill yourself meme""" 
          
    text = text.replace('|','\n')
    kys = Image.open("images/images/kys.jpg")
    font = ImageFont.truetype("fonts/fonts/HussarBd.otf", 30)
    draw = ImageDraw.Draw(kys)
    draw.text((30,25),text,(255,255,255),font=font)
    draw = ImageDraw.Draw(kys)
    kys.save("kyss.jpg")
    await bot.upload("kyss.jpg")
    os.remove("kyss.jpg")
  
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def troll(self, mem: discord.Member):
    '''Troll someone'''
    im = Image.open("images/images/stepped_on_shit.jpg")
    async with aiohttp.ClientSession() as cs: 
      async with cs.get(mem.avatar_url) as ava: 
        with open("image.jpg",'wb') as avatar: 
          avatar.write(await ava.read())
    
    temp = Image.open("image.jpg")
    temp = temp.resize((150,150))
    im.paste(temp, box=(220,690))
    im.save("edited.jpg")
    await bot.upload("edited.jpg")
    os.remove("edited.jpg")
    os.remove("image.jpg")
     
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def graphp(self, f):
    '''Plot (x,y) in a graph. WIP'''
    im = Image.open("images/images/test-2.jpg")
    d=ImageDraw.Draw(im)
    
    func = lambda x: eval(f)
    
    for i in range(-250,251): 
      try: 
        x = i+250
        y = 500-(func(i)+250) 
      except: continue
      d.point((x, y), fill =(0,0,0))
    
    im.save("test.jpg")
    await asyncio.sleep(0.2)
    await bot.upload("test.jpg")
    await asyncio.sleep(0.2)
    os.remove("test.jpg")
    
    
  @commands.cooldown(rate=1,per=10,type=commands.BucketType.user)
  @commands.command() 
  async def graph(self, f):
    '''Plot the points in a graph and join them; hence making a line. WIP'''
    im = Image.open("images/images/test-2.jpg")
    d=ImageDraw.Draw(im)
    
    func = lambda x: eval(f)
    
    for i in range(-250,251): 
      try: 
        x1 = i+250
        y1 = 500-(func(i)+250)
        x2 = i+251
        y2 = 500-(func(i+1)+250) 
      except: continue
      d.line([(x1, y1),(x2,y2)], fill =(0,0,255))
    
    im.save("test.jpg")
    await asyncio.sleep(0.2)
    await bot.upload("test.jpg")
    await asyncio.sleep(0.2)
    os.remove("test.jpg")
    
    
class Admins:
  
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
  @commands.command(pass_context=True) 
  async def purge(slef, ctx, x:int): 
    '''Command for admins to delete some amount of messages'''
    if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:
      msg = await bot.purge_from(ctx.message.channel,check=None, limit=x)
      em = discord.Embed(title='Purged:', description='Deleted {} message(s)'.format(len(msg)), colour=discord.Colour.green())
      await bot.say(embed=em)
    else: 
      em = discord.Embed(title=ctx.message.author.name, description="Sorry, command only for admins", colour=discord.Colour.red())
      await bot.say(embed=em)
    
  @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
  @commands.command(pass_context=True)
  async def warn(self, ctx, mem:discord.Member, *, reason): 
    "Usage: 'user' 'warning'"
    em = discord.Embed(title="WARNING",description="You have been warned by {0}".format(ctx.message.author.name),color=discord.Color.red())
    em.add_field(name="Warned by: ", value=ctx.message.author.name)
    em.add_field(name="Top Role: ", value=ctx.message.author.top_role.name)
    em.add_field(name="Reason: ", value=reason)
    em.add_field(name="server: ", value=ctx.message.server.name)
    if dict(ctx.message.channel.permissions_for(ctx.message.author))['administrator'] or ctx.message.author.id=='388984732156690433':
      await bot.send_message(mem, embed=em)
      await bot.say("{0} warned {1}".format(ctx.message.author.name, mem.name))
    else: 
      em = discord.Embed(title=ctx.message.author.name+":", description="Sorry, command only for admins", colour=discord.Colour.red())
      await bot.send_message(ctx.message.channel, embed=em)
     
    
class Useful:
    
  @commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
  @commands.command(pass_context=True,aliases=["PING"])
  async def ping(self, ctx):
    '''ping the bot'''
    em = discord.Embed(title="Pong!")
    pongmsg = await bot.send_message(ctx.message.channel, embed=em)
    def timedelta_milliseconds(td):
      return td.days * 86400000 + td.seconds * 1000 + td.microseconds / 1000
    ms = abs(int(timedelta_milliseconds(pongmsg.timestamp - ctx.message.timestamp)))
    if ms < 70:
      em.colour = discord.Colour.green() 
    elif ms > 70 and ms < 130:
      em.colour = discord.Colour(0xFFFF00)
    else:
      em.colour = discord.Colour.red() 
    em.description = "Took: " + str(ms) +"ms"
    await bot.edit_message(pongmsg, embed=em)
     
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def define(self, query):
    '''Get the meaning of a word'''
    url = "http://www.dictionary.com/browse/{}?s=t".format(query)
    async with aiohttp.ClientSession() as cs:
      async with cs.get(url) as response:
        html = await response.read()
    soup = bs(html, 'html.parser')
    meaning = soup.find(attrs={'class':'def-content'}).text.strip()
    example = soup.find(attrs={'class':'def-block def-inline-example'}).text.strip()
    em = discord.Embed(title=query, color=discord.Colour.green(), url="http://www.dictionary.com")
    em.add_field(name="Meaning", value=meaning, inline=False)
    em.add_field(name="Example", value=example, inline=False)
    await bot.say(embed=em)
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def search(self, *, query):
    '''Google something'''
    listSearch=[]
    em = discord.Embed(title="This is what I've found:") 
    for i in googlesearch.search(query, stop=2, pause=0.5):
      em.description = i
      break
    for u in googlesearch.search(query, start=2, stop=5):
      listSearch.append(u)
    em.add_field(name="See Also:", value='\n'.join(listSearch))
    em.set_footer(text = "Data from google.com©")
    await bot.say(embed=em)

  @commands.command()
  async def inviteme(self):
    '''Invite me to a server'''
    await bot.say(discord.utils.oauth_url(bot.user.id))
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)    
  @commands.command(pass_context=True)
  async def dp(self, ctx, mem:discord.Member=None):
    '''See someone's profile photo'''
    mem = mem or ctx.message.author
    em = discord.Embed(title="{}'s avatar".format(mem.name))
    em.set_image(url=mem.avatar_url)
     
    async with aiohttp.ClientSession() as cs:
      async with cs.get(mem.avatar_url) as r:
        with open("tempava.jpg",'wb') as ava:
          ava.write(await r.read())
 
    im = Image.open("tempava.jpg").convert("RGB")
    im = im.resize((510,510))
    d = list(im.getdata())
    r, g, b = 0, 0, 0
    for q,w,e in d:
      r += q
      g += w
      b += e
    hex_colour = '%02x%02x%02x' % (int(r/len(d)), int(g/len(d)), int(b/len(d)))
    em.colour = discord.Colour(int(hex_colour, 16))
    await bot.say(embed=em)
 
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command(pass_context=True)
  async def emoji(self, ctx, emote):
    '''Make your emojis BIG'''
    emote = emote.split(':')
    id = emote[-1].replace('>','')
    name = emote[1] 
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://discordapp.com/api/emojis/{}.png'.format(id)) as r:
        with open(name+'.png', 'wb') as f:
          f.write(await r.read())
    await bot.send_file(ctx.message.channel, name+'.png')
    await asyncio.sleep(0.3)
    os.remove(name+'.png')
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command() 
  async def image(self, *, x):
    ''' Quickly search an image '''
    soup = ImageSoup()
    images = soup.search(x, n_images=25)
    image = images[randint(0,24)]
    await bot.say(image.URL)
    
     
    
class math: 
    
  @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
  @commands.command()
  async def factorial(self, x:int):
    '''Calculate factorial of a number'''
    if type(x) == int and x > 0:
      if x > 100000:
        em = discord.Embed(description="Enter a number between **1 to 100000**", colour=discord.Colour.red())
        await bot.say(embed = em)
      else:
        fact = 1
        while x > 1:
          fact*=x
          x-=1
        await bot.say("```"+fact+"```")
    else: 
      em = discord.Embed(description="Enter a number between **1 to 100000**", colour=discord.Colour.red())
      await bot.say(embed = em)
    
    
    
class Security: 
    @commands.command(pass_context=True, description = "Usage: [all|this] [true|false]")
    async def blockInvites(self, ctx, channels, option):
      '''Block Invites from a channel or the whole server'''
      if dict(ctx.message.channel.permissions_for(ctx.message.author))['administrator'] or dict(ctx.message.channel.permissions_for(ctx.message.author))['manage_server']:
             
             
         if ctx.message.server.id in server_id:
             server_id[ctx.message.server.id][1].append('blockInvites')
             if ctx.message.channel.id in server_id[ctx.message.server.id][0]:
                 if channels == 'this':
                      if option == 'true':
                         await bot.say("Block invites feature is already enabled for this channel.✅")
                      elif option == 'false':
                         server_id[ctx.message.server.id][0].remove(ctx.message.channel.id)
                         await bot.say("Invite links won't be blocked from this channel.")
                 elif channels == 'all':
                      if option == 'true':
                         for i in ctx.message.server.channels:
                             server_id[ctx.message.server.id][0].append(i.id)
                         await bot.say("Blocking invite links from all the channels.✅")
                      elif option == 'false':
                         for i in range(len(server_id[ctx.message.server.id][0])):
                                  server_id[ctx.message.server.id][0].pop()
                         await bot.say("Invite links won't be blocked in any of the channels.")
             elif ctx.message.channel.id not in server_id[ctx.message.server.id][0]:
                 if option == 'true':
                      if channels == 'this':
                         server_id[ctx.message.server.id][0].append(ctx.message.channel.id)
                         await bot.say("Invite links will be blocked from this channel.✅")
                      elif channels == 'all':
                         for i in ctx.message.server.channels:
                                  server_id[ctx.message.server.id][0].append(i.id)
                         await bot.say("Blocking invite links from all the channels.✅")
                 elif option == 'false':
                      if channels == 'this':
                         await bot.say("Not blocking invite links from this channel.")
                      elif channels == 'all':
                         for i in range(len(server_id[ctx.message.server.id][0])):
                                  server_id[ctx.message.server.id][0].pop()
                         await bot.say("Not blocking invite links from any of the channels")
         elif ctx.message.server.id not in server_id:
             server_id[ctx.message.server.id] = [[],[]]
             server_id[ctx.message.server.id][1].append('blockInvites')
             if ctx.message.channel.id in server_id[ctx.message.server.id][0]:
                 if channels == 'this':
                      if option == 'true':
                         await bot.say("Block invites feature is already enabled for this channel.✅")
                      elif option == 'false':
                         server_id[ctx.message.server.id][0].remove(ctx.message.channel.id)
                         await bot.say("Invite links won't be blocked from this channel.")
                 elif channels == 'all':
                      if option == 'true':
                         for i in ctx.message.server.channels:
                                  server_id[ctx.message.server.id][0].append(i.id)
                         await bot.say("Blocking invite links from all the channels.✅")
                      elif option == 'false':
                         for i in range(len(server_id[ctx.message.server.id][0])):
                                  server_id[ctx.message.server.id][0].pop()
                         await bot.say("Invite links won't be blocked in any of the channels.")
             elif ctx.message.channel.id not in server_id[ctx.message.server.id][0]:
                 if option == 'true':
                      if channels == 'this':
                         server_id[ctx.message.server.id][0].append(ctx.message.channel.id)
                         await bot.say("Invite links will be blocked from this channel.✅")
                      elif channels == 'all':
                         for i in ctx.message.server.channels:
                                  server_id[ctx.message.server.id][0].append(i.id)
                         await bot.say("Blocking invite links from all the channels.✅")
                 elif option == 'false':
                      if channels == 'this':
                         await bot.say("Not blocking invite links from this channel.")
                      elif channels == 'all':
                         for i in range(len(server_id[ctx.message.server.id][0])):
                                  server_id[ctx.message.server.id][0].pop()
                         await bot.say("Not blocking invite links from any of the channels")
      else:
         await bot.say("❌You don't have the permission to use this command")
    
    @commands.command(pass_context=True, description="USE ONLY WHEN NECESSARY!")
    async def panic(self, ctx, option):
      '''Save the server from a raid by turning the permissions of every person in the server'''
      overwrite = discord.PermissionOverwrite()
      overwrite_for_lorris = discord.PermissionOverwrite()
    
      overwrite_for_lorris.send_messages = True
      overwrite_for_lorris.ban_members = True
      overwrite_for_lorris.kick_members = True
      overwrite_for_lorris.add_reactions = True
      overwrite_for_lorris.send_tts_messages = True
    
      if ctx.message.channel.permissions_for(ctx.message.author).administrator:
            
          if option == "on":
               
            overwrite.send_messages = False
            overwrite.ban_members = False
            overwrite.kick_members = False
            overwrite.add_reactions = False
            overwrite.send_tts_messages = False
            for channels in ctx.message.server.channels:
              for role in ctx.message.server.roles:
                if role.name == "@everyone":
                    try:
                      await bot.edit_channel_permissions(channels, role, overwrite)
                    except: pass
            lorris = discord.utils.get(ctx.message.server.members, name="Lorris")
            await bot.edit_channel_permissions(channels, lorris, overwrite_for_lorris)      
            await bot.send_message(ctx.message.channel, "The panic command is turned ON. No one in the server can send messages in **any** channel or kick / ban members. To disable the command use `L+panic off`")
               
    
          if option == "off":
                
            overwrite.send_messages = True
            overwrite.ban_members = True
            overwrite.kick_members = True
            overwrite.add_reactions = True
            overwrite.send_tts_messages = True
            for channels in ctx.message.server.channels:
              for role in ctx.message.server.roles:
                if role.name == "@everyone":
                    try:
                      await bot.edit_channel_permissions(channels, role, overwrite)
                    except: pass
            lorris = discord.utils.get(ctx.message.server.members, name="Lorris")
            await bot.edit_channel_permissions(channels, lorris, overwrite_for_lorris)  
            await bot.send_message(ctx.message.channel, "The panic command is turned OFF")   
      else:
        await bot.send_message(ctx.message.channel, "Sorry, you don't have the `administrator` permission. If this is really a case of a raid/spam contact the server admin **immediately**; If not, using this command may get you in trouble, my friend :')") 
   
class TicTacToe:
   
    @commands.command(pass_context = True)
    async def ttt(self, ctx):
      '''Start a new TicTacToe game.'''
        
      global font
      background = Image.open("images/images/tictactoe.jpg")
      font = ImageFont.truetype("fonts/fonts/comicsans.ttf", 130)
   
   
      if not ctx.message.channel.id in channels_with_gameON:
          
        await bot.say("A new TicTacToe game has been started. Say `L+join` to join")
          
        turn = 'x'
        global session_id 
             
        session_id = random.randint(0,100)
        while session_id in session_ids:
          session_id = random.randint(0,100)
        session_ids.append(session_id)
  
        channels_with_gameON[ctx.message.channel.id] = session_id
  
        sessions[channels_with_gameON[ctx.message.channel.id]] = []
        sessions[channels_with_gameON[ctx.message.channel.id]].append([])                               #FOR PLAYERS
        sessions[channels_with_gameON[ctx.message.channel.id]][0].append(ctx.message.author.id)         #adding the 1st player
     
        sessions[channels_with_gameON[ctx.message.channel.id]].append([[], []])                         #2 list coz 2 player's choices
        sessions[channels_with_gameON[ctx.message.channel.id]].append(background)                       #adding image object
        sessions[channels_with_gameON[ctx.message.channel.id]].append(turn)
        background.save("tempTTT.jpg")
     
   
      elif ctx.message.channel.id in channels_with_gameON:
        await bot.say("Sorry, there's an ongoing TicTacToe game in this channel. Try again later")
   
   
    @commands.command(pass_context = True)
    async def join(self, ctx):
      '''Join an ongoing TicTacToe game'''
      global channels_with_gameON
      if not len(sessions[channels_with_gameON[ctx.message.channel.id]][0]) >= 2:
        if not ctx.message.author.id in sessions[channels_with_gameON[ctx.message.channel.id]][0]:
          if not ctx.message.channel.id in channels_with_gameON:
            await bot.say("No game of TicTacToe is currently on in this channel. Use `L+ttt` to make one.")
   
          elif ctx.message.channel.id in channels_with_gameON:
            sessions[channels_with_gameON[ctx.message.channel.id]][0].append(ctx.message.author.id)  #adding the 2nd player
   
            await bot.say("{0} joined the TicTacToe game made by {1}".format(ctx.message.author.name, discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0]).name)) 
            await bot.say("TicTacToe game started. Use `L+mark <box number>` to make a choice") 
   
   
        elif ctx.message.author.id in sessions[channels_with_gameON[ctx.message.channel.id]][0]:
          await bot.say("Sorry, you can't play with yourself :\" )")
      else: 
        await bot.say(f"Sorry, the ongoing game created by {discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0]).name} is already full")
        
  
    @commands.command(pass_context = True)
    async def mark(self, ctx, choice: int):
      global channels_with_gameON
      async def dispose():
        global channels_with_gameON
        async for i in bot.logs_from(ctx.message.channel, limit=15):
                  if "Use `L+mark" in i.content and i.author.id == "389493821043376130" or i.content.startswith("L+mark"): 
                    await bot.delete_message(i)
        sessions[channels_with_gameON[ctx.message.channel.id]][2].save(f"{channels_with_gameON[ctx.message.channel.id]}.jpg")
        await bot.send_file(ctx.message.channel, f"{channels_with_gameON[ctx.message.channel.id]}.jpg", filename = "TicTacToe.jpg", content=None)
        await bot.say(f"Yay! {winner.mention} won this game! {loser.mention}, better luck next time :)")
  
        session_ids.remove(channels_with_gameON[ctx.message.channel.id])
        channels_with_gameON = {key : value for key, value in channels_with_gameON.items() if key != ctx.message.channel.id}
        
      
          
      if not ctx.message.author.id in sessions[channels_with_gameON[ctx.message.channel.id]][0]:
        await bot.say("You're not in any ongoing game currently")
    
      elif ctx.message.author.id in sessions[channels_with_gameON[ctx.message.channel.id]][0]:
        if type(choice) == int:
          if not choice in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and not choice in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
               
            draw = ImageDraw.Draw(sessions[channels_with_gameON[ctx.message.channel.id]][2])
   
            if sessions[channels_with_gameON[ctx.message.channel.id]][3] == 'x':
              if ctx.message.author.id == sessions[channels_with_gameON[ctx.message.channel.id]][0][0]:
                draw.text(coordinates[choice], "X", (0,0,0), font=font)
                sessions[channels_with_gameON[ctx.message.channel.id]][1][0].append(choice)
                sessions[channels_with_gameON[ctx.message.channel.id]][3] = 'o'
                sessions[channels_with_gameON[ctx.message.channel.id]][2].save(f"{channels_with_gameON[ctx.message.channel.id]}.jpg")
                try: 
                  await bot.delete_message(ctx.message)
                  await asyncio.sleep(0.1)
                except: pass
  
                async for i in bot.logs_from(ctx.message.channel, limit=15):
                  if "Use `L+mark" in i.content and i.author.id == "389493821043376130" or i.content.startswith("L+mark"): 
                    await bot.delete_message(i)
                file_msg = await bot.send_file(ctx.message.channel, f"{channels_with_gameON[ctx.message.channel.id]}.jpg", filename = "TicTacToe.jpg", content="Use `L+mark <box number>` to make a choice")  
     
                await asyncio.sleep(0.2)
                os.remove(f"{channels_with_gameON[ctx.message.channel.id]}.jpg")
                      
     
              elif ctx.message.author.id == sessions[channels_with_gameON[ctx.message.channel.id]][0][1]:
                await bot.say(f"Sorry, {ctx.message.author.mention}, it is {discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0]).mention}'s turn")
     
            elif sessions[channels_with_gameON[ctx.message.channel.id]][3] == 'o':
              if ctx.message.author.id == sessions[channels_with_gameON[ctx.message.channel.id]][0][1]:
                draw.text(coordinates[choice], "O", (0,0,0), font=font)
                sessions[channels_with_gameON[ctx.message.channel.id]][1][1].append(choice)
                sessions[channels_with_gameON[ctx.message.channel.id]][3] = 'x'
                sessions[channels_with_gameON[ctx.message.channel.id]][2].save(f"{channels_with_gameON[ctx.message.channel.id]}.jpg")
                try:
                  await bot.delete_message(ctx.message)
                  await asyncio.sleep(0.1)
                except:pass
                async for i in bot.logs_from(ctx.message.channel, limit=15):
                  if "Use `L+mark" in i.content and i.author.id == "389493821043376130" or i.content.startswith("L+mark"): 
                    await bot.delete_message(i)
                    
                file_msg = await bot.send_file(ctx.message.channel, f"{channels_with_gameON[ctx.message.channel.id]}.jpg", filename = "TicTacToe.jpg", content="Use `L+mark <box number>` to make a choice")  
     
                     
                await asyncio.sleep(0.2)
                os.remove(f"{channels_with_gameON[ctx.message.channel.id]}.jpg")
     
              elif ctx.message.author.id == sessions[channels_with_gameON[ctx.message.channel.id]][0][0]:
                await bot.say(f"Sorry, {ctx.message.author.mention}, it is {discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1]).mention}'s turn")
     
     
            #player 1
            #123
            if 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 2 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(10,90),(500,90)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
     
            #456
            elif 4 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 6 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(10,255),(500,255)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
     
            #789  
            elif 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 8 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(10,420),(500,420)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
   
            #147  
            elif 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 4 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(90,10),(90,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
     
            #258  
            elif 2 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 8 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(255,10),(255,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
     
            #369
            elif 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 6 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(420,10),(420,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
   
            #159
            elif 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(10,10),(500,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
   
            #357
            elif 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] and 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][0]:
              draw.line([(500,10),(10,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              await dispose()
   
            #player 2
            #123
            if 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 2 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(10,90),(500,90)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #456
            elif 4 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 6 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(10,255),(500,255)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #789  
            elif 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 8 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(10,420),(500,420)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #147  
            elif 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 4 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(90,10),(90,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #258  
            elif 2 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 8 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(255,10),(255,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #369
            elif 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 6 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(420,10),(420,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #159
            elif 1 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 9 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(10,10),(500,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            #357
            elif 3 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 5 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1] and 7 in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
              draw.line([(500,10),(10,500)], width=10, fill=(255,0,0))
              winner = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][1])
              loser = discord.utils.get(ctx.message.server.members, id = sessions[channels_with_gameON[ctx.message.channel.id]][0][0])
              await dispose()
   
            elif len(sessions[channels_with_gameON[ctx.message.channel.id]][1][0])+len(sessions[channels_with_gameON[ctx.message.channel.id]][1][1]) == 9:
              await bot.say("It's a draw! No one wins and no one loses! ")
              sessions[channels_with_gameON[ctx.message.channel.id]] = []
              channels_with_gameON = {key : value for key, value in channels_with_gameON.items() if key != ctx.message.channel.id}
   
   
          elif choice in sessions[channels_with_gameON[ctx.message.channel.id]][1][0] or choice in sessions[channels_with_gameON[ctx.message.channel.id]][1][1]:
            await bot.say("This choice has already been made. Try a different one")
   
   
   
        else:
          await bot.say("Wrong choice type. Make an integer choice between 1-9")
  
    @commands.command(pass_context=True)
    async def leave(self, ctx):
      global channels_with_gameON
      if not ctx.message.channel.id in channels_with_gameON:
  
        await bot.say("You're not in any ongoing game in this channel.")
  
      elif ctx.message.channel.id in channels_with_gameON:
        if ctx.message.author.id in sessions[channels_with_gameON[ctx.message.channel.id]][0]:
          session_ids.remove(channels_with_gameON[ctx.message.channel.id])
          channels_with_gameON = {key : value for key, value in channels_with_gameON.items() if key != ctx.message.channel.id}
          await bot.say("Successfully left the game.")
  
        else:
          await bot.say("You're not in any ongoing game in this channel.")

class Help: 
  @commands.command (pass_context=True) 
  async def help(self, ctx): 
   
    msg = await bot.say("*Please wait for the help message to load*")
    page_index = 1
    embed_list = []
    for i in bot.cogs:
      
      em = discord.Embed(title = i, description = "Help on " + i, colour = 0x00FFFF)
      if not i == "REPL" and not i == "Help":
        for command_name in dir(bot.cogs[i])[26:]:
          command = bot.get_command(command_name)
          em.add_field(name = command_name, value = command.help, inline=False)
        embed_list.append(em)
      em.set_footer(text="Page {0} of {1}".format(page_index-1, len(bot.cogs) - 2))
      page_index += 1
    info_embed = discord.Embed(title = "Help Info", 
                  description = "\u23EA:  Go to the first page\n\u25C0:  Go to the previous page\n\u23F9:  Stop the help command\n\u25B6:  Go to the next page\n\u23E9:  Go to the last page\n\U0001f522:  Asks for a page number\n\u2139:  Shows this info", colour = 0x2279DE)

    await bot.edit_message(msg, embed = embed_list[0])
    embed_list.append(info_embed)
    pa = Paginator(bot, msg, ctx.message.author, 0)
    await pa.paginate(embed_list)
   
  
       
       
bot.remove_command('help')
bot.add_cog(Help())
bot.add_cog(TicTacToe())
bot.add_cog(Admins())
bot.add_cog(Useful())
bot.add_cog(Fun())
bot.add_cog(Security())
bot.add_cog(math())
bot.run(str(os.environ("TOKEN")))
