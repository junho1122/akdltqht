import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    print("-----------------------------------")
    game = discord.Game("제작자 : 유준호#2879 [24시간구동]")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("아잇봇"):
        await message.channel.send("아잇?")

    if message.content.startswith("뒤질래?"):
            await message.channel.send("아잇 ㅠㅠ")

    if message.content.startswith("라면"):
        await message.channel.send("아잇~~!!!!어ㅢ;풀으르릉어응!~으")

    if message.content.startswith("소고기"):
        await message.channel.send("으아잇~음~푸칙으~")

    if message.content.startswith("|771410|"):
        author = message.guild.get_member(int(message.content[9:27]))
        role = discord.utils.get(message.guild.roles, name="이스터에그")
        await author.add_roles(role)

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!보내기"):
        channel = message.content[5:23]
        msg = message.content[24:]
        await client.get_channel(int(channel)).send(msg)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
