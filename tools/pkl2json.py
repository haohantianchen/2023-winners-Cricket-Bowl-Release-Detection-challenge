import json
import pickle

# Read PKL file
with open('your_path/eval_results.pkl', 'rb') as f:
    data = pickle.load(f)

# Create a dict to store videos and their corresponding t-start and t-end
video_data = {}
counter =0

# Iterate through each key-value pair in the dict
for video_id, t_start, t_end,label in zip(data["video-id"], data["t-start"], data["t-end"],data["label"]):

    # Check if a record for this video already exists
    t_start=int(t_start*30)
    t_end=int(t_end*30)
    label = int(label)
    if video_id not in video_data:

        # If it doesn't exist, create a new record for the video and start numbering from 0
        counter = 0
        label=int(label)
        numlist = [t_start,t_end]
        video_data[video_id] = {
           counter:numlist,
        }
    else:
        counter = counter +1
        numlist = [t_start,t_end]

        # If a record of this video already exists, append new t-start and t-end and assign a new number
        video_data[video_id][counter]=[t_start,t_end]


# Write the results to a JSON file
with open('your_path/output.json', 'w') as f:
    json.dump(video_data, f, indent=4)
