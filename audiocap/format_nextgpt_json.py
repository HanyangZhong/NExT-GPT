import os
import pandas as pd
import csv
import json


train_folder = '/hy-tmp/audiocap/all_audio/'
csv_file = 'aud.csv'

def csv_to_json(input_file, output_file,train_folder):
    # Initialize the resulting list
    results = []

    # Loop through the audio files in the train folder
    for filename in os.listdir(train_folder):
        if filename.endswith('.wav'):
            # Get the file name without extension
            name = os.path.splitext(filename)[0]
            print('name:',name)
    
            # Open the CSV file
            with open(input_file, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
        
                # Make sure to skip the header if there's one
                # next(csvreader)
        
                for idx, row in enumerate(csvreader):
                    # Assuming each ID is based on the index and there are two rows per conversation
                    
                    idnum = int(row[0])
                    # print(row)
                    conversation_id = f"{idnum}"  # Format the id to have leading zeros
                    # print(conversation_id)
                    audio_name = str(row[1])
                    audio = f"{row[1]}.wav"
                    # print(audio_name)
                    if name == audio_name:
                        print(audio)
                        # human_conversation1 = {
                        #     "from": "human",
                        #     "value": f"<audio>\nWhat is happening according to this audio?"
                        # }
            
                        # # Get the next row for GPT's response
                        # # gpt_response = next(csvreader)
                        # gpt_conversation1 = {
                        #     "from": "gpt",
                        #     "value": f"{row[4]}"
                        # }
            
                        result = {
                            "caption": f"{row[4]}",
                            "audio": audio
                        }
            
                        results.append(result)
        
    # Write the results to a JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(results, jsonfile, indent=2)


if __name__ == '__main__':
        
    # Read the CSV file into a DataFrame
    # df = pd.read_csv(csv_file) 
    
    # # Loop through the audio files in the train folder
    # for filename in os.listdir(train_folder):
    #     if filename.endswith('.wav'):
    #         # Get the file name without extension
    #         name = os.path.splitext(filename)[0]
    #         print('name:',name)
    #         # Find the row in the DataFrame with matching name
    #         row = df.loc[df['audiocap_id'] == name]
            
    #         # Process the row here
    #         print('row:',row)
    csv_to_json(csv_file, 'out.json',train_folder)