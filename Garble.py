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

def addNote():
	time = datetime.datetime.now()

	filename = "GarbleNotes.xml";
	fileSize = os.path.getsize(filename)
	
	if fileSize < 14:	# File formatting is somehow messed up. Doesn't contain the root nodes. 
		notes = open(filename, 'w+');
		notes.write("<root>\n</root>");
		notes.close();

	notes = open(filename, "r+");	
	notes.seek(os.path.getsize(filename) - 8)	# seek to right before the </root>

	# write this note in... 		
	notes.write("\n\t<note>\n");
	
	notes.write("\t\t<meta>\n");
	notes.write("\t\t\t<time>\n");
	
	notes.write("\t\t\t<year>");
	notes.write(str(time.year));
	notes.write("</year>\n");
	
	notes.write("\t\t\t<month>");
	notes.write(str(time.month));
	notes.write("</month>\n");
	
	notes.write("\t\t\t<day>");
	notes.write(str(time.day));
	notes.write("</day>\n");

	notes.write("\t\t\t<hour>");
	notes.write(str(time.hour));
	notes.write("</hour>\n");
	
	notes.write("\t\t\t<minute>");
	notes.write(str(time.minute));
	notes.write("</minute>\n");
	
	notes.write("\t\t</time>\n");
	notes.write("\t</meta>\n");
	
	notes.write("\t\t<message>");
	
	content = raw_input(":");
	while content != "":
	#	notes.write("\n\t\t\t");		# Proper spacing and tabbing... for style reasons... 
		notes.write("\n");			# Omit tabbing so that we can preserve it using Pre Tag when doing XML rendering...
		notes.write(content);
		content = raw_input(":")
	
	notes.write("\n\t\t</message>\n");	
	notes.write("\t</note>\n");
	
	notes.write("</root>");	
	notes.close();

addNote();
