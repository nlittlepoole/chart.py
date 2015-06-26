import settings
import colors
import json
import itertools
from line import LineChart

class StackedChart(LineChart):
	def __init__(self, labels, width=450, height=450):
		self.top = None
		self.opac = 1
		LineChart.__init__(self,labels,width,height)

	def add_dimension(self, name ,lst, options={}):
		mapped = []
		if self.top:
			for a,b in itertools.izip_longest(self.top,lst):
				b = b if b else 0
				c = a + b if a else b
				mapped.append(c)  
		else:
			mapped =lst
			self.top = mapped
		LineChart.add_dimension(self,name,mapped,options)
		col = options.get("fill_color", "rgba(151,187,205,1)")
		self.y[name]['fill_color'] = colors.construct_color(col, 1)