import ev3dev.ev3 as ev3


def move_head():
    motor = ev3.MediumMotor()
    print(motor.position_sp)

move_head()