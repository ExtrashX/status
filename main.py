# Credit By Bimzzx (Lynzzx / Bl4ckSh4d0w).
# Tolong Jangan Hapus Creditnya | Please Don't Remove Credit
## ================================ [ IMPORT MODULE ] ============================== ##
import discord, os, asyncio, time, random, xontol
from discord.ext import commands, tasks
## ================================ [ KONFIGURASI AWAL ] ============================== ##
client = commands.Bot(command_prefix='-', self_bot=True)
client.remove_command(name='help')
## ================================ [ STARTED ] ============================== ##
async def ubah_status():
    statuses = ["Bimm", "Lynzzx", "BlackShadow", "Bimzzx", "Lynzzx", "BlackShadow"]
    while not client.is_closed():
    	status = random.choice(statuses)
    	await client.change_presence(activity = discord.Streaming(name=status, url="https://www.twitch.tv/bimzz19"))
    	await asyncio.sleep(3)
    	client.loop.create_task(ubah_status())

@client.event
async def on_ready():
    print(f"------------------ [ SELFBOT STATUS ] -----------------")
    time.sleep(0.2)
    print(f"-------------------------------------------------------")
    print(f"[+] Connected to {client.user.name}#{client.user.discriminator} [{client.user.id}]")
    print(f"[+] Discord Py Version :", discord.__version__)
    print(f"-------------------------------------------------------")
    for guild in client.guilds:
    	print(f"[+] Connected On ({len(client.guilds)}) Server : ")
    	print(guild.name, " [", guild.id, "]")
    	print(f"-------------------------------------------------------")
    await client.wait_until_ready()
    ubah_status()



xontol.xontol()
client.run(os.getenv("TOKEN"), bot=False)
