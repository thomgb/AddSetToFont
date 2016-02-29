"""
Add some glyphs to the font.
"""


from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController

import unicodeRanges
reload(unicodeRanges)
from unicodeRanges import *
a = dir(unicodeRanges)
glyphSets=[]

for i in a:
	if i[0] != "_":
	    newSet={'checkBox':False, 'glyphSet':i}
	    glyphSets.append(newSet)
f = CurrentFont()
glyphOrder = []
class addToFont(BaseWindowController):

	def __init__(self):
		self.w = FloatingWindow((320, 400), "")

		self.w.fNtxt = TextBox((10,10,100,22), 'Family Name')
		self.w.familyName = EditText((10,30,-30,22), f.info.familyName)

		self.w.sNtxt = TextBox((10,60,100,22), 'Style Name')
		self.w.styleName = EditText((10,90,-30,22), f.info.styleName)

		columnDescriptions = [
							  dict(title="", key="checkBox", cell=CheckBoxListCell(), width=15),
							  dict(title="glyphSet")
							]
		self.w.list = List((0, 140, 200, -0),
						   glyphSets,
						   columnDescriptions=columnDescriptions,
						   editCallback=self.listEditCallback,
						   )
		self.w.exe = Button((230,-50, -30, 30), "exe", callback=self.exe)
		self.w.open()

	def listEditCallback(self, sender):
		pass

	def exe(self, sender):
		for glyph in f.lib['public.glyphOrder']:
			glyphOrder.append(glyph)

		items =  self.w.list.get()
		for item in items:
			if not item["checkBox"]:
				continue
			glyph_set = item["glyphSet"]
			for glyph in eval(glyph_set):
				 #print glyph
				glyphOrder.append(glyph[1])
		f.glyphOrder = glyphOrder
		f.info.familyName = self.w.familyName.get()
		f.info.styleName = self.w.styleName.get()
		self.w.close()


addToFont()
