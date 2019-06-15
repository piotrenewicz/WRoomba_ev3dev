import ev3dev.ev3 as ev3


def move_head(pos):
    motor = ev3.MediumMotor()
    print(motor.position)
    # 
    # motor.position_sp = pos
    # motor.run_to_abs_pos()

move_head(100)