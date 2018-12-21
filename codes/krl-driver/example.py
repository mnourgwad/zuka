#! py -2
from krldriver import *

def take():
	PTP(POS,"","",-857)
	GRIPPER_CLOSE()
	PTP(POS,"","",-757)

def drop():
	PTP(POS,"","",-857)
	GRIPPER_OPEN()
	PTP(POS,"","",-757)

def p(n):
	if n == 1: PTP(POS,-80,-125,-757)
	if n == 2: PTP(POS,-80,50,-757)
	if n == 3: PTP(POS,90,50,-757)
	if n == 4: PTP(POS,90,-125,-757)

distenation = 1
source = 4

VEL_CP(3)
VEL_PTP(100)
OV_PRO(10)
APO(0)
#Home 
#BASE(525,0,890,0,0,0)
#TOOL(0,0,0,0,-90,0) 

#Home Pal
#BASE(450,0,800,0,0,0)
#TOOL(0,0,0,0,-180,0) 

#Chess board 
BASE(450,0,80,0,0,0)
TOOL(0,0,200,0,-180,0) 

#BASE(BASE_DATA=6)
#TOOL(TOOL_DATA=5)

LIN(0,0,0,0,0,0)
#PAL_MODE(TRUE)
'''
while 1:
	p(source)
	take()
	p(distenation)
	drop()
	distenation -=1
	source -=1
	if distenation == 0: distenation = 4
	if source == 0: source = 4
'''
"""
EXAMPLES

Setup Functions
	TOOL(0,0,0,0,0,0)  					# or  	TOOL(TOOL_DATA=3)
	BASE(525,0,890,0,0,0)  	 			# or	BASE(BASE_DATA=30)
	APO(1.5)							# Approximation value of 1.5mm for C_PTP and C_DIS values
	VEL_CP(.15)							# Sets CP motions' velocity (LIN and CIRC) to .15m/s
 	VEL_PTP(30)							# Sets axis velocities at PTP motion to 30% of the maximum allowable velocity
	OV_PRO(50)							# Sets the overall program velocities (VEL_CP and VEL_PTP) to 50% of their values

Motion Functions
	PTP(AXIS,0,-90,90,80,70,60)			# or  	PTP(POS,0,0,60,0,0,0)	
	PTP_REL(POS,"","",20)    			# Unchanged values of X, Y, A, B, and C
	LIN(0,10)
	LIN_REL("",10)
	CIRC("",10,"","","","",-5,5)		# If you're at the (0,0,0) point, this line will draw half a circle [or letter C]
Other
	OUT(1,TRUE) 						# Sets output port 1 to TRUE signal 
	WAIT(.2)							# Wait for 200ms

Auxilliary Functions [Not an original part of KRL]
	PTP_HOME() 							# Robot's home position
	GRIPPER_OPEN()						# Does the required instruction to operate a gripper actuated by port 1 and 4 
	GRIPPER_CLOSE()
	INI()								# Sets 	VEL_CP = 3m/s
    VEL_PTP = 100%
	OV_PRO = 10%
	APO o= 0
	TOOL = (0,0,0,0,0,0)
	BASE = (525,0,890,0,0,0)  [The same position for home of KR6 r900 sixx]
  and goes to the PTP(POS,0,0,0,0,0,0) of the Base to initialize the $POS_ACT variable to be 
  able to use PTP_REL and LIN_REL motions.

  It's recommended to use this function at the beginning.
  You can change the values of the speeds and approximation by 
  passing parameters to this function
  INI(VEL_CP, VEL_PTP, OV_PRO, APO)	
    """
