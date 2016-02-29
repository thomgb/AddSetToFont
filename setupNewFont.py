"""
This is the observer.
If a new font did open, than the dialog pops up.
"""


from mojo.events import addObserver
from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController

import unicodeRanges
from unicodeRanges import *
a = dir(unicodeRanges)
glyphSets=[]
for i in a:
	if i[0] != "_":
		newSet={'checkBox':False, 'glyphSet':i}
		glyphSets.append(newSet)

class setupNewFont(object):

    def __init__(self):
        addObserver(self, "setup", "newFontDidOpen")

    def setup(self, info):
        font = info["font"]

        class scherm(BaseWindowController):

        	def __init__(self):
        		self.w = FloatingWindow((320, 650), "")

        		self.w.fNtxt = TextBox((10,10,100,22), 'Family Name')
        		self.w.familyName = EditText((10,30,-30,22))

        		self.w.sNtxt = TextBox((10,60,100,22), 'Style Name')
        		self.w.styleName = EditText((10,90,-30,22))

        		columnDescriptions = [
        							  dict(title="", key="checkBox", cell=CheckBoxListCell(), width=15),
        							  dict(title="glyphSet")
        							]
        		self.w.list = List((0, 140, 200, -0),
        						   glyphSets,
        						   columnDescriptions=columnDescriptions,
        						   editCallback=self.listEditCallback,
        						   )
        		self.w.exe = Button((230,600, -30, 30), "exe", callback=self.exe)
        		self.w.open()

        	def listEditCallback(self, sender):
        		pass

        	def exe(self, sender):
        		mynewfont = []
        		items =  self.w.list.get()
        		for item in items:
        			if not item["checkBox"]:
        				continue
        			glyph_set = item["glyphSet"]
        			for glyph in eval(glyph_set):
        				 print glyph
        				 font.lib["public.glyphOrder"].append(glyph[1])
        		font.info.familyName = self.w.familyName.get()
        		font.info.styleName = self.w.styleName.get()
        		self.w.close()


        scherm()
setupNewFont()
