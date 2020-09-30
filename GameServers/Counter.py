
class Counter:
    def __init__(self, max_count):
        self.max_count = max_count;
        self.count = 0;
        self.can_be_destroyed = False;

    def tick(self):
        if self.count >= self.max_count:
            self.can_be_destroyed = True;
            return;
        self.count += 1;

    def signal(self):
        self.count = 0;
        self.can_be_destroyed = False;