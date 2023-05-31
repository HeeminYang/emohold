import os
from pydub import AudioSegment

# Directory of the MP4 files
input_dir = "/home/projects/Metaverse2021/Crop_Metaverse/저학년"

# Directory where the MP3 files should be saved
output_dir = "/home/projects/Metaverse2021/Crop_Metaverse/저학년_MP3"

# Get the names of the group 1 folders
group1_folders = os.listdir(input_dir)

# Iterate over the group 1 folders
for group1_folder in group1_folders:
    # Get the path to the group 1 folder
    group1_path = os.path.join(input_dir, group1_folder)

    # Create the group 1 folder in the output directory if it doesn't already exist
    output_group1_path = os.path.join(output_dir, group1_folder)
    if not os.path.exists(output_group1_path):
        os.makedirs(output_group1_path)

    # Get the names of the group 2 folders in the group 1 folder
    group2_folders = os.listdir(group1_path)

    # Iterate over the group 2 folders
    for group2_folder in group2_folders:
        # Get the path to the group 2 folder
        group2_path = os.path.join(group1_path, group2_folder)

        # Create the group 2 folder in the output directory if it doesn't already exist
        output_group2_path = os.path.join(output_group1_path, group2_folder)
        if not os.path.exists(output_group2_path):
            os.makedirs(output_group2_path)

        # Get the names of the MP4 files in the group 2 folder
        mp4_files = [f for f in os.listdir(group2_path) if f.endswith(".mp4")]

        # Iterate over the MP4 files
        for mp4_file in mp4_files:
            # Get the path to the MP4 file
            mp4_path = os.path.join(group2_path, mp4_file)

            # Get the name of the MP3 file
            mp3_file = mp4_file.replace(".mp4", ".mp3")

            # Get the path to the MP3 file
            mp3_path = os.path.join(output_group2_path, mp3_file)

            # Load the MP4 file using pydub
            mp4 = AudioSegment.from_file(mp4_path)

            # Save the MP4 file as MP3 using pydub
            mp4.export(mp3_path, format="mp3")