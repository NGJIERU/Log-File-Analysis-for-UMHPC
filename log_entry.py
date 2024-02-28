class LogEntry:
    def __init__(self, timestamp, event, job_id):
        self.timestamp = timestamp
        self.event = event
        self.job_id = job_id
        self.job_ended = False  # Initially set to False

    def mark_job_ended(self):
        self.job_ended = True