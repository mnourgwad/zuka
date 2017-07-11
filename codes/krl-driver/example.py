from krldriver import *

INI(3,100,10,0)
APO(30)
OV_PRO(30)
while 1:
	# The robot will go from left to write infinitly with 30% of its maximum speed, and 30mm of approximation.
	PTP(AXIS,-169)
	PTP(AXIS,169)



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
		PAL_MODE(TRUE)						# Activates the pallitizing mode, where A4 and A5 don't rotate.

	Auxilliary Functions [Not an original part of KRL]
		PTP_HOME() 							# Robot's home position
		GRIPPER_OPEN()						# Does the required instruction to operate a gripper actuated by port 1 and 4 
		GRIPPER_CLOSE()
		INI()								# Sets 	VEL_CP = 3m/s
													VEL_PTP = 100%
													OV_PRO = 10%
													APO = 0
													TOOL = (0,0,0,0,0,0)
													BASE = (525,0,890,0,0,0)  [The same position for home of KR6 r900 sixx]
											  and goes to the PTP(POS,0,0,0,0,0,0) of the Base to initialize the $POS_ACT variable to be 
											  able to use PTP_REL and LIN_REL motions.

											  It's recommended to use this function at the beginning.
											  You can change the values of the speeds and approximation by passing parameters to this function
											  INI(VEL_CP, VEL_PTP, OV_PRO, APO)

"""
