# Import required libraries
import os
import requests



# Set directory containing MP4 files
mp4_dir = "/home/heemin/mv/test/data"

# Set directory to save converted MP3 files
mp3_dir = "/home/heemin/mv/test/out"

# Set directory to save converted MP3 files
txt_dir = "/home/heemin/mv/test/files"

# Set CLOVA Speech Recognition API URL
api_url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=ko"

# Set CLOVA Speech Recognition API key
api_key = "wv4mxKVHVqMkmLc8ibIe"
api_secret = "l5mlJs2lkB8AV4KqicqpXpP2RGloWSpIClhGYoZM"

# Iterate over all files in the MP4 directory
for file in os.listdir(mp4_dir):
  # Check if file is an MP4 file
  if file.endswith(".mp4"):
    # Get the full path of the MP4 file
    mp4_file = os.path.join(mp4_dir, file)
    # Get the file name without the extension
    mp3_file = os.path.splitext(file)[0]
    # Use FFmpeg to convert the MP4 file to MP3
    os.system(f"ffmpeg -i {mp4_file} {mp3_dir}/{mp3_file}.mp3")
    # Read the MP3 file into memory
    with open(f"{mp3_dir}/{mp3_file}.mp3", "rb") as audio_file:
        # Set the request headers
        headers = {
        "X-NCP-APIGW-API-KEY-ID": api_key,
        "X-NCP-APIGW-API-KEY": api_secret,
        "Content-Type": "application/octet-stream",
        }
        # Send the request to the CLOVA Speech Recognition API
        response = requests.post(api_url, headers=headers, data=audio_file)       
        # Get the transcribed text
        text = response.text
        # Save the transcribed text to a file
    with open(f"{txt_dir}/{mp3_file}.txt", "w") as text_file:
        text_file.write(text)