import os
import cv2
from ultralytics import YOLO
import subprocess

# Function to detect animals and cut video segments
def detect_and_cut(video_path, segment_directory, model_path, detected_animals):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_skip = 5  # Skip frames for efficiency
    frame_index = 0
    start_time = None
    end_time = None
    segments = []
    
    # Load YOLO model
    model = YOLO(model_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_index % frame_skip == 0:
            results = model(frame)
            animal_detected = False
            for result in results.pred:
                for obj in result:
                    class_name = model.names[int(obj[5])]
                    if class_name in detected_animals:
                        animal_detected = True
                        break
            
            if animal_detected:
                if start_time is None:
                    start_time = frame_index / frame_rate
                end_time = frame_index / frame_rate
            else:
                if start_time is not None and end_time is not None:
                    segments.append((start_time, end_time))
                    start_time = None
                    end_time = None
        
        frame_index += 1
    
    cap.release()

    # If any segments were found, process them
    if segments:
        segment_list_file = os.path.join(segment_directory, f'{video_name}_segments.txt')
        with open(segment_list_file, 'w') as f:
            for i, (start, end) in enumerate(segments):
                output_segment_file = os.path.join(segment_directory, f'{video_name}_segment_{i}.mp4')
                cut_video(video_path, start, end, output_segment_file)
                f.write(f"file '{output_segment_file}'\n")
        
        return segment_list_file

    return None

# Function to cut segments using FFmpeg
def cut_video(input_video, start_time, end_time, output_file):
    command = [
        'ffmpeg',
        '-i', input_video,
        '-ss', str(start_time),
        '-to', str(end_time),
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command)
