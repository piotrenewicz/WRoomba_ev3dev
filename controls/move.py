import ev3dev.ev3 as ev3


def move_head(pos):
    motor = ev3.ServoMotor()
    motor.position_sp = pos

move_head(10)