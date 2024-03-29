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
import wx; 	# Wxpython, our GUI framework. 


class Garble(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Garble", size=(500,150))
		self.textfield = wx.TextCtrl(self, style=wx.TE_MULTILINE)
	        self.Bind(wx.EVT_CLOSE, self.OnExit)		# Allows us to autosave on close. 
		self.Show(True)

	def OnExit(self,event):
	    try:
		self.checkNote(self.textfield.GetValue());
		self.Destroy()
	    except Exception, err:
		print("ERROR: %s\n" % str(err));		
		self.Destroy()

	
	def consoleNote(self):
		self.checkNote(self.consoleRead());
			
	def checkNote(self, message):
		if message != "":		#  && (message != "\n")
			self.outXML(message);
			self.addNote(message);
			
	def consoleRead(self):
		content = "";
		message = raw_input(":");
		while message != "":		# Option to remove all the folder setup we did if no-message is written in...
			content = content + message + "\n";
			message = raw_input(":")
		return content;

	def addNote(self, note):	# String note to be written in...
		time = datetime.datetime.now()
		if os.path.exists("Notes") == False:
			print "Setting up Notes folder";
			os.mkdir("Notes");

		os.chdir("Notes")
		# 2010 020 416 305 900
		noteID = (time.year * 10**12) + (time.month * 10**10) + (time.day * 10**8) + (time.hour * 10**6) + (time.minute * 10**4) + (time.second * 10**2);
		tries = 0;
		while os.path.exists(str(noteID)) == True:
			noteID = noteID+1
			tries = tries+1		# Keep track of how many times we're adding, so that we don't overlap the second count. 
			if tries == 99:		# I'm sleepy. possibly a math bug here... check back when awake... 
				noteID-98;
				noteID*100;
	
		# Assuming that we no longer need filedir as a long. Converting to str permenentaly for optimization... to avoid repeted conversion...
		# and to avoid an extra variable. 
	
		noteID = str(noteID)	
		os.mkdir(noteID);
		os.chdir(noteID);				# Move to the folder specific for this note...
		content = open("content.txt", "w");
		content.write(note);
		content.close();
		print "New Note ("+noteID+") added";

	# Note that XML output is depreciated and vulnerable to injection attacks. 
	def outXML(self, note):
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
	
		notes.write("\t\t<year>");
		notes.write(str(time.year));
		notes.write("</year>\n");
	
		notes.write("\t\t<month>");
		notes.write(str(time.month));
		notes.write("</month>\n");
	
		notes.write("\t\t<day>");
		notes.write(str(time.day));
		notes.write("</day>\n");

		notes.write("\t\t<hour>");
		notes.write(str(time.hour));
		notes.write("</hour>\n");
	
		notes.write("\t\t<minute>");
		notes.write(str(time.minute));
		notes.write("</minute>\n");
	
		notes.write("\t\t<message>");
		notes.write(str(note));		# Omit tabbing so that we can preserve it using Pre Tag when doing XML rendering...
		notes.write("\n");	
	
		notes.write("\n\t\t</message>\n");	
		notes.write("\t</note>\n");
	
		notes.write("</root>");	
		notes.close();
#addNote();


app = wx.App(False)
garble = Garble()
#garble.consoleNote();
app.MainLoop()

