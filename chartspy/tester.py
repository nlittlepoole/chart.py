from chartspy import *
from chartspy.colors import *
import datetime
import random

numdays = 5
base = datetime.datetime.today()
date_list = [(base - datetime.timedelta(days=x)).strftime("%B %d, %Y") for x in range(0, numdays)]

a = random.sample(xrange(100), numdays)
b = random.sample(xrange(100), numdays)

x = LineChart(date_list, params= {"pointDot" : True})
x.add_dimension("Line 1",a, options=DEFAULT_GREEN)
x.add_dimension("Line 2",b)
x.set_color("Line 2", DEFAULT_RED )

#x = DoughnutChart([{"label": "test", "value":300}, {"label": "test2", "value":100},{"label": "test3", "value":200}  ])
#print x.build_chart()
print x.build_html()
