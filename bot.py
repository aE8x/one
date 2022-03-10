import discord
client = discord.Client()
channel1id = 785365953675919421
channel2id = 951461255967821917

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = client.get_channel(channel2id)
        await channeltosend.send(message.content, embed=message.embeds[0])

client.run("OTUxNDYyOTU1OTUyNzk5NzU1.Yin07g.ucoXx2YUrGitcXi9NVuZQmvHZ9I")