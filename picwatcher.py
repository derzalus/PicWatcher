import asyncio
import sys
from nio import (
    AsyncClient,
    AsyncClientConfig,
    LoginResponse,
    JoinedMembersResponse,
    ProfileGetResponse
)

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Replace with your server URL, user ID, and password for login
homeserver = "https://matrix.org"
username = "YOUR_USERNAME"  # Replace this with your actual Matrix User Name
password = "YOUR_PASSWORD"  # Replace this with your actual Matrix password
device_id = "PICTUREBOT"  # Unique device ID for the bot session

# Replace with your target room ID
room_id = "YOUR_ROOM_ID"

# Define the client globally so it can be used in callbacks
client = None

async def check_profile_picture(user_id):
    """Check if the user has a profile picture (avatar)."""
    response = await client.get_profile(user_id)  # Updated with get_profile method
    
    if isinstance(response, ProfileGetResponse) and response.avatar_url:
        print(f"{user_id} has a profile picture: {response.avatar_url}")
        return True
    else:
        print(f"{user_id} does NOT have a profile picture.")
        return False

async def check_all_users_in_room():
    """Check the profile picture of all users in the specified room."""
    response = await client.joined_members(room_id)

    if isinstance(response, JoinedMembersResponse):
        print("Successfully retrieved members from the room.")
        for member in response.members:
            user_id = member.user_id
            if user_id != username:
                print(f"Checking profile picture for {user_id}...")
                if member.avatar_url is None:
                    message_content = f"{user_id}, please update your profile picture."
                    formatted_message_content = f'<a href="https://matrix.to/#/{user_id}">{user_id}</a>, please update your profile picture.'

                    await client.room_send(
                        room_id,
                        message_type="m.room.message",
                        content={
                            "msgtype": "m.text",
                            "body": message_content,
                            "format": "org.matrix.custom.html",
                            "formatted_body": formatted_message_content
                        }
                    )
                    print(f"Sent profile update message to {user_id}")
                else:
                    print(f"{user_id} already has a profile picture: {member.avatar_url}")
    else:
        print("Failed to retrieve room members.")

async def main():
    global client
    # Initialize the Matrix client without encryption enabled
    config = AsyncClientConfig(store_sync_tokens=True)  # No encryption needed
    client = AsyncClient(
        homeserver,
        username,
        device_id=device_id,  # Set the unique device ID for the bot session
        config=config  # Configuration for the client
    )

    print("Logging in...")
    login_response = await client.login(password)

    if isinstance(login_response, LoginResponse):
        print(f"Logged in as {username} on device {login_response.device_id}")
    else:
        print(f"Failed to log in: {login_response}")
        return

    print(f"Joining room {room_id}...")
    try:
        await client.join(room_id)
    except Exception as join_error:
        print(f"Failed to join the room: {join_error}")
        return

    print("Checking all users in the room...")
    await check_all_users_in_room()

    print("Closing connection...")
    await client.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(main())






























