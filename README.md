# Badger Cam Editor

## Hi Morgan 

To run this I think you need to...

```bash

git clone https://github.com/Intentional-Industries/badgerCamEditor.git

cd badgerCamEditor

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

mkdir src/input_directory src/output_directory src/segment_directory src/processed_directory

chmod -R u+w src/input_directory src/output_directory src/segment_directory src/processed_directory 

# now put the source file in src/input_directory

python3 src/main/py



```

we're aiming for 

```bash
badgerCamEditor/
├── venv/                 # Virtual environment (shouldn't be included in the repo)
├── src/                  # Source code for the project
│   ├── animal_detector.py # Detection script
│   ├── main.py           # Main script
│   └── video_stitcher.py  # Stitching script
│   ├── utils
|       ├── compressor.py      # turns avi to mp4
|       ├── restoreProcesses.py # cleans up a mess if files are in the wrong place
├── requirements.txt      # Dependency list (included in the repo)
└── .gitignore            # File to ignore unnecessary files like venv/
```
then just run the main.py script and hide behind your wall incase your lap top blows up



