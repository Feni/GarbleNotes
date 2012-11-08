# Garble, Version 0.1
# A Note taking program that simply appends your notes to a notes.txt file with simple meta data such as date and time... 
# Author: Feni Varughese

# Version 0.1: June 24, 2010
# Outputs to a simple text file

# Version 0.2: June 25, 2010
# Adds support for multi-line inputs
# Change in API to support this, by capturing the input at the method... 

# Version 0.3: June 26, 2010
# Support for formatted display in a browser


# TODO: Switch to sqlite database for data storage
# 	Check and smart fix the format of the notes if previous one closed before fully written... 
# 	Support searching and sorting
#	Add viewing tools also
#	Auto-tagging and more system-context sensitive meta data
#	Insert Note id and note count ect. ect. meta data. 


import datetime	# import the datetime package to allow us to add in the time meta-data
import os;	# Allows us to get the filesize, which allows us to seek to the position right before </root>
import dircache;

def addNote():
	time = datetime.datetime.now()

	if os.path.exists("Notes") == False:
		print "Setting up Notes folder";
		os.mkdir("Notes");

	os.chdir("Notes")
	
	# 2010 020 416 305 900
	filedir = (time.year * 10**12) + (time.month * 10**10) + (time.day * 10**8) + (time.hour * 10**6) + (time.minute * 10**4) + (time.second * 10**2);
	
	tries = 0;
	while os.path.exists(str(filedir)) == True:
		filedir = filedir+1
		tries = tries+1		# Keep track of how many times we're adding, so that we don't overlap the second count. 
		if tries == 99:		# I'm sleepy. possibly a math bug here... check back when awake... 
			filedir-98;
			filedir*100;
	
	# Assuming that we no longer need filedir as a long. Converting to str permenentaly for optimization... to avoid repeted conversion...
	# and to avoid an extra variable. 
	
	filedir = str(filedir)	
	print "New Note. ID: "+filedir
	os.mkdir(filedir);

	os.chdir(filedir);				# Move to the folder specific for this note...
	content = open("content.txt", "w");
	message = raw_input(":");
	while message != "":		# Option to remove all the folder setup we did if no-message is written in...
		content.write(message);
		content.write("\n");
		message = raw_input(":")
	
	content.close();

addNote();
