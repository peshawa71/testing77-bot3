# import subprocess
# print("may its working")

# input_file = "main_video.mp4"
# output_file = "hhhhh.mp4"

# # Trim from 5 to 10 seconds without re-encoding (super fast)
# cmd = [
#     "ffmpeg",
#     "-i", input_file,     # input file
#     "-ss", "5",           # start time
#     "-to", "10",          # end time
#     "-c", "copy",         # copy streams (no re-encoding)
#     output_file
# ]

# subprocess.run(cmd, check=True)
# print("Video edited and saved as", output_file)

# main.py
# import os
# from moviepy.editor import VideoFileClip

# video_path = "main_video.mp4"
# print(os.path.exists(video_path))  
# # Check if file exists
# if not os.path.exists(video_path):
#     raise FileNotFoundError(f"The file '{video_path}' does not exist!")

# # If it exists, proceed
# clip = VideoFileClip(video_path)

# # Cut 5s → 15s


# # Export
# clip.write_videofile("cut.mp4", codec="libx264", audio_codec="aac", fps=24)




# --- lerawa bo xwarawa be kesha esh akat>>>



# from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
# import os
# from dotenv import load_dotenv
# from telethon.sync import TelegramClient
# from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
# from telethon.tl.types import InputPeerChannel
# import tqdm


# # Load .env
# load_dotenv()
# # api_id = int(os.getenv("API_ID"))
# # api_hash = os.getenv("API_HASH")
# api_id = int(os.getenv("APITELEGRAM_ID")) 
# api_hash = os.getenv("APITELEGRAM_HASH")

# # api_id = 
# # api_hash = ""
# # channel_to_send = -1002384585674
# channel_to_send = -1002332921402

# DOWNLOADS_DIR = "taste"
# os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# client = TelegramClient("session_name", api_id, api_hash)
# client.start()
# path = "editings"
# os.makedirs(path, exist_ok=True) 
# import os

# def create_path(path_str):
#     """
#     Create each directory in the given path one by one if it doesn't exist.
#     Example: sponsor/taste/i
#     """
#     parts = path_str.split(os.sep)  # split by folder separator (/ or \)
#     current_path = ""

#     for part in parts:
#         if not part:  # skip empty parts (e.g., if path starts with /)
#             continue
#         current_path = os.path.join(current_path, part)
#         if not os.path.exists(current_path):
#             os.mkdir(current_path)
#             print(f"Created: {current_path}")
#         else:
#             print(f"Exists: {current_path}")

# def get_available_filename(base_name, ext=".mp4"):
#     i = 1
#     filename = f"{base_name}{ext}"
#     while os.path.exists(filename):
#         filename = f"{base_name}_{i}{ext}"
#         i += 1
#     return filename

# def edit_image(path="sponsors1/images/screensponsor1.jpg"):
#     from moviepy.editor import ImageClip

#     # Load an image
#     clip = ImageClip(path)

#     # Add duration (since MoviePy works with video, even for images you need duration)
#     clip_with_duration = clip.set_duration(5)  # 5 seconds

#     # Save it as a video
#     print("editing... loading")
#     clip2 = clip_with_duration.write_videofile("editings/edited_pic.mp4", fps=24)
#     print(f"edited : {clip}")
#     print("sending... loading")
#     # connect to Telegram

#     return "editings/edited_pic.mp4"

#     # send video to "Saved Messages" (or replace with friend's username/chat_id)


# def download_sponsor_videos(chat, limit):

#     messages = client.get_messages(chat, limit=limit)

#     reverse_data = messages[::-1]


#     for msg in tqdm.tqdm(reverse_data):

#         # if msg.media and not msg.id == 9 and not msg.id == 4:
#         if msg.media and "screensponsor1" in msg.text:
#             # current_path1 = create_path(f"taste/{msg.text}")
#         # if msg.media: and "sponsor_onscreen" in msg.text 


#             # for message2 in tqdm.tqdm(messages) if message2.media and "چیرۆکی شەوێک" in message2.text and message2.id == max_id:
#             #     current_max_id = msg.id
#             #     DOWNLOAD_VIDEO = message2

            

#             try:

#                 namefile = get_available_filename(f"sponsors1/{msg.message}")
#                 if "image" in msg.text.lower():
#                     namefile = get_available_filename(f"sponsors1/{msg.message}", "")
                    


#                 print(f"\n📥 Downloading media from message ID {msg.id} {msg.text} loading...")
#                 filename = client.download_media(msg, namefile)
#                 print(f"{filename} dowmnloaded")

#                 if filename:

#                     print(f"\n✅ Downloaded: {filename}")

#                     image_video = edit_image(filename)

#                     client.send_file("completed1", image_video, caption="Here is the video 🎬")
#                     print("sented to channel you provided")

                    

#             except Exception as e:
#                 print(f"❌ file Error : {e}")

# download_sponsor_videos("sponsor_hadia", 2)

# --- ta era, era alem xapa gyan >>>
# # watch again bro for ...
# from telethon import TelegramClient

# api_id = 1234567  # your API ID
# api_hash = 'your_api_hash'
# channel = 'https://t.me/your_channel_username'  # or channel ID

# client = TelegramClient('session_name', api_id, api_hash)

# async def send_video():
#     await client.start()

#     await client.send_file(
#         entity=channel,
#         file='your_video.mp4',
#         caption="🎬 Watch this video!",
#         supports_streaming=True,  # This is what makes it playable without download
#         thumb='thumbnail.jpg'  # Optional: add custom thumbnail
#     )

# with client:
#     client.loop.run_until_complete(send_video())

from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.tl.types import InputPeerChannel
import tqdm
import requests

api_id = int(os.getenv("APITELEGRAM_ID")) 
api_hash = os.getenv("APITELEGRAM_HASH")
from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.tl.types import InputPeerChannel
import tqdm
import requests

url = "https://i.ibb.co/Zp45mK3s/logo-gull2bigger.png"  # your direct link
response = requests.get(url)
path11 = "sponsors1/images"
os.makedirs(path11, exist_ok=True)
with open(f"{path11}/logo.png", "wb") as f:
    f.write(response.content)

print("Logo downloaded as logo.png")


# Load .env
load_dotenv()
# api_id = int(os.getenv("API_ID"))
# api_hash = os.getenv("API_HASH")
# api_id = int(os.getenv("APITELEGRAM_ID")) 
# api_hash = os.getenv("APITELEGRAM_HASH")

# api_id = 26361414
# api_hash = "3c2e0087748a3fc216f6eb807232c05d"
# channel_to_send = -1002384585674

api_id = 20158406
api_hash = "f0f4bc610215107583cd16e733c9cc38"
channel_to_send = -1002332921402
path = "editings"
os.makedirs(path, exist_ok=True) 

DOWNLOADS_DIR = "taste"
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

client = TelegramClient("session_name", api_id, api_hash)
client.start()

import os

def create_path(path_str):
    """
    Create each directory in the given path one by one if it doesn't exist.
    Example: sponsor/taste/i
    """
    parts = path_str.split(os.sep)  # split by folder separator (/ or \)
    current_path = ""

    for part in parts:
        if not part:  # skip empty parts (e.g., if path starts with /)
            continue
        current_path = os.path.join(current_path, part)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
            print(f"Created: {current_path}")
        else:
            print(f"Exists: {current_path}")

def get_available_filename(base_name, ext=".mp4"):
    i = 1
    filename = f"{base_name}{ext}"
    while os.path.exists(filename):
        filename = f"{base_name}_{i}{ext}"
        i += 1
    return filename

def make_video(path="sponsors1/images/sponsor2.jpg", path2="sponsors1/images/screensponsor1.jpg"):
    from moviepy.editor import ImageClip

    os.makedirs("sponsors1/images", exist_ok=True)
    os.makedirs("editings", exist_ok=True)
    os.makedirs("editings/export", exist_ok=True)


    # Load an image
    clip1 = ImageClip(path) 

    # Add duration (since MoviePy works with video, even for images you need duration)
    clip_with_duration = clip1.set_duration(20)  # 5 seconds

    # Save it as a video
    print("editing... loading")
    clip_with_duration.write_videofile("editings/new1.mp4", fps=24)
    clip2 = ImageClip(path2)
    clip2 = clip2.set_duration(5)  # 5 seconds
    clip2.write_videofile("editings/new2.mp4", fps=24)

    print(f"edited : {clip2}")
    print("sending... loading")
    # connect to Telegram

    return "completed"

    # send video to "Saved Messages" (or replace with friend's username/chat_id)

def vidoe_edit():
        
    from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips

    # === 1. Load your main video ===
    main = VideoFileClip("editings/new1.mp4")

    # === 2. Prepare the logo overlay ===
    logo = (
        ImageClip(f"{path11}/logo.png")
        .set_duration(main.duration)   # logo lasts for the whole video           # scale down
        .set_pos(("right", "top"))     # position (can be "bottom", "left", etc.)
    )

    # Overlay logo on the main video
    # main_with_logo = CompositeVideoClip([main, logo])

    # === 3. Cut the main video into parts ===
    # Example: cut 0–10 sec, skip 10–20 sec, keep 20–40 sec
    part1 = main.subclip(0, 5)
    part2 = main.subclip(5, 10)

    # === 4. Load the videos to insert ===
    insert1 = VideoFileClip("editings/new2.mp4")
    # insert2 = VideoFileClip("insert2.mp4")

    # === 5. Put everything together ===
    final = concatenate_videoclips([part1, insert1, part2, insert1])

    # === 6. Export the final video ===
    final.write_videofile("editings/export/final_output.mp4", fps=24)
    print("sending to channel you provided... loading")
    client.send_file("completed1", "editings/export/final_output.mp4", caption="Here is the video 🎬")


def download_sponsor_videos(chat, limit):

    messages = client.get_messages(chat, limit=limit)

    reverse_data = messages[::-1]


    for msg in tqdm.tqdm(reverse_data):

        # if msg.media and not msg.id == 9 and not msg.id == 4:
        if msg.media and "images" in msg.text:
            # current_path1 = create_path(f"taste/{msg.text}")
        # if msg.media: and "sponsor_onscreen" in msg.text 


            # for message2 in tqdm.tqdm(messages) if message2.media and "چیرۆکی شەوێک" in message2.text and message2.id == max_id:
            #     current_max_id = msg.id
            #     DOWNLOAD_VIDEO = message2

            

            try:

                # namefile = get_available_filename(f"sponsors1/{msg.message}")
                namefile = get_available_filename(f"sponsors1/{msg.message}", "")
                    


                print(f"\n📥 Downloading media from message ID {msg.id} {msg.message} loading...")
                filename = client.download_media(msg, namefile)
                print(f"{filename} dowmnloaded")

                if filename:

                    print(f"\n✅ Downloaded: {filename}")


                    # client.send_file("completed1", image_video, caption="Here is the video 🎬")
                    # print("sented to channel you provided")

                    

            except Exception as e:
                print(f"❌ file Error : {e}")

download_sponsor_videos("sponsor_hadia", 50)
make_video()
vidoe_edit()
# # watch again bro for ...
# from telethon import TelegramClient

# api_id = 1234567  # your API ID
# api_hash = 'your_api_hash'
# channel = 'https://t.me/your_channel_username'  # or channel ID

# client = TelegramClient('session_name', api_id, api_hash)

# async def send_video():
#     await client.start()

#     await client.send_file(
#         entity=channel,
#         file='your_video.mp4',
#         caption="🎬 Watch this video!",
#         supports_streaming=True,  # This is what makes it playable without download
#         thumb='thumbnail.jpg'  # Optional: add custom thumbnail
#     )

# with client:
#     client.loop.run_until_complete(send_video())

# # watch again bro for ...
# from telethon import TelegramClient

# api_id = 1234567  # your API ID
# api_hash = 'your_api_hash'
# channel = 'https://t.me/your_channel_username'  # or channel ID

# client = TelegramClient('session_name', api_id, api_hash)

# async def send_video():
#     await client.start()

#     await client.send_file(
#         entity=channel,
#         file='your_video.mp4',
#         caption="🎬 Watch this video!",
#         supports_streaming=True,  # This is what makes it playable without download
#         thumb='thumbnail.jpg'  # Optional: add custom thumbnail
#     )

# with client:
#     client.loop.run_until_complete(send_video())


