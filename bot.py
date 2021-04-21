import discord
import datetime


weekday = datetime.datetime.today().weekday()
hour = datetime.datetime.today().hour 
# hour += 3


constanta = 8

cod = ['Mate', 'Sport', 'Istorie', 'Engleza', 'Muzica/Desen', 'Bio',
       'Geogra', 'Romana', 'Chimie', 'Fizica', 'informatica', 'Franceza/Germana'
       'Psiho', 'Ed antreprenoriala', 'Religie'
]

link = [
    'https://meet.google.com/lookup/h25azkpwbq?authuser=1&hs=179',
    'https://meet.google.com/lookup/bko2g7z7hl?authuser=1&hs=179',
    'https://meet.google.com/lookup/f5jf3j4bah?authuser=1&hs=179',
    'https://zoom.us/j/95223240033?pwd=VCs3UGZDMmR0SFcxZzU2KzBkWUNKdz09',
    'Muzica : https://meet.google.com/lookup/asro2v2rb5?authuser=1&hs=179 \n        Arte : https://meet.google.com/lookup/hingwga7je?authuser=1&hs=179',
    'https://meet.google.com/lookup/h7ulknirey?authuser=1&hs=179',
    'https://meet.google.com/lookup/huiosib6ba?authuser=1&hs=179',
    'https://zoom.us/j/5858050008?pwd=WVNPVVh5b0RPaTl1SWNkczNQd3V5dz09',
    'https://meet.google.com/lookup/deqmst3blv?authuser=1&hs=179',
    'https://meet.google.com/lookup/dj3ph5som2?authuser=1&hs=179',
    'https://zoom.us/j/7640359867?pwd=ZDdldStaKzA1Z1drVFdoVE1qRVlndz09',
    'Franceza : https://meet.google.com/lookup/e6agip4x75?authuser=1&hs=179 \n        Germana : https://meet.google.com/lookup/goaty6ltyd?authuser=1&hs=179',
    'https://meet.google.com/lookup/acwhr2ezxm?authuser=1&hs=179',
    'https://meet.google.com/lookup/gi5v364hbu?authuser=1&hs=179',
    'https://meet.google.com/lookup/h7kgcgv5ta?authuser=1&hs=179'
]

orar = [
    [0, 0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 0],
    [10, 10, 10, 11, 0, 5],
    [12, 7, 7, 3, 8, 13],
    [10, 10, 9, 9, 11, 14]
]


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!hatz'):
    ('Hatzzz johnule')

  if 'boss' in message.content or 'master' in message.content:
    await message.channel.send('Seful meu este john')

  if message.content.startswith('!calc'):
    str = message.content[5: len(message.content)]
    answ = eval(str)
    await message.channel.send(answ)

  if message.content == '!comands' or message.content == '!help' :
    str = '```fix\nEverything is yellow in fix\n --No matter the line!```'
    await message.channel.send(str)


  if message.content == '!orar':
    await message.channel.send(file=discord.File('orar.jpg'))

  if message.content == '!ora' or message.content == '!ora curenta':
    if weekday >= 0 and weekday < 6:
        if hour > 7 and hour < 14:
            mesg = 'Ora : ' + (cod[orar[weekday - 1][hour - constanta]]) + '\n'
            mesg1 =  'Link : ' + (link[orar[weekday - 1][hour - constanta]])
            mesg += mesg1
            await message.channel.send(mesg)
        else:
            await message.channel.send('Nu aveti ora momentan')
    else:
      await message.channel.send('WEEKEND!!!')

  if message.content == '!ora vit' or message.content == '!ora vitoare':
    if weekday >= 0 and weekday < 6:
        if hour > 6 and hour < 13:
            mesg = 'Ora : ' + (cod[orar[weekday - 1][hour - constanta + 1]]) + '\n'
            mesg1 =  'Link : ' + (link[orar[weekday - 1][hour - constanta + 1]])
            mesg += mesg1
            await message.channel.send(mesg)
        else:
            await message.channel.send('Nu mai aveti ore')
    else:
      await message.channel.send('WEEKEND!!!')



client.run('ODM0MzgzMDI5MjE2NjA4Mjg4.YIAFwA._mofjESAQOZyuVdGWMyJNlauDX8')
