import discord, os

cid = os.getenv("CID")
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
  print("Hi")

@bot.event
async def on_member_join(member):
  guild = member.guild
  channel = bot.get_channel(int(cid))
  if channel is not None:
    embed = discord.Embed(title=f"ยินดีต้อนรับสู่แก๊งค์ **{guild.name}**\nขอให้อยู่ด้วยกันนานๆนะครับ", description=f"", color=discord.Color.from_rgb(177, 10, 255))
    embed.set_author(name = f"{member.name}#{member.discriminator}", icon_url = member.avatar_url)
    embed.set_image(url="https://share.creavite.co/uNRJZUSr40ECnMvd.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/893177764461547542/893339738512166932/standard.gif")
    embed.set_footer(text="made script bye Xenozsama#8590")
    try:
      await channel.send(embed=embed)
      print(f"<@!{member.id}> has joined the server")
    except:
      print("i can't do that")
  else:
      print("Failed to fetch channel")
      

token = os.environ.get("TOKEN")
bot.run(token)
