import os

# Directory containing the files
folder_path = "output"

# String to be removed from file names
string_to_remove = " _ Facebook"

# Get list of files in the folder
files = os.listdir(folder_path)

# Loop through each file
for file in files:
    # Check if the file name contains the string to be removed
    if string_to_remove in file:
        # Construct the new file name by replacing the string to be removed with an empty string
        new_file_name = file.replace(string_to_remove, "")
        # Construct the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_file_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File '{file}' has been renamed to '{new_file_name}'")