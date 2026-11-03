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


# ──────────────── /faq ────────────────
@bot.tree.command(name="faq", description="❓ Frequently asked questions")
async def faq_command(interaction: discord.Interaction):
    embed1 = discord.Embed(title="📚 FAQ", color=ACCENT)
    embed2 = discord.Embed(description="""🤔 **What is Roblox MultiHub?**  
A free tool to manage Roblox accounts, run multiple sessions, and organize your windows.""", color=ACCENT)
    embed3 = discord.Embed(description="""👥 **Can I use multiple accounts at once?**  
Yes, and launch them into the same server when space is available.""", color=ACCENT)
    embed4 = discord.Embed(description="""➕ **How do I add accounts?**  
Sign in through your browser or import cookies individually or in bulk.""", color=ACCENT)
    embed5 = discord.Embed(description="""💾 **Can I save my setup?**  
Yes. Save accounts, games, layouts, and settings as presets.""", color=ACCENT)
    embed6 = discord.Embed(description="""🔒 **Where is my account data stored?**  
Encrypted on your PC. It is never uploaded to external services.""", color=ACCENT)
    embed7 = discord.Embed(description="""🆓 **Is it free and open source?**  
Yes. No ads, subscriptions, or paywalls. The full source code is included.""", color=ACCENT)
    embed8 = discord.Embed(description="""📂 **Which operating systems are supported?**  
Windows.""", color=ACCENT)

    await interaction.response.send_message(embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8])


# ──────────────── /download ────────────────
@bot.tree.command(name="download", description="📥 Get the download link")
async def download_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📥 Download",
        description="To Download Roblox MultiHub, Click On The Button Below!",
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


# ──────────────── /features ────────────────
@bot.tree.command(name="features", description="✨ See what it can do")
async def features_command(interaction: discord.Interaction):
    embed1 = discord.Embed(title="Roblox MultiHub — Full Feature List (v1.1.3)", color=ACCENT)
    embed2 = discord.Embed(description="""👥 **ACCOUNTS**
- Log in with a browser, or add several at once with username:password
- Paste / import / drag-and-drop cookies (bulk)
- Groups, aliases, notes, saved passwords, profile pictures
- A game per account, search, sorting, your own order
- Edit many accounts at once, and view details of many at once (age, Robux, Premium)
- Live status: in game / online / offline (colored dot)
- List view and Cards view
- Startup check: tells you which accounts Roblox signed out
- Account-locked detection (HTTP 403) — see which account got blocked""", color=ACCENT)
    embed3 = discord.Embed(description="""🚀 **LAUNCHING**
- Join a game, a specific server (Job ID), a private server, or follow a player
- Search a game by name, pick a server by players/ping/FPS, or random
- Launches like Roblox Account Manager — no "human verification" on join
- Delay between accounts, max-windows limit, auto-close previous window
- Server browser: get several accounts into the SAME server
- Launch selected / Launch all / Stop all""", color=ACCENT)
    embed4 = discord.Embed(description="""🪟 **MULTI-INSTANCE & WINDOW LAYOUT**
- Run several Roblox windows at once
- Automatic grid, custom rows/columns, or fixed size
- Scale, gaps, margins, borderless, always-on-top, multi-monitor
- Pin a window to an exact spot, rename windows to account names
- Live preview, auto-capture, global hotkeys""", color=ACCENT)
    embed5 = discord.Embed(description="""⚡ **PERFORMANCE**
- FPS cap + graphics presets (quality, textures, anti-aliasing, grass, sky, API)
- CPU priority + minimize all
- RAM cleaner (Mem Reduct-style): manual or automatic over a limit (with confirmation)
- Max alts: throttles the windows you're not playing (Idle priority + Windows efficiency mode + memory trim); the one you play stays full speed""", color=ACCENT)
    embed6 = discord.Embed(description="""📊 **MONITOR**
- Live card per account: CPU and RAM sparklines, uptime
- Preview thumbnail per client
- Focus / Minimize / Close per window""", color=ACCENT)
    embed7 = discord.Embed(description="""💾 **PRESETS***
- Save your whole setup (accounts, games, window layout, settings)
- One click restores everything, or run it automatically at startup
- A preset uses its own settings WITHOUT overwriting your global settings""", color=ACCENT)
    embed8 = discord.Embed(description="""🤖 **AUTOMATION**
- Anti-AFK (mouse nudge / jump / zoom) — stops idle kicks without interrupting auto-hatch
- Auto-relaunch (watcher) + crash breaker (stops endlessly relaunching a crashing account)
- Macro recorder (TinyTask-style) in its own window, small/large size""", color=ACCENT)
    embed9 = discord.Embed(description="""🔔 **DISCORD WEBHOOK ALERTS**
- Notifications on crash/kick, relaunch, batch finished, account locked
- "Send a test message", fully opt-in""", color=ACCENT)
    embed10 = discord.Embed(description="""🔒 **SAFETY & STORAGE**
- Accounts encrypted (Windows DPAPI or your own password, AES-256)
- Everything stays local on your PC — nothing is uploaded
- Automatic backups (last 10 kept)""", color=ACCENT)
    embed11 = discord.Embed(description="""🎨 **OTHER**
- Dark / light theme, icons on the navigation
- Language support (English + Dutch, extendable)
- Update check at startup (notify-only, never downloads by itself)
- Start with Windows, one-click installer
- Discord icon + donation link, foldable Help page""", color=ACCENT)

    # Discord allows max 10 embeds per message, so the 11th goes in a follow-up message
    await interaction.response.send_message(embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10])
    await interaction.followup.send(embeds=[embed11])


# ──────────────── /tutorial ────────────────
@bot.tree.command(name="tutorial", description="📚 Learn how to get started")
async def tutorial_command(interaction: discord.Interaction):
    embed1 = discord.Embed(description="""📚 **Tutorial**
    SOON""", color=ACCENT)

    await interaction.response.send_message(embeds=[embed1])


# ──────────────── /dlpanel ────────────────
@bot.tree.command(name="dlpanel", description="📥 Download panel")
async def dlpanel_command(interaction: discord.Interaction):
    embed1 = discord.Embed(description="""🚀 **Roblox MultiHub** — launch all your Roblox alts at once, free & open source.

🌐 Website: https://roblox-multihub.vosje-brecht.workers.dev/
⬇️ Download: https://github.com/Roblox-MultiHub/Roblox-MultiHub/raw/main/download/RobloxMultiHub.zip

Unzip → run Install RobloxMultiHub.bat → add accounts → Launch. Use your own accounts!""", color=SUCCESS)

    await interaction.response.send_message(embeds=[embed1])


if __name__ == "__main__":
    if not TOKEN or not GUILD_ID:
        raise SystemExit("❌ Missing DISCORD_TOKEN or GUILD_ID. Check your .env file.")
    bot.run(TOKEN)
