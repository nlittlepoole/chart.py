import settings
import colors
import json
import math
import random

class LineChart():
    
    def __init__(self, labels, width=450, height=450, params={}):
        self.embed = '<canvas id="myChart" width="%s" height="%s"></canvas><script>var canv= document.getElementById("myChart"); \n var ctx = canv.getContext("2d");' %( str(width), str(height) ) 
        self.type = 'Line'
        self.struct = 'points'
        if(width/len(labels) < 30) or params.get("nth"):
            temp = [""] * len(labels)
            nth = params.get("nth", int(math.ceil( 30.0/(width/len(labels)))))

            LAMBDA = lambda:0

            if type(nth) == int:
                for index in range(0,len(labels), nth ):
                    temp[index] = labels[index]
                labels = temp
            if isinstance(nth, type(LAMBDA)):
                mapped = map(nth, labels)
                labels = mapped
                params['nth'] = None

        self.x = labels
        self.y = {}
        self.params = {'datasetFill' : False, 'animation' : True, 'pointDot' : False}
        self.params.update(params)


    def set_color(self,dimension, color_scheme):
        self.y[dimension].update(color_scheme)
        return dimension

    def add_dimension(self, name ,lst, options={}):
        self.y[name] = {"values": lst, "name":name }
        self.set_color(name, colors.DEFAULT_BLUE)

        for key in options.keys():
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
                "data": self.y[dimension].get("values",[]),
                "stacked": self.y[dimension].get('stacked', 'false'),
            }
            data["datasets"].append(line)
        js_data = json.dumps(data)
        var = "var data = %s" % js_data
        chart = self.embed + "\n" + var
        chart = chart + "\n" + "var myLineChart = new Chart(ctx).%s(data, %s ); \n " % ( self.type ,str(json.dumps(self.params)))
        func = """function change(name, stacked) {\n
                var svg = document.getElementById(name);\n
                myLineChart.datasets.forEach(function (dimension, index) {\n
                    
                    if (dimension.label == name) {
                        if ('temp' in myLineChart.datasets[index] && myLineChart.datasets[index].temp.length > 0) {

                            myLineChart.datasets[index].[struct] = myLineChart.datasets[index].temp;
                            myLineChart.datasets[index].temp = [];
                            svg.style.fill=myLineChart.datasets[index].fillColor;
                            
                            if(stacked==true){
                                for (i = 0; i < index; i++) { 
                                   for (x = 0; x < myLineChart.datasets[index].[struct].length; x++) { 
                                            myLineChart.datasets[i].[struct][x].value = myLineChart.datasets[i].[struct][x].value + myLineChart.datasets[index].[struct][x].value;
                                   }
                                }
                            }

                        } else {

                            if(stacked==true){
                                for (i = 0; i < index; i++) { 
                                   for (x = 0; x < myLineChart.datasets[index].[struct].length; x++) { 
                                        myLineChart.datasets[i].[struct][x].value = myLineChart.datasets[i].[struct][x].value - myLineChart.datasets[index].[struct][x].value;
                                   }
                                }
                            }
                            myLineChart.datasets[index].temp = myLineChart.datasets[index].[struct];
                            myLineChart.datasets[index].[struct] = [];
                            svg.style.fill="white";
                        }
                        myLineChart.update();
                    }
                });

            }
            </script>\n
            <br> <h2>Legend:</h2>
            """.replace("[struct]", self.struct)
        toggle = ''
        for lin in reversed(data["datasets"]):
            toggle = toggle + """
                        <br>
                        <svg height="15" width="15" onclick="change('%s', %s)" style="cursor: pointer;">
                          <circle  id="%s" cx="7" cy="10" r="5" stroke="%s" stroke-width="1" fill="%s" />
                        </svg>
                        <font style="cursor: pointer;" onclick="change('%s',%s)">%s</font>
                    """ % ( lin['label'],lin['stacked'],lin['label'],lin['strokeColor'], lin['pointColor'] if self.type == 'Line' else lin['fillColor'] ,lin['label'],lin['stacked'],lin['label'])
        token = random.randint(1, 10000)
        chart = chart + func + toggle
        return chart.replace("myLineChart", "myLineChart%d" % token ).replace("ctx", "ctx%d" % token ).replace("canv", "canv%d" % token ).replace("myChart", "myChart%d" % token )
    def build_html(self):
        html = '<html>\n<head>\n<title>Chart</title>\n<script src= "http://www.chartjs.org/assets/Chart.js"></script> \n</head>\n<body>\n %s' % self.build_chart()
        html = html + '\n</body></html>'
        return html

        
