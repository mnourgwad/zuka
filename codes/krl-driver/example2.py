#! py -2

from krldriver import *

VEL_CP(3)
VEL_PTP(100)
OV_PRO(50)
APO(0)
BASE(525,0,890,0,0,0)
TOOL(0,0,0,0,-90,0) 
PAL_MODE(TRUE)


while (1):
	OV_PRO(30)
	PTP(AXIS,0,-90,90,0,0,0)
	PTP(AXIS,90,-90,90,0,0,0)
	OV_PRO(50)
	PTP(AXIS,-90,-90,90,0,0,0)
	PTP(AXIS,0,-90,90,0,0,0)