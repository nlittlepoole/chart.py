import struct

def construct_color(val, opacity):
	if "rgba" in val:
		return val
	if "#" in val:
		val = struct.unpack('BBB',val.decode('hex'))
	val = val + (opacity,)
	return "rgba" + str(val) 

DEFAULT_BLUE = { 
                "fill_color" : "rgba(151,187,205,0.2)",
                "stroke_color" : "rgba(151,187,205,1)",
                "point_color" : "rgba(151,187,205,1)",
                "point_stroke_color" :"#fff",
                "point_highlight_fill_color" : "#fff",
                "point_highlight_stroke_color" :"rgba(151,187,205,1)",
            }
DEFAULT_GREEN = { 
                "fill_color" : "rgba(0,255,0,0.2)",
                "stroke_color" : "rgba(39, 174, 96,.4)",
                "point_color" : "rgba(39, 174, 96,1)",
                "point_stroke_color" :"#fff",
                "point_highlight_fill_color" : "#fff",
                "point_highlight_stroke_color" :"rgba(39, 174, 96,1)",
            }
DEFAULT_RED = { 
                "fill_color" : "rgba(255,0,0,0.2)",
                "stroke_color" : "rgba(192, 57, 43,.4)",
                "point_color" : "rgba(192, 57, 43,1)",
                "point_stroke_color" :"#fff",
                "point_highlight_fill_color" : "#fff",
                "point_highlight_stroke_color" :"rgba(192, 57, 43,1)",
            }