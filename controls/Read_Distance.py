import ev3dev.ev3 as ev3


def read_distance():
    sensor = ev3.UltrasonicSensor()
    return sensor.value()
