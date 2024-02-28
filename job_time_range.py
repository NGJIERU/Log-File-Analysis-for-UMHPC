from datetime import datetime

class JobTimeRange:
    def __init__(self, allocate_timestamp, complete_timestamp):
        self.allocate_timestamp = allocate_timestamp
        self.complete_timestamp = complete_timestamp

    def calculate_time_execution(self):
        return self.complete_timestamp - self.allocate_timestamp
