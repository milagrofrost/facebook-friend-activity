# Facebook page scraper and activity stats record

This was a two night project that I scrapped together to figure out how dead my Facebook was.  How frequently do my "friends" post on the site?  

Facebook makes it difficult to scrape data off the site.  They obfuscate/encrypt their HTML code so simply inspecting and saving the code is not an option.  You need to basically do a screen catpure or browser window capture of the page and then OCR the text that is captured.  One issue with that is when you are attempting to automate screen caps of hundreds of pages, Facebook will slow your request way down after around 400-500 page loads.  So there are a few obstacles to this.  




# Steps

We use a few tools/scripts to complete this task.
- Chrome
- Bardeen Chrome Extension
- Python

## Get the list of Facebook friends URLs
- Go to your Facebook profile and click on the Friends tab.  
- Your Friends list will not fully populated at the start.  Facebook prevents you from seeing the whole list without putting in the work.
- At the friends list, scroll all the way down on the page, the Friends list will keep populating.  When the friends list looks to be  at the end you can stop scrolling.
- Now we need to Inspect the page to get our Friends list URLs
	- Using Developer Tools in Chrome, select the Elements tab in the Developer Tools sidebar
	- In the `<body>` section of the Elements, right click on the body and "Copy element"
- In your favorite IDE/text editor (that has regex capabilities) you'll need to find all instances of the Facebook URLs for your friends.
- Search for and extract all instances of \"https://www.facebook.com/.*?\" This will return every Facebook URL that was on that page.  This will include more than friends URLs so you'll need to manually filter some of it out. 
- When you cleaned up that listto just Friends URLs, save it to a Google Sheet and give that sheet a name.

## Bardeen

Bardeen is a Chrome extension that can automate things in your browser.  We'll use this to automate scraping of Friends' pages

- Install the Chrome extension
	- https://chrome.google.com/webstore/detail/bardeen-automate-manual-w/ihhkmalpkhkoedlmcnilbbhhbhnicjga
- Use this template to use the page scraping workflow
	- https://bardeen.ai/s/UHVMEV4fZTI5
- When that workflow is in your Bardeen profile, you'll need to update it to work with your Google Sheet you made as well as updating the Google Drive where the screen caps will be saved.
- Before you start the Bardeen workflow, clear out your notifications in Facebook.  Having notifications appends a (1) to your screen cap files.  You can remove that later in post, but thats one less step.  
- Once thats setup you can run the workflow and it should open every Facebook friend page one by one.  It will attempt to scroll down a few times to get a few pages of activity.
	- Try to keep your scrapes to about 300-400 Friends.  Anymore than that and Facebook will put you in timeout and you'll only be able to get one or two posts max from each Friend.  
- The screen caps will be saved to your Google drive in the location you specified when you edited the Bardeen Workflow.  
- The screen caps should have about 10 portions of the latest activity.
- Download the screen caps in your Google drive to your computer.

## Using Python to clean up file names

- The screen caps will be saved as the Title of the page in your Browser.  We need to clean up the files names to only include the person's name.
- This Screen caps will usually look like this "Firstname Lastname _ Facebook.pdf" or "(1) Firstname Lastname _ Facebook.pdf" if you didn't clear notifications.  
- You can use the python script "rename_files.py" to clear out the unwanted text from the file names.  Assuming you saved the screen caps in a folder called "output" adjacent to the script.

## Using Python to OCR the PDF

- Bardeen seems to only save the pages as a picture and does not preserve the text.  So we need to Extract the text out of the picture.
- You'll need to install the python module "PyPDF2" for this to work.  `pip install PyPDF2` 
- Use the python script "pdf-to-tx.py" to start OCR'ing your PDFs.  Assuming you saved the screen caps in a folder called "output" adjacent to the script. And you created a folder called "txt" adjacent to the "output" foler
- This should save the OCR'd content to the "txt" folder

## Extract the dates from your Friends pages

- Now for the "fun" part.  What you've been waiting for.  
- Now that you have your Friends pages in text format (as best as possible), now we can start looking for the last post they made.
- Use the python script "find_last_post.py" to look for and output the dates of your friends.  It will output three things.  
	- Their name
	- The last post timestamp they posted personally.  Doesn not include posts where they were mentioned or posts that other people made on their page
	- If not personal post was found ,the script will attempt to find the oldest activity on their page.  This will get an idea of how far back the screen cap went and you can assum they haven't posted anything at least since the oldest activity.  
- Facebook timestamps posts a few different ways which is hella fustrating.  The regex in the script tries to accomodate for those different formats, and sometimes can fail spectacularly.
- Here are some exmaple formats:
	- March 10, 2023
	- March 10, 2023 at 10:58 PM
	- March 10
	- Yesterday at 10:58 PM
	- AND THE DREADED 12h, 3d or 4w or 2y.  It's harder to find these ones.
	
## CLEANUP!!!

-	In the output of the last python script you'll have the CSV outputted.  Copy the CSV portion and paste to Google Sheets.
-	Split the CSV to columns and get to work cleaning up the trash.
-	Select the columns that are supposed to dates and format them as dates
-	I had about a 60% success rate on getting a valid date.  The ones that were not recognized by Google Sheets as dates I had to manually update so it could read them.
-	Some values are just trash and didn;t pickup an acutal date.  You can always go back play with the regex to see if you can knockout false values, or just manually go through Facebook friends profile to find a date.  
-	When you get the dates all cleaned up, how you use it is up to you!!