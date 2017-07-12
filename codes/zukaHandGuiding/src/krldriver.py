from kukavarproxy import *

axes_limits = [ [-170,170],[-190,45],[-120,156],[-185,185],[-120,120],[-350,350]]
#robot = KUKA('172.31.1.147')
AXIS = 'a'
POS = 'p'
FALSE = 0
TRUE = 1

def INI(VEL_CP_VAL=3, VEL_AXIS_VAL=100, OV_PRO_VAL=10 ,APO_VAL=0):
	VEL_CP(VEL_CP_VAL)
	VEL_PTP(VEL_AXIS_VAL)
	OV_PRO(OV_PRO_VAL)
	APO(APO_VAL)
	BASE(525,0,890,0,0,0)
	TOOL(0,0,0,0,-90,0) 
	PTP(POS,0,0,0,0,0,0)

def PTP_HOME():
	PTP(AXIS,0,-90,90,0,0,0)

def GRIPPER_OPEN():
	OUT(1,TRUE)
	OUT(1,FALSE)
	OUT(4,TRUE)
	OUT(4,FALSE)

def GRIPPER_CLOSE():
	OUT(4,TRUE)
	OUT(4,FALSE)
	OUT(1,TRUE)
	OUT(1,FALSE)

def OUT(ioPort, Signal):
	while (int (robot.read("KRLD_COM"))): continue
	robot.write("KRLD_IO",ioPort)
	if Signal == True: robot.write("KRLD_SIGNAL","TRUE")
	else: robot.write("KRLD_SIGNAL","FALSE")
	robot.write("KRLD_COM",14)

def PAL_MODE(Signal):
	while (int (robot.read("KRLD_COM"))): continue
	if Signal == True: robot.write("KRLD_SIGNAL","TRUE")
	else: robot.write("KRLD_SIGNAL","FALSE")
	robot.write("KRLD_COM",15)

def PTP(interpolation, v1="",v2="",v3="",v4="",v5="",v6=""):
	if v1 == v2 == v3 == v4 == v5 == v6 == "": 
		raise error(2)
		return 0
	if interpolation == AXIS: 
		axes = [v1,v2,v3,v4,v5,v5]
		for index,axis in enumerate(axes):
			pass
			#if float(axis) <= axes_limits[index][0] or float(axis) >= axes_limits[index][1]: raise error(1,(index+1))
		while (int (robot.read("KRLD_COM"))): continue
		destination = format_axis(v1,v2,v3,v4,v5,v6)
		robot.write("KRLD_AXIS", destination)
		robot.write("KRLD_COM",1)
	elif interpolation == POS:
		while (int (robot.read("KRLD_COM"))): continue
		destination = format_pos(v1,v2,v3,v4,v5,v6)
		robot.write("KRLD_POS",destination)
		robot.write("KRLD_COM",2)
	else:
		raise error(3)

def PTP_REL(interpolation, v1="",v2="",v3="",v4="",v5="",v6=""):
	if v1 == v2 == v3 == v4 == v5 == v6 == "": 
		raise error(2)
		return 0
	if interpolation == AXIS: 
		while (int (robot.read("KRLD_COM"))): continue
		destination = format_axis(v1,v2,v3,v4,v5,v6)
		robot.write("KRLD_AXIS", destination)
		robot.write("KRLD_COM",5)
	elif interpolation == POS:
		while (int (robot.read("KRLD_COM"))): continue
		destination = format_pos(v1,v2,v3,v4,v5,v6)
		robot.write("KRLD_POS",destination)
		robot.write("KRLD_COM",6)
	else:
		raise error(3)

def LIN (x="",y="",z="",a="",b="",c=""):
	if x == y == z == a == b == c == "": raise error(3)
	while (int (robot.read("KRLD_COM"))): continue
	destination = format_pos(x,y,z,a,b,c)
	robot.write("KRLD_POS",destination)
	robot.write("KRLD_COM",3)

def LIN_REL (x="",y="",z="",a="",b="",c=""):
	if x == y == z == a == b == c == "": raise error(3)
	while (int (robot.read("KRLD_COM"))): continue
	destination = format_pos(x,y,z,a,b,c)
	robot.write("KRLD_POS",destination)
	robot.write("KRLD_COM",7)

def CIRC (x="",y="",z="",a="",b="",c="",xAux="",yAux="",zAux="",aAux="",bAux="",cAux=""):
	if x == y == z == a == b == c == "": raise error(3)
	if xAux == yAux == zAux == aAux == bAux == cAux == "": raise error(5)
	while (int (robot.read("KRLD_COM"))): continue
	destination = format_pos(x,y,z,a,b,c)
	robot.write("KRLD_POS",destination)
	auxilliary = format_pos(xAux,yAux,zAux,aAux,bAux,cAux)
	robot.write("KRLD_POS",auxilliary)
	robot.write("KRLD_COM",4)

def WAIT(time_sec):
	while (int (robot.read("KRLD_COM"))): continue
	robot.write("KRLD_SLEEP", abs(time_sec))
	robot.write("KRLD_COM",8)

def BASE(x=0,y=0,z=0,a=0,b=0,c=0,offX=0,offY=0,offZ=0,offA=0,offB=0,offC=0,BASE_DATA=-1):
	while (int (robot.read("KRLD_COM"))): continue
	if BASE_DATA > 0: 
		base_frame = "BASE_DATA["  + str(BASE_DATA) + "]"
		robot.write("KRLD_BASE", robot.read(base_frame))	
	else:
		if x == y == z == a == b == c == "": raise error(3)
		base_frame = format_pos(x,y,z,a,b,c)
		robot.write("KRLD_BASE", base_frame)
	offset_data = format_pos(offX,offY,offZ,offA,offB,offC)
	robot.write("KRLD_BASE_OFFSET", offset_data)
	robot.write("KRLD_COM",9)

def TOOL(x=0,y=0,z=0,a=0,b=0,c=0,TOOL_DATA=-1):
	while (int (robot.read("KRLD_COM"))): continue
	if TOOL_DATA > 0: 
		tool_frame = "TOOL_DATA["  + str(TOOL_DATA) + "]" 
		robot.write("KRLD_TOOL", robot.read(tool_frame))
	else:
		if x == y == z == a == b == c == "": raise error(3)
		tool_frame = format_pos(x,y,z,a,b,c)
		robot.write("KRLD_TOOL", tool_frame)
	robot.write("KRLD_COM",10)

def APO(approximation_value):
	while (int (robot.read("KRLD_COM"))): continue
	robot.write("KRLD_APO", approximation_value )
	robot.write("KRLD_COM",11)

def VEL_CP(velocity_value):
	while (int (robot.read("KRLD_COM"))): continue
	robot.write("KRLD_VEL_CP", velocity_value)
	robot.write("KRLD_COM",12)

def VEL_PTP(velocity_value):
	while (int (robot.read("KRLD_COM"))): continue
	robot.write("KRLD_VEL_PTP", velocity_value)
	robot.write("KRLD_COM",13)

def OV_PRO(percentage):
	while (int (robot.read("KRLD_COM"))): continue
	if percentage < 0 or percentage > 100: raise error(4)
	robot.write("$OV_PRO", percentage)
	

def format_axis(A1, A2, A3, A4, A5, A6):
	axes = [A1,A2,A3,A4,A5,A6]
	axes_names = ["A1","A2","A3","A4","A5","A6"]
	instruction = " "
	for index,axis in enumerate(axes):
		if axis != "":
			if instruction[len(instruction)-1] != " ":	instruction += ", "
			instruction += axes_names[index] + " " + str(axis)
	return "{" + instruction + "}"

def format_pos(x, y, z, a, b, c):
	coordinates = [x,y,z,a,b,c]
	coordinates_names = ["X","Y","Z","A","B","C"]
	instruction = " "
	for index,coordinate in enumerate(coordinates):
		if coordinate != "":
			if instruction[len(instruction)-1] != " ":	instruction += ", "
			instruction += coordinates_names[index] + " " + str(coordinate)
	return "{" + instruction + "}"

def error(index, axis=9):
	if index == 1: print("A" + str(axis)+ " limits violated.")
	if index == 2: print("One parameter- at least- should be defined for motion.")
	if index == 3: print("Interpolation type is wrongly defined.")
	if index == 4: print("$OV_PRO values should be percentage.")
	if index == 5: print("Incorrect base number.")
	if index == 6: print("One auxilliary coordinate- at least- should be defined for CIRC motion.")
	raise SystemExit
