
# importing required modules
from PyPDF2 import PdfReader

import os
  
# Directory containing the files
folder_path = "output"

# Get list of files in the folder
files = os.listdir(folder_path)

# Loop through each file
for file in files:
    if "pdf" in file:
        print(f"\n\n\n{file}\n\n\n")
        # creating a pdf reader object
        reader = PdfReader(f"{folder_path}/{file}")
        
        # printing number of pages in pdf file
        print(len(reader.pages))
        
        # getting a specific page from the pdf file
        page = reader.pages[0]
        
        # extracting text from page
        text = page.extract_text()
        print(text)

        # Open the file in write mode
        with open(f"txt/{file.replace('pdf', 'txt')}", 'w') as file:
            # Write the string to the file
            file.write(text)