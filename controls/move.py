import ev3dev.ev3 as ev3
motor = ev3.MediumMotor()
motor.stop_action = 'hold'

def move_head(pos, speed= 100):
    motor.speed_sp = speed
    motor.position_sp = pos
    motor.run_to_abs_pos()


