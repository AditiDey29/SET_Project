#!/bin/bash

# Navigate to the main folder
cd kafka_results

# Loop through each subfolder from v0 to v99
for i in {0..99}; do
   
    folder="v$i"
    if [ -d "$folder" ]; then
        # Navigate into the subfolder
        cd "$folder"
        
        # Delete all files except lizard.txt
        find . -maxdepth 1 ! -name "lizard.txt" -type f -delete
        find . -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +
        
        # Navigate back to the main folder
        cd ..
    fi
done

