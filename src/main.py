import os
import shutil
from animal_detector import detect_and_cut
from video_stitcher import concatenate_segments

# Paths
input_directory = 'input_directory'
output_directory = 'output_directory'
segment_directory = 'segment_directory'
processed_directory = 'processed_directory'  # Directory for processed files
model_path = 'yolov8x.pt'  # Path to your YOLO model

# Create output, segment, and processed directories if they don't exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(segment_directory, exist_ok=True)
os.makedirs(processed_directory, exist_ok=True)

# List of animals we're interested in detecting
detected_animals = ['fox', 'deer', 'squirrel', 'badger']

# Main loop to process all videos in the input directory
for video_file in os.listdir(input_directory):
    if video_file.endswith('.mp4') or video_file.endswith('.avi'):
        video_path = os.path.join(input_directory, video_file)
        video_name, _ = os.path.splitext(video_file)
        
        print(f"Processing {video_name}...")
        
        # Detect animals and cut segments
        segment_list_file = detect_and_cut(video_path, segment_directory, model_path, detected_animals)
        
        # If segments were found, stitch them together
        if segment_list_file:
            final_output = os.path.join(output_directory, f'{video_name}_stitched.mp4')
            concatenate_segments(segment_list_file, final_output)
            print(f"Stitched video created for {video_name}")
        else:
            print(f"No animals detected in {video_name}. Skipping stitching.")
        
        # Move the processed file to the processed directory
        processed_file_path = os.path.join(processed_directory, video_file)
        shutil.move(video_path, processed_file_path)
        print(f"Moved {video_file} to {processed_directory}")
            
print("All videos processed and moved!")
