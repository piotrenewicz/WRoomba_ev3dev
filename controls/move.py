import ev3dev.ev3 as ev3


def move_head(pos, speed= 100):
    motor = ev3.MediumMotor()
    motor.speed_sp = speed
    motor.position_sp = pos
    motor.run_to_abs_pos()


