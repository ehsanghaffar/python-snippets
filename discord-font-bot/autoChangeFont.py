
import discord
from discord.ext import commands
import json

# font list
FONT_FILE = 'fonts.json'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

def load_fonts():
    """Load fonts from a JSON file."""
    try:
        with open(FONT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"current_font": None, "fonts_list": []}

def save_fonts(data):
    """Save fonts to a JSON file."""
    with open(FONT_FILE, 'w') as file:
        json.dump(data, file, indent=4)

fonts_data = load_fonts()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    """Automatically update nickname of new members with the default font, if set."""
    fonts_data = load_fonts()
    current_font = fonts_data.get("current_font")
    if current_font:
        try:
            new_name = f'{fonts_data["fonts_list"][current_font]} {member.name}'
            await member.edit(nick=new_name)
            print(f"Changed nickname for {member} to use font {current_font}")
        except:
            print(f"Couldn't change nickname for {member}")

@bot.command(name='setfont', help='Sets the font for new members')
@commands.has_permissions(administrator=True)
async def set_font(ctx, font_number: int):
    fonts_data = load_fonts()
    if 0 <= font_number < len(fonts_data["fonts_list"]):
        fonts_data["current_font"] = font_number
        save_fonts(fonts_data)
        await ctx.send(f"Font set to {fonts_data['fonts_list'][font_number]}")
    else:
        await ctx.send("Invalid font number.")

@bot.command(name='listfonts', help='Lists available fonts')
async def list_fonts(ctx):
    fonts_data = load_fonts()
    font_list = "\n".join([f"{i}: {font}" for i, font in enumerate(fonts_data["fonts_list"])])
    await ctx.send(f"Available fonts:\n{font_list}")

@bot.command(name='addfont', help='Adds a new font to the list (Admin only)')
@commands.has_permissions(administrator=True)
async def add_font(ctx, *, font: str):
    fonts_data = load_fonts()
    fonts_data["fonts_list"].append(font)
    save_fonts(fonts_data)
    await ctx.send(f"Added new font: {font}")

@bot.command(name='removefont', help='Removes a font from the list (Admin only)')
@commands.has_permissions(administrator=True)
async def remove_font(ctx, font_number: int):
    fonts_data = load_fonts()
    if 0 <= font_number < len(fonts_data["fonts_list"]):
        removed_font = fonts_data["fonts_list"].pop(font_number)
        save_fonts(fonts_data)
        await ctx.send(f"Removed font: {removed_font}")
    else:
        await ctx.send("Invalid font number.")

@bot.command(name='applyfont', help='Apply the default font to all server members (Admin only)')
@commands.has_permissions(administrator=True)
async def apply_font(ctx):
    fonts_data = load_fonts()
    current_font = fonts_data.get("current_font")
    if current_font is None:
        await ctx.send("No default font set.")
        return

    font = fonts_data["fonts_list"][current_font]
    failed = []

    for member in ctx.guild.members:
        try:
            await member.edit(nick=f'{font} {member.name}')
        except Exception as e:
            failed.append(member.name)
            print(f"Failed to change nickname for {member.name}: {e}")

    if failed:
        await ctx.send(f"Updated all possible members. Failed to update: {', '.join(failed)}")
    else:
        await ctx.send("Updated all members with the default font.")


bot.run('BOT_TOKEN')