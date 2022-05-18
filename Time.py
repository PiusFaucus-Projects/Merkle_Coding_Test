class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalise()

    def normalise(self):
        if self.hours > 23:
            self.hours = 0

        while self.minutes > 59:
            self.hours += 1
            self.minutes -= 60

        while self.seconds > 59:
            self.minutes += 1
            self.seconds -= 60

    def scale(self, seconds):
        self.seconds += seconds
        self.normalise()

    def timeString(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)


if __name__ == "__main__":
    t = Time(1, 30, 20)
    print(t.timeString())
    t.scale(400)
    print(t.timeString())