import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':plan1'):
        await message.channel.send('1.Matematyka   2.J.Polski  3.J.Polski  4.W-F  5.Geografia  6.Technika')
    if message.content.startswith(':plan2'):
        await message.channel.send('1.Matematyka   2.J.Polski  3.Religia  4.Informatyka  5.Angielski  6.Plastyka 7.WDŻ')
    if message.content.startswith(':plan3'):
        await message.channel.send('1.Polski Dodatkowy   2.J.Polski  3.Historia  4.W-F  5.Muzyka  6.Matematyka') 
    if message.content.startswith(':plan4'):
        await message.channel.send('1.Angielski/-   2.Matematyka  3.Lekcja Wychowawcza  4.Religia 5.W-F  6.-/Angielski')
    if message.content.startswith(':plan5'):
        await message.channel.send('1.Angielski/-   2.J.Polski  3.Bilogia  4.W-F 5.Historia')                  

client.run('Nzg3OTU0MjQ4MzM1NjIyMTQ0.X9cdlA.yDNTh5LUdQmnxfuFT9WutxKtvmc')
