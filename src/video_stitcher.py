import subprocess
import os

# Directory where the video segments are stored
segment_directory = 'output_segments'
output_file = 'final_output.mp4'

# Create a list of all the segment files
segment_files = [f for f in os.listdir(segment_directory) if f.startswith('output_segment_') and f.endswith('.mp4')]

# Write the list of segments to a file for FFmpeg
with open('segment_list.txt', 'w') as f:
    for segment in sorted(segment_files):
        f.write(f"file '{os.path.join(segment_directory, segment)}'\n")

# FFmpeg command to concatenate the segments
concat_command = [
    'ffmpeg',
    '-f', 'concat',               # Concatenation mode
    '-safe', '0',                 # Allow relative paths
    '-i', 'segment_list.txt',     # Input list of files
    '-c', 'copy',                 # Copy codecs (no re-encoding)
    output_file                   # Output file
]

# Run the FFmpeg concatenation command
subprocess.run(concat_command)

print(f"Video segments concatenated into {output_file}")
