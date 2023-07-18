import datetime

class Availability:
    def __init__(self, timestamp: datetime.datetime, freeSlots: int, usedSlots: int):
        self.timestamp = timestamp
        self.freeSlots = freeSlots
        self.usedSlots = usedSlots