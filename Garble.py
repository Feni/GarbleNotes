# Garble, Version 0.1
# A Note taking program that simply appends your notes to a notes.txt file with simple meta data such as date and time... 
# Author: Feni Varughese

# Version 0.1: Outputs to a simple text file
# TODO: Switch to sqlite database for data storage
# 	Support searching and sorting
#	Add viewing tools also
#	Auto-tagging and more system-context sensitive meta data

import datetime	# import the datetime package to allow us to add in the time meta-data


def addNote(content):
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
	
	notes.write("\t<message>\n\t\t");
	notes.write(content);
	notes.write("\n\t</message>\n");	

	notes.write("</note>\n\n");
	notes.close();

newNote = raw_input(":");
addNote(newNote);
