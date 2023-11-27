# CHOOSING THE DIFFERENT VIDEOS CAN BE DONE IN THE SCRIPT BELOW 
# THEY HAVE BEEN DOWNLOADED FROM THE UCF 50 DATASET - 
# TO RUN THIS IN THE COMMAND LINE
# chmod +x demo/run_visualisations.sh
# ./demo/run_visualisations.sh


#!/bin/bash

# Define the checkpoint
CHECKPOINT="R_101.pth"

# Define your dataset paths
declare -a VIDEOS=(
    "datasets/UCF50/WalkingWithDog/v_WalkingWithDog_g10_c03.avi"
    "datasets/UCF50/WalkingWithDog/v_WalkingWithDog_g01_c01.avi"
    "datasets/UCF50/HorseRiding/v_HorseRiding_g10_c01.avi"
    "datasets/UCF50/Drumming/v_Drumming_g01_c03.avi"
)

# Define methods and their corresponding config files
declare -A CONFIGS=(
    ["base"]="configs/vid_R_101_C4_1x.yaml"
    ["mega"]="configs/MEGA/vid_R_101_C4_MEGA_1x.yaml"
)

for METHOD in "${!CONFIGS[@]}"; do
    CONFIG="${CONFIGS[$METHOD]}"
    for VIDEO_PATH in "${VIDEOS[@]}"; do
        # Extract video name without extension and parent folders
        VIDEO_NAME=$(basename -- "$VIDEO_PATH")
        VIDEO_NAME="${VIDEO_NAME%.*}"
        
        # Set the output folder
        OUTPUT_FOLDER="visualization/${METHOD}/${VIDEO_NAME}"

        # Create the output folder
        mkdir -p "$OUTPUT_FOLDER"

        # Run the command
        python demo/demo.py $METHOD $CONFIG $CHECKPOINT --video \
            --visualize-path "$VIDEO_PATH" \
            --output-folder "$OUTPUT_FOLDER" --output-video

        echo "Visualization for $VIDEO_NAME with $METHOD method complete."
    done
done

echo "All visualizations complete."