from line import LineChart
x = LineChart(["Monday","Tuesday","Wednesday"])
x.add_dimension("Line 1",[1,2,3])
x.add_dimension("Line 2",[3,2,1], options={"fill_color":{"color":(0,255,0) , "opacity":.2 }})
print x.build_chart()
print x.build_html()