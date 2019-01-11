import discord
client = discord.Client()

@client.event
async def on_message(message):
    #we do not want the bot to respond to it self
    if message.author == client.user:
        return

    if message.content.startswith("<patch"):
        msg = "Dear Explorers: \
 To offer you a better gaming experience, our servers will be down for maintenance for some time. \
                                    Check the information below to find out when the server will be up again in your area: \
EST (New York): January 10, 2019, 00:50 -  AM - 3:00 AM \
UTC -2  (Saint Paul): January 10, 2019, 3:50 AM - 6:00 AM \
UTC+1 (London): January 10, 2019, \
5:50 AM - 8:00 AM \
UTC+2 (Berlin, Paris): January 10, 2019, 6:50 AM - 9:00 AM \
UTC+9 (Tokyo, Seoul): January 10, 2019, 14:50 - 17:00 \Completion time may be extended if maintenance cannot be finished within the expected time. Apologies in advance for any inconvenience in such an event, and thank you for your support and understanding.".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("<help"):
        msg = "Find below commands, \
!patch < this command can only be used by an Discord Manager!"
        await client.send_message(message.channel, msg)
    if message.content.startswith("<C.D."):
        msg = "Creative Destruction is a sandbox survival mobile game that infusing sandbox crafting and Battle Royale with a light, cartoon art style. \
Players will parachute in a large-scale battlefield of 16,000,000 square meters, with 13 interesting spots waiting to be explored.\
In this virtual world, all elements in this world can be built or dismantled. Explorers can use an secret weapon named Destructor to dismantle anything in sight and build bastions via an innovative workshop system. \
There is a variety of weaponry at your fingertips. Collect unique weapons, race against snowstorms, and battle to the death! \
Build the best, break the rest! Come join a smash-and-shoot deathmatch in wonderland!"
        await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print('Bot is ready')



client.run("NDQ5MTMwNTYxNzk0MDgwNzg5.DxZkkg.qOotuixqzOHky4j9nMuJmm_MHmU")

