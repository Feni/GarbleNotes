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

	dirlist = dircache.listdir('Notes')
	filedir = str(len(dirlist));	# Bug of overwriting over an existing folder if we delete a file and the count messes up. 
	print "There are currently "+filedir+" notes in the Notes folder ";
		
	os.chdir("Notes")
	os.mkdir(filedir);				# Convention: Start at message 0...
	os.chdir(filedir);				# Move to the folder specific for this note...
	
	filename = "meta.xml";	
	notes = open(filename, "w");

	# write this note in... 
	notes.write('<?xml version="1.0" encoding="UTF-8" ?>');
	notes.write("<note id = '"+filedir+"'>");
	
	notes.write("<created>");
	notes.write("<year>");
	notes.write(str(time.year));
	notes.write("</year>");
	
	notes.write("<month>");
	notes.write(str(time.month));
	notes.write("</month>");
	
	notes.write("<day>");
	notes.write(str(time.day));
	notes.write("</day>");

	notes.write("<hour>");
	notes.write(str(time.hour));
	notes.write("</hour>");

	notes.write("<minute>");
	notes.write(str(time.minute));
	notes.write("</minute>");

	notes.write("</created>");
	notes.write("<content type='text' src = 'content.txt'>");# I can't embed the content directly, since it might mess up the xml validity
	notes.write("</content>");
	notes.write("</note>");
	
	os.mkdir("Content");	# Create a new sub folder for all content to prevent file-name conflicts with the meta data files. 
	os.chdir("Content")

	content = open("content.txt", "w");
	
	message = raw_input(":");
	while message != "":		# Option to remove all the folder setup we did if no-message is written in...
		content.write(message);
		content.write("\n");
		message = raw_input(":")
		
	notes.close();

addNote();
