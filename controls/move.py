import ev3dev.ev3 as ev3


def move_head(pos):
    motor = ev3.MediumMotor()

    # print(motor.position)
    print(motor.speed)
    motor.position_sp = pos
    motor.run_to_abs_pos()


move_head(100)
