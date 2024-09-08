import os
import shutil
import subprocess

# Directory containing your AVI files
directory = '/Users/howardkitto/Movies/BadgerCam/apr-may-23'
output_directory = os.path.expanduser('~/CompressedMovies')  # Expands the '~' symbol to the home directory
processed_directory = os.path.expanduser('~/Movies/BadgerCam/deleteMe')  # Directory for processed files

# Make sure the output and processed directories exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(processed_directory, exist_ok=True)

# List all AVI files in the directory
avi_files = [filename for filename in os.listdir(directory) if filename.endswith(".AVI")]

# Print the number of files found
file_count = len(avi_files)
print(f"Found {file_count} AVI files.")

# Loop through each AVI file in the directory
for filename in avi_files:
    input_file = os.path.join(directory, filename)
    output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + "_compressed.mp4")
    
    # FFmpeg command to compress the video
    command = [
        'ffmpeg',
        '-i', input_file,                # Input file
        '-vcodec', 'libx264',            # H.264 codec
        '-profile:v', 'high',            # Use the high profile (supports 4:2:2)
        '-pix_fmt', 'yuv420p',           # Convert to yuv420p (4:2:0) for QuickTime compatibility
        '-crf', '23',                    # Constant Rate Factor (adjust this between 18-28, lower is better quality)
        '-preset', 'slow',               # Compression speed vs file size (can use 'medium' for faster compression)
        '-acodec', 'aac',                # Audio codec (AAC)
        '-b:a', '128k',                  # Audio bitrate
        '-movflags', '+faststart',       # Optimize for streaming/playback
        output_file                      # Output file
    ]
    
    print(f"Compressing {filename}...")
    result = subprocess.run(command)

    # If compression was successful, move the file to the processed directory
    if result.returncode == 0:
        processed_file = os.path.join(processed_directory, filename)
        shutil.move(input_file, processed_file)
        print(f"Moved {filename} to {processed_directory}")
    else:
        print(f"Compression failed for {filename}. File not moved.")

print("Compression completed!")
