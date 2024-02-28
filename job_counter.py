class JobCounter:
    def __init__(self):
        self.jobs_created = 0
        self.jobs_ended = 0

    def increment_created(self):
        self.jobs_created += 1

    def increment_ended(self):
        self.jobs_ended += 1

    def get_counts(self):
        return self.jobs_created, self.jobs_ended