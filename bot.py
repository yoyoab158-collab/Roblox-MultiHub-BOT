import os
import discord
from discord import app_commands
from dotenv import load_dotenv
 
# ──────────────── Config ────────────────
load_dotenv()  # reads the .env file next to this script
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
ACCENT = discord.Color.from_rgb(88, 101, 242)  # blurple
SUCCESS = discord.Color.from_rgb(87, 242, 135)  # green
 
 
class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
 
    async def setup_hook(self):
        # Sync commands to your server only, so they show up instantly
        guild = discord.Object(id=int(GUILD_ID))
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
 
 
bot = Bot()
 
 
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/download"))
 
# ──────────────── /download ────────────────
@bot.tree.command(name="download", description="📥 Get the download link")
async def download_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📥 Download",
        description="To Download Roblox MultiHub, Click On The Button Below!🔻",
        color=SUCCESS,
    )
    embed.add_field(name="⚡ Fast", value="Direct link", inline=True)
    embed.add_field(name="🔒 Safe", value="Verified source", inline=True)
    embed.add_field(name="🆓 Free", value="No cost", inline=True)
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.set_footer(text=f"Requested by {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    embed.timestamp = discord.utils.utcnow()
 
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", emoji="📥", style=discord.ButtonStyle.link, url="https://github.com/Roblox-MultiHub/Roblox-MultiHub/releases"))
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
 
 
if __name__ == "__main__":
    if not TOKEN or not GUILD_ID:
        raise SystemExit("❌ Missing DISCORD_TOKEN or GUILD_ID. Check your .env file.")
    bot.run(TOKEN)
 
