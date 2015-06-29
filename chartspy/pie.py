import settings
import colors
import json
import math
import random

class PieChart():
    
    def __init__(self, data, width=450, height=450, params={}):
        self.embed = '<canvas id="myChart" width="%s" height="%s"></canvas><script>var canv= document.getElementById("myChart"); \n var ctx = canv.getContext("2d");' %( str(width), str(height) ) 
        self.type = 'Pie'
        self.struct = 'points'

        self.data = []
        self.params = {'animateScale' : True, }
        self.params.update(params)
        self.add_data(data)

    def add_data(self,lst, options={}):
        """
        Takes in a list of dicts with name and value keys
        """
        cols = [colors.DEFAULT_BLUE, colors.DEFAULT_GREEN, colors.DEFAULT_RED]
        i = 0
        for val in lst:
            if not val.get('color') or not val.get('highlight'):
                col = cols[ i % len(cols) ]
                i = i + 1
                val["color"] = col['point_color']
                val["highlight"] = col['stroke_color'] 
            self.data.append(val)

    def build_chart(self):

        js_data = json.dumps(self.data)
        var = "var data = %s" % js_data
        chart = self.embed + "\n" + var
        chart = chart + "\n" + "var myLineChart = new Chart(ctx).%s(data, %s ); \n " % ( self.type ,str(json.dumps(self.params)))
        func = """function change(name, pos) {\n
                    var svg = document.getElementById(name);\n
                    if( myLineChart.segments[pos].value != 0){
                                myLineChart.segments[pos].value=0;
                                svg.style.fill="white";
                    }
                    else{ 
                        myLineChart.segments[pos].value=data[pos].value;
                        svg.style.fill=data[pos].color;
                    }
                    myLineChart.update()
                }

            canv.onclick = function(evt){
                var tag  = myLineChart.getSegmentsAtEvent(evt)[0].label;
                for (i = 0; i < myLineChart.segments.length; i++) { 
                    if(tag == myLineChart.segments[i].label){
                        change(tag, i);
                    }
                }
            }
            </script>\n
            <br> <h2>Legend:</h2>
            """.replace("[struct]", self.struct)
        toggle = ''
        i = 0
        for lin in self.data:
            toggle = toggle + """
                        <br>
                        <svg height="15" width="15" onclick="change('%s', %d)" style="cursor: pointer;">
                          <circle  id="%s" cx="7" cy="10" r="5" stroke="%s" stroke-width="1" fill=" %s " />
                        </svg>
                        <font style="cursor: pointer;" onclick="change('%s',%d)">%s</font>
                    """ % ( lin['label'],i,lin['label'],lin['highlight'], lin['color'] ,lin['label'], i,lin['label'])
            i = i +1
        chart = chart + func + toggle
        token = random.randint(1, 10000)
        return chart.replace("myLineChart", "myLineChart%d" % token ).replace("ctx", "ctx%d" % token ).replace("canv", "canv%d" % token ).replace("myChart", "myChart%d" % token )
    def build_html(self):
        html = '<html>\n<head>\n<title>Chart</title>\n<script src= "http://www.chartjs.org/assets/Chart.js"></script> \n</head>\n<body>\n %s' % self.build_chart()
        html = html + '\n</body></html>'
        return html
class DoughnutChart(PieChart):
    def __init__(self, data, width=450, height=450, params={}):
        PieChart.__init__(self,data,width,height,params)
        self.type = 'Doughnut'
        
