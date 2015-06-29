import settings
import colors
import json
import itertools
from line import LineChart

class BarChart(LineChart):
	def __init__(self, labels, width=450, height=450, params={}):
		LineChart.__init__(self,labels,width,height,params)
		self.type = 'Bar'
		self.struct = 'bars'