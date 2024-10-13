# PicWatcher

PicWatcher is a simple Matrix bot that checks if users in a room have a profile picture (avatar). If a user does not have a profile picture, the bot sends a polite reminder to update their avatar.

## Features:
- Checks profile pictures of all users in a specified Matrix room.
- Sends a message to users without profile pictures asking them to update.
- Lightweight and easy to use.
- Can be customized for other tasks and checks.

## Installation:

### Prerequisites:
- Python 3.8 or higher.
- A Matrix account.
- Access to a Matrix room where the bot will operate.

1. Clone the repository:

git clone https://github.com/derzalus/picwatcher.git
cd picwatcher


2. Install the required dependencies:

pip install matrix-nio

3. Configure the bot:

In the picwatcher.py file, replace the following placeholders with your actual information:

YOUR_USERNAME_HERE: Your Matrix username (e.g., @botusername:matrix.org).
YOUR_PASSWORD_HERE: Your Matrix password.
YOUR_ROOM_ID: The room ID where the bot will operate (e.g., !abcdefg:matrix.org)

4. Run the bot:

python picwatcher.py

The bot will log in, join the specified room, and check if users have profile pictures.

Usage:
Once the bot is running, it will:

Log into the Matrix server.
Join the specified room.
Check the profile pictures of all room members.
Send a reminder message to users without profile pictures.

Example Message:
If a user does not have a profile picture, the bot will send a message like this:

@username, please update your profile picture. (Sent by PicWatcher bot)

Customization:
You can change the reminder message format or add additional checks (e.g., display name checks) by modifying the check_all_users_in_room function in the code.

License:
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing:
Feel free to fork this project and submit pull requests for any improvements or features you’d like to add.
