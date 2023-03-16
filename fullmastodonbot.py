import os
import random
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Set the folder path where the video files are located
folder_path = "/filepath"

# Set the output file name
output_file_name = "randomnewclip.mp4"

# Set the duration of the clip
duration = 50

# Get a list of all the video files in the folder
video_files = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mov", ".mkv"))]

# Choose a random video file from the list
random_video_file = random.choice(video_files)

# Create a VideoFileClip object from the random video file
video = VideoFileClip(os.path.join(folder_path, random_video_file))

# Get the duration of the video
video_duration = video.duration

# Choose a random start time for the clip
start_time = random.uniform(0, video_duration - duration)

# Set the end time of the clip
end_time = start_time + duration

# Clip the video
clip = video.subclip(start_time, end_time)

# Get the audio from the video
audio = clip.audio

# Write the clip to a new file with the audio
clip_with_audio = clip.set_audio(audio)
clip_with_audio.write_videofile(os.path.join(folder_path, output_file_name))

print("The new video file has been created successfully!")

from mastodon import Mastodon
import time

mastodon = Mastodon(
    access_token = 'secret token',
    api_base_url = 'https://botsin.space/'
)

media_file = 'output file'
media_id = mastodon.media_post(media_file, description='This is my video clip!')
try:
    mastodon.status_post('This is my video clip!', media_ids=[media_id])

except:
    print("30s delay")
    time.sleep(30)
    mastodon.status_post('This is my video clip!', media_ids=[media_id])

finally:
    print("Toot posted successfully!")