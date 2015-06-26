import settings
import colors
import json

class LineChart():
    
    def __init__(self, labels, width=450, height=450):
        self.embed = ' <canvas id="myChart" width="%s" height="%s"></canvas><script>var ctx = document.getElementById("myChart").getContext("2d");' %(str(width), str(height)) 
        self.x = labels
        self.y = {}

    def set_color(self,dimension, color_scheme):
        self.y[dimension].update(color_scheme)
        return dimension

    def add_dimension(self, name ,lst, options={}):
        self.y[name] = {"values": lst }
        self.set_color(name, colors.DEFAULT_BLUE)

        for key in options.keys():
            print options[key]
            if "color" in key and type(options[key]) == dict :
                options[key] = colors.construct_color(options[key].get("color", (0,0,0)) , options[key].get("opacity", 1 ))
        self.y[name].update(options)
    def update_dimension(self, name, key, value):
        self.y.get(name, {})[key] = value
    

    def build_chart(self):
        data  = { "labels": self.x, "datasets" : []}
        for dimension in reversed(self.y.keys()):
            line = { 
                "label": str(self.y[dimension].get('name')),
                "fillColor": self.y[dimension].get("fill_color"),
                "strokeColor": self.y[dimension].get("stroke_color"),
                "pointColor": self.y[dimension].get("point_color",),
                "pointStrokeColor": self.y[dimension].get("point_stroke_color"),
                "pointHighlightFill":self.y[dimension].get("point_highlight_fill_color"),
                "pointHighlightStroke": self.y[dimension].get("point_highlight_stroke_color"),
                "data": self.y[dimension].get("values",[])
            }
            data["datasets"].append(line)
        js_data = json.dumps(data)
        var = "var data = %s" % js_data
        chart = self.embed + "\n" + var
        chart = chart + "\n" + "var myLineChart = new Chart(ctx).Line(data); \n </script>" 
        return chart

    def build_html(self):
        html = '<html><head><title>Chart</title><script src= "http://www.chartjs.org/assets/Chart.js"></script> </head><body> %s' % self.build_chart()
        html = html + '</body></html>'
        return html

        
