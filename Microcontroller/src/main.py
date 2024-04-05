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

bumper_b = Bumper(brain.three_wire_port.b)

# Variables
cycle = 0
cycleT = cycle
Unit = 1
t = int # Temporary variable


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

def Calibrate():
    #Calibrates motors 12, 10, and 20 to look more like the scarab walk cycle, and to be more stable.
    #It is reccomended to have a single Calibrate() at the beginning of your code.
    motor_12.spin_for(FORWARD, 90, DEGREES, wait=False)
    motor_10.spin_for(FORWARD, 90, DEGREES, wait=False)
    motor_20.spin_for(FORWARD, 90, DEGREES)
    motor_19.set_stopping(HOLD)
    motor_2.set_stopping(HOLD)
    motor_11.set_stopping(HOLD)

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
    Degrees = Degrees * 2
    if Degrees > 720:
        motor_2.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * Degrees), DEGREES, wait=False)
        motor_12.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * Degrees), DEGREES, wait=False)
        motor_11.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * Degrees), DEGREES, wait=False)
        motor_20.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
        motor_19.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
        motor_10.spin_for(FORWARD, (Degrees * Unit), DEGREES)
    else:
        motor_2.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
        motor_12.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
        motor_11.spin_for(FORWARD, ((math.fabs(360/Degrees) - 1) * -Degrees), DEGREES, wait=False)
        motor_20.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
        motor_19.spin_for(FORWARD, (Degrees * Unit), DEGREES, wait=False)
        motor_10.spin_for(FORWARD, (Degrees * Unit), DEGREES)


def press():
    global cycle, cycleT
    sleep(300)
    cycle += 1
    if cycle > 4:
        cycle = 0
    cycleT = cycle


def main():
    global cycle, cycleT, t
    Calibrate()
    bumper_b.pressed(press)
    while True:
        sleep(50)
        if cycleT == 1:
            cycleT = 0
            Forward(360)
            Turn(180)
            Forward(360)
        elif cycleT == 2:
            cycleT = 0
            Turn(360)
            Forward(20)
            Turn(360)
            Forward(20)
        elif cycleT == 3:
            cycleT = 0
            Turn(1800)
        elif cycleT == 4:
            cycleT = 0
            Forward(100)
            Turn(90)
            Forward(100)
            Turn(90)
            Forward(100)
            Turn(90)
            Forward(100)
            Turn(90)

run = Thread(main)
