import ev3dev.ev3 as ev3


def read_distance():
    sensor = ev3.UltrasonicSensor()
    print(sensor.value())


read_distance()
