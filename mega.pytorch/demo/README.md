# Demo Usage

The demo script supports visualization for video object detection. It can process an image folder consisting of frames decoded from a video or process a video file directly. Currently, the demo has been tested with `.mp4` files, but other video formats should also be compatible.

## Requirements

This demo uses the UCF50 dataset which can be downloaded and extracted with the following Python script:

```python
import os
import urllib.request
import rarfile

UCF50_URL = 'https://www.crcv.ucf.edu/data/UCF50.rar'
UCF50_PATH = 'datasets/UCF50.rar'

# Download and extract the UCF50 dataset
urllib.request.urlretrieve(UCF50_URL, UCF50_PATH)
with rarfile.RarFile(UCF50_PATH) as rf:
    rf.extractall()
os.remove(UCF50_PATH)
```

Ensure to have the `rarfile` Python package installed before running the script:

```shell
pip install rarfile
```

## Inference on an Image Folder

Run the following command to start inference on an image folder:

```shell
python demo/demo.py ${METHOD} ${CONFIG_FILE} ${CHECKPOINT_FILE} [--visualize-path ${IMAGE_FOLDER}] [--suffix ${IMAGE_SUFFIX}] [--output-folder ${FOLDER}] [--output-video]
```

**Example**:

```shell
python demo/demo.py base configs/vid_R_101_C4_1x.yaml R_101.pth --suffix ".JPEG" --visualize-path datasets/ILSVRC2015/Data/VID/val/ILSVRC2015_val_00003001 --output-folder visualization [--output-video]
```

## Inference on a Video

To perform inference on a video, use the command:

```shell
python demo/demo.py ${METHOD} ${CONFIG_FILE} ${CHECKPOINT_FILE} --video [--visualize-path ${VIDEO_PATH}] [--output-folder ${FOLDER}] [--output-video]
```

**Example**:

```shell
python demo/demo.py base configs/vid_R_101_C4_1x.yaml R_101.pth --video --visualize-path datasets/ILSVRC2015/Data/VID/snippets/val/ILSVRC2015_val_00003001.mp4 --output-folder visualization [--output-video]
```

The following bash script can be used to automate the visualization process for multiple methods and videos:

```bash
#!/bin/bash

# Define the checkpoint
CHECKPOINT="R_101.pth"

# Define dataset paths
declare -a VIDEOS=(
    "datasets/UCF50/WalkingWithDog/v_WalkingWithDog_g10_c03.avi"
    "datasets/UCF50/WalkingWithDog/v_WalkingWithDog_g01_c01.avi"
    "datasets/UCF50/HorseRiding/v_HorseRiding_g10_c01.avi"
    "datasets/UCF50/Drumming/v_Drumming_g01_c03.avi"
)

# Define methods and configs
declare -A CONFIGS=(
    ["base"]="configs/vid_R_101_C4_1x.yaml"
    ["mega"]="configs/MEGA/vid_R_101_C4_MEGA_1x.yaml"
)

# Process videos
for METHOD in "${!CONFIGS[@]}"; do
    CONFIG="${CONFIGS[$METHOD]}"
    for VIDEO_PATH in "${VIDEOS[@]}"; do
        VIDEO_NAME=$(basename -- "$VIDEO_PATH")
        VIDEO_NAME="${VIDEO_NAME%.*}"
        OUTPUT_FOLDER="visualization/${METHOD}/${VIDEO_NAME}"
        mkdir -p "$OUTPUT_FOLDER"
        python demo/demo.py $METHOD $CONFIG $CHECKPOINT --video --visualize-path "$VIDEO_PATH" --output-folder "$OUTPUT_FOLDER" --output-video
        echo "Visualization for $VIDEO_NAME with $METHOD method complete."
    done
done

echo "All visualizations complete."
```

To execute this script:

1. Give it execute permissions:
   ```shell
   chmod +x demo/run_visualisations.sh
   ```

2. Run the script:
   ```shell
   ./demo/run_visualisations.sh
   ```

This script will generate visualisations for each video in the `VIDEOS` array, using both the 'base' and 'mega' methods as specified, and will save the results in separate folders under `visualization/${METHOD}/${VIDEO_NAME}`.

Note: The `--output-video` argument specifies that the output should be a video. If you prefer to save each frame's visualisation as an image, omit this argument.