import json

# Read JSON file
with open('your_path/output.json', 'r') as f:
    data = json.load(f)

# Create a new JSON data structure
new_data = {}
import numpy as np
def get_nonzero_intervals(arr):
    intervals = {}
    start = None
    end = None
    counter = 0
    for i, value in enumerate(arr):
        if value != 0:
            if start is None:
                start = i
            end = i
        else:
            if start is not None:
                intervals[counter]=[start, end]
                counter = counter +1
                start = None
                end = None

    if start is not None:
        intervals[counter]=[start, end]
        counter = counter +1
    return intervals

# Iterate through the data of each video
for video_id, video_data in data.items():
    # Save new list data
    new_video_data = {}
    count = np.zeros(20000)
    counter =0
    # Iterate through each list
    sorted_lists = sorted(video_data.items(), key=lambda x: int(x[1][0]))

    for i in range(len(sorted_lists)):
        list_id, lst = sorted_lists[i]
        start, end = lst
        if   end - start >0:
            for i in range(start,end):  
                count[i]=count[i]+1
                
    count[count<1]=0
    new_video_data=get_nonzero_intervals(count)
    
    # Add to a new data structure
    if new_video_data:
        new_data[video_id] = new_video_data

# Write the results to a new JSON file
with open('your_path/output_postprocess.json', 'w') as f:
    json.dump(new_data, f, indent=4)
