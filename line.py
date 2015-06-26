import settings
import colors
import json

class LineChart():
    
    def __init__(self, labels):
        self.embed = settings.CANVAS
        self.x = labels
        self.y = {}

    def add_dimension(self, name ,lst, options={}):
        self.y[name] = {"values": lst }
        for key in options.keys():
            if "color" in key:
                options[key] = colors.construct_color(options[key].get("color", (0,0,0)) , options[key].get("opacity", 1 ))
        self.y[name].update(options)

    def update_dimension(self, name, key, value):
        self.y.get(name, {})[key] = value
    

    def build_chart(self):
        data  = { "labels": self.x, "datasets" : []}
        for dimension in self.y.keys():
            print "dimension", dimension, self.y
            line = { 
                "label": str(self.y[dimension].get('name')),
                "fillColor": self.y[dimension].get("fill_color","rgba(255,0,0,.2)"),
                "strokeColor": self.y[dimension].get("stroke_color","rgba(220,220,220,1)"),
                "pointColor": self.y[dimension].get("point_color","rgba(220,220,220,1)"),
                "pointStrokeColor": self.y[dimension].get("point_stroke_color","#fff"),
                "pointHighlightFill":self.y[dimension].get("point_highlight_fill_color", "#ff0000"),
                "pointHighlightStroke": self.y[dimension].get("point_highlight_stroke_color", "rgba(220,220,220,1)"),
                "data": self.y[dimension].get("values",[])
            }
            data["datasets"].append(line)
        js_data = json.dumps(data)
        var = "var data = %s" % js_data
        chart = self.embed + "\n" + var
        chart = chart + "\n" + "var myLineChart = new Chart(ctx).Line(data); \n </script>"
        return chart

        
