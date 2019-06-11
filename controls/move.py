import ev3dev.ev3 as ev3


def move_head(pos):
    motor = ev3.LargeMotor()
    motor.position_sp = 0
    motor.run_to_abs_pos(pos)

move_head(10)