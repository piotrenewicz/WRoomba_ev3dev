import ev3dev.ev3 as ev3

head = ev3.MediumMotor()
eyes = ev3.UltrasonicSensor()


def setup():
    head.stop_action = 'hold'
    head.position_sp = 100


def look_there():
    return eyes.value()


def move_head_to(pos, speed=None):
    if speed is not None:
        head.speed_sp = speed
    head.position_sp = pos
    head.run_to_abs_pos()


