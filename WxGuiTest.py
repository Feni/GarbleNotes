import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Garble", size=(500,150))
		self.textfield = wx.TextCtrl(self, style=wx.TE_MULTILINE)
	        self.Bind(wx.EVT_CLOSE, self.OnExit)		# Allows us to autosave on close. 
		self.Show(True)

	def OnExit(self,event):
       		print "You wrote: "+self.textfield.GetValue()
	        self.Destroy()
		
app = wx.App(False)
frame = MyFrame()
app.MainLoop()
