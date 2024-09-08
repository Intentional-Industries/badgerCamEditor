# Badger Cam Editor

## Hi Morgan 

To run this I think you need to...

```bash

git clone https://github.com/Intentional-Industries/badgerCamEditor.git

cd badgerCamEditor

python3 -m venv venv

source venv/bin/activate

```

we're aiming for 

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


then just run the main.py script and hide behind your wall incase your lap top blows up



