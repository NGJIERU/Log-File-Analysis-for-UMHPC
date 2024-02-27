from datetime import datetime

class JobTimeRange:
    def __init__(self, allocate_timestamp, complete_timestamp):
        self.allocate_timestamp = allocate_timestamp
        self.complete_timestamp = complete_timestamp

    def calculate_time_range(self):
        allocate_time = datetime.strptime(self.allocate_timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        complete_time = datetime.strptime(self.complete_timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        return complete_time - allocate_time
