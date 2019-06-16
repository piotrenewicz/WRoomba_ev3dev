import ev3dev.ev3 as ev3

head = ev3.MediumMotor()
eyes = ev3.UltrasonicSensor()


def setup():
    head.stop_action = 'hold'
    head.speed_sp = 100


def look_there():
    return eyes.value()


def move_head_to(pos, speed=None):
    if speed is not None:
        head.speed_sp = speed
    head.position_sp = pos
    head.run_to_abs_pos()


def blocking_move_head_to(pos, speed=None):
    move_head_to(pos, speed)
    while head.position != pos:
        if head.state == 'stalled':
            break


setup()


class Awareness(object):
    def __enter__(self):
        self.prev_heading = head.position
        self.active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        move_head_to(self.prev_heading)
        self.active = False

    def __iter__(self):
        if not self.active:
            self.__enter__()
            self.close = True
        else:
            self.close = False

        self.world.clear()
        self.heading = 0
        blocking_move_head_to(self.heading)
        return self

    world = dict()

    def __next__(self):
        self.heading += 1
        if self.heading == 300:
            self.heading = -90
            blocking_move_head_to(self.heading)
        if self.heading == 0:
            raise StopIteration
        move_head_to(self.heading)
        self.world[self.heading] = look_there()
        return self.heading


