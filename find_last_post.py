import re
import os
from datetime import datetime, timedelta


# Regular expression pattern to match timestamp format

pattern1 = r'\b\d+[A-Za-z]{1,2}\b'
pattern2 = r'\b[A-Za-z]{3,9} \d{1,2} at \d{1,2}:\d{1,2}\b'
pattern3 = r'\b[A-Za-z]{3,9} \d{1,2}, \d{4}'
pattern4 = r'\b[A-Za-z]{3,9} \d{1,2}'
pattern5 = r'\bYesterday at \d{1,2}:\d{1,2}\b'

#timestamp_pattern = f"{pattern2}|{pattern3}|{pattern2}"




# Function to extract last post timestamp from a file
def extract_last_timestamp(file_path):
    try:
        with open(f"txt/{file_path}", 'r') as file:
            page_dump = file.read()
            name_raw = file_path.replace(".txt", "")

            name_clean_pattern = r'\(\d+\)'
            name = re.sub(name_clean_pattern, '', name_raw)

            combined_pattern = ("|".join([pattern2, pattern3, pattern4, pattern5]))
            timestamp_pattern = rf"^(?!.*other)^.{{0,4}}{name}..*?(?:\n.*?|)({combined_pattern})"
            #print(timestamp_pattern)
            timestamps = re.findall(timestamp_pattern, page_dump, flags=re.MULTILINE)
            if timestamps:
                return timestamps[0]
            else:
                timestamp_pattern = rf"^(?!.*other|friends)^.{{0,4}}{name}.*?(?:\n.*?|)(?!.*friends)({pattern1})"
                timestamps = re.findall(timestamp_pattern, page_dump, flags=re.MULTILINE)
                if timestamps:
                    return timestamps[0]
                else:
                    return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def extract_any_last_timestamp(file_path):
    try:
        with open(f"txt/{file_path}", 'r') as file:
            page_dump = file.read()

            combined_pattern = ("|".join([pattern3, pattern2]))
            timestamp_pattern = rf"({combined_pattern})"
            #print(timestamp_pattern)
            timestamps = re.findall(timestamp_pattern, page_dump)
            if timestamps:
                return timestamps[-1]
            else:
                return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


files = os.listdir("txt")

no_posts = []

posts = []

# Iterate through the list of files and extract last post timestamps
for file_path in files:
    data = f"{file_path}|"
    #print(f"File: {file_path}")
    last_timestamp = extract_last_timestamp(file_path)

    data += f"{last_timestamp}|"
    if last_timestamp:
        #print(last_timestamp)
        data += f"None"
    else:
        #print("No post found.")
        no_posts.append(file_path)
        other_ts = extract_any_last_timestamp(file_path)
        #print(other_ts)
        data += str(other_ts)
    posts.append(data)
        
print("\n".join(no_posts))

print("\n".join(posts))