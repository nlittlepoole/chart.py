# Charts.py

Chart py is a python charting library based on the open source Chart.js


> Charts.py exists to make inserting charts into python projects as simple as possible.
> The syntax for this wrapper is constructed to be as simple to use as possible. 

Check out the [Demo] ipython notebook!

### Version
0.1.01

### Tech

* [Charts.js] - HTML enhanced for web apps!


### Installation

```sh
$ git clone https://github.com/nlittlepoole/chart.py.git
$ cd charts.py
$ sudo python setup.py install
```

### Usage

```python
from chartspy import *
from chartspy.colors import *
import datetime
import random


numdays = 15
base = datetime.datetime.today()
date_list = [(base - datetime.timedelta(days=x)).strftime("%B %d, %Y") for x in range(0, numdays)]

a = random.sample(xrange(100), numdays)
b = random.sample(xrange(100), numdays)

x = LineChart(date_list)
x.add_dimension("Line 1",a, options=DEFAULT_GREEN)
x.add_dimension("Line 2",b)
x.set_color("Line 2", DEFAULT_RED )
print x.build_chart()
print x.build_html()


```
### Plugins/Extensions/Frameworks

Currently known support for:

* iPython (adding native support)
* Django
* Flask



### Development

Want to contribute? Great!
Feel free to make PRs!

### Todo's

* Write More Tests
* Auto Chart Generator

License
----

MIT


**Free Software, Hell Yeah!**

[Charts.js]:http://www.chartjs.org/
[Demo]: http://nbviewer.ipython.org/github/nlittlepoole/chart.py/blob/master/chartspy/demo.ipynb
