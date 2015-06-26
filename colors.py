import struct

def construct_color(val, opacity):
	if "#" in val:
		val = struct.unpack('BBB',val.decode('hex'))
	val = val + (opacity,)
	return "rgba" + str(val) 