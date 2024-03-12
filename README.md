# Discord Font Bot

The Discord Font Bot enhances server engagement by dynamically changing member nicknames to include unique fonts. This Python bot leverages the discord.py library and includes features such as setting a default font for new members, allowing server admins to add or remove fonts, and providing the ability to apply the default font to all server members' nicknames.

## Features

- **Dynamic Font Application:** Automatically apply a selected font to new server members' nicknames.
- **Font Management:** Add and remove fonts directly through Discord commands.
- **Default Font Application:** Apply the selected default font to all server members' nicknames with a single command.
- **Font List Viewing:** List all available fonts for easy management and selection.

## Prerequisites

To run the Discord Font Bot, ensure you have the following:

- Python 3.6 or higher
- discord.py library
- A Discord Bot Token

## Installation

1. **Clone the Repository**

```bash
git clone https://your-repository-url-here
cd discord-font-bot
```

2. **Install Dependencies**

```bash
pip install discord.py
```

3. **Configure Your Bot**

Edit the bot token in the script:

```python
bot.run('YOUR_BOT_TOKEN')
```

Replace `'YOUR_BOT_TOKEN'` with your actual bot token from the Discord Developer Portal.

4. **Set up the Bot on Discord**

Follow the instructions to add your bot to a server, ensuring you grant it the "Manage Nicknames" permission.

## Usage

Run the bot:

```bash
python font_bot.py
```

### Bot Commands

- `!listfonts` - Lists all available fonts.
- `!setfont <font_number>` - Sets the default font for new members. (Admin only)
- `!addfont "<font_name>"` - Adds a new font to the list. Include the font in quotes. (Admin only)
- `!removefont <font_number>` - Removes a font from the list based on its number. (Admin only)
- `!applyfont` - Applies the default font to all server members' nicknames. Use with caution. (Admin only)

## Contributing

Contributions to the Discord Font Bot are welcome! Feel free to fork the repository and submit pull requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- This project relies on the fantastic [discord.py](https://github.com/Rapptz/discord.py) library.
- Thank you to the Discord community for inspiring this project.
