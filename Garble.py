# Garble, Version 0.1
# A Note taking program that simply appends your notes to a notes.txt file with simple meta data such as date and time... 
# Author: Feni Varughese

# Version 0.1: June 24, 2010
# Outputs to a simple text file

# Version 0.2: June 25, 2010
# Adds support for multi-line inputs
# Change in API to support this, by capturing the input at the method... 


# TODO: Switch to sqlite database for data storage
# 	Check and smart fix the format of the notes if previous one closed before fully written... 
# 	Support searching and sorting
#	Add viewing tools also
#	Auto-tagging and more system-context sensitive meta data

import datetime	# import the datetime package to allow us to add in the time meta-data

def addNote():
	time = datetime.datetime.now()

	notes = open('GarbleNotes.txt', 'a')
	notes.write("\n<note>\n");
	
	notes.write("\t<year>");
	notes.write(str(time.year));
	notes.write("</year>\n");
	
	notes.write("\t<month>");
	notes.write(str(time.month));
	notes.write("</month>\n");
	
	notes.write("\t<day>");
	notes.write(str(time.day));
	notes.write("</day>\n");

	notes.write("\t<hour>");
	notes.write(str(time.hour));
	notes.write("</hour>\n");
	
	notes.write("\t<minute>");
	notes.write(str(time.minute));
	notes.write("</minute>\n");
	
	notes.write("\t<message>");
	
	content = raw_input(":")
	while content != "":
		notes.write("\n\t\t");		# Proper spacing and tabbing... for style reasons... 
		notes.write(content);
		content = raw_input(":")
	
	notes.write("\n\t</message>\n");	

	notes.write("</note>\n\n");
	notes.close();

addNote();
