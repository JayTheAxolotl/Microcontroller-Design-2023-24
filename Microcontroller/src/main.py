#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_10 = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False)
motor_19 = Motor(Ports.PORT19, GearSetting.RATIO_36_1, False)
motor_20 = Motor(Ports.PORT20, GearSetting.RATIO_36_1, False)
motor_11 = Motor(Ports.PORT11, GearSetting.RATIO_36_1, True)
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_36_1, True)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_36_1, True)

bumper_a = Bumper(brain.three_wire_port.a)


# wait for rotation sensor to fully initialize
wait(30, MSEC)

def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
Unit = 1

def Calibrate():
    #Calibrates motors 12, 10, and 20 to look more like the scarab walk cycle, and to be more stable.
    #It is reccomended to have a single Calibrate() at the beginning of your code.
    motor_12.spin_for(FORWARD, 90, DEGREES, wait=False)
    motor_10.spin_for(FORWARD, 90, DEGREES, wait=False)
    motor_20.spin_for(FORWARD, 90, DEGREES)

def Forward(Degrees):
    #in general 360 degrees moves the bot about 86cm/34in
    motor_2.spin_for(FORWARD, Degrees, DEGREES, wait=False)
    motor_19.spin_for(FORWARD, Degrees, DEGREES, wait=False)
    motor_11.spin_for(FORWARD, Degrees, DEGREES, wait=False)
    motor_20.spin_for(FORWARD, Degrees, DEGREES, wait=False)
    motor_12.spin_for(FORWARD, Degrees, DEGREES, wait=False)
    motor_10.spin_for(FORWARD, Degrees, DEGREES)

def Turn(Degrees):
    # The reason for the (math.fabs(360/Degrees) - 1) * -Degrees formula is so that the motors are in the right position
    # The amount the bot spins is not exact to the degrees inputted, also to turn left use a negative input
    motor_2.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
    motor_12.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
    motor_11.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
    motor_20.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
    motor_19.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
    motor_10.spin_for(FORWARD, (Degrees * Unit), DEGREES)

def when_started1():
    #Calibrate()
    if bumper_a.pressing() == 1:
        #Forward(100)
        brain.screen.print("worked")
    else:
        pass

when_started1()
