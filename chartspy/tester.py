from line import LineChart
from stacked import StackedChart
import colors
import datetime
import random

numdays = 15
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

a = random.sample(xrange(100), numdays)
b = random.sample(xrange(100), numdays)

x = StackedChart(["Monday","Tuesday","Wednesday"])
x.add_dimension("Line 1",a, options=colors.DEFAULT_GREEN)
x.add_dimension("Line 2",b, options=colors.DEFAULT_RED)
x.set_color("Line 2", colors.DEFAULT_RED )
print x.build_chart()
print x.build_html()