from read_file import ReadFile
from job_time_range import JobTimeRange
from datetime import datetime

class LogEntry:
    def __init__(self, timestamp, event, job_id):
        self.timestamp = timestamp
        self.event = event
        self.job_id = job_id
        self.job_ended = False  # Initially set to False

    def mark_job_ended(self):
        self.job_ended = True

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

class ReadFile:
    def read_log_file(self, file_path):
        log_entries = []
        job_counter = JobCounter()  # Instantiate JobCounter class
        job_ranges = {}  # Initialize job_ranges dictionary

        with open(file_path, 'r') as file:
            for line in file:
                timestamp_str, event_str = line.strip().split("] ")
                timestamp = datetime.strptime(timestamp_str[1:], "%Y-%m-%dT%H:%M:%S.%f")
                if "sched: Allocate" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    log_entry = LogEntry(timestamp, "sched: Allocate", job_id)
                    log_entries.append(log_entry)
                    job_counter.increment_created()  # Increment jobs created count
                    # Add job_id to job_ranges with an empty list
                    job_ranges[job_id] = []
                elif "_job_complete" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    # Find the corresponding log entry for the job ID
                    for entry in log_entries:
                        if entry.job_id == job_id and not entry.job_ended:
                            entry.mark_job_ended()  # Mark the job as ended
                            job_counter.increment_ended()  # Increment jobs ended count
                            job_ranges[job_id].append(timestamp)  # Record completion timestamp
                            break  # Break out of the loop once the job is marked as ended

        return log_entries, job_counter, job_ranges

if __name__ == "__main__":
    file_reader = ReadFile()
    file_path = "./data/logtester.txt"
    log_entries, job_counter, job_ranges = file_reader.read_log_file(file_path)

    # Calculate time execution for each job
    for job_id, timestamps in job_ranges.items():
        if len(timestamps) == 2:
            start_time, end_time = timestamps
            time_execution = end_time - start_time
            print(f"JobID: {job_id}, Time Execution: {time_execution}")

    # Get the number of jobs created and ended
    jobs_created, jobs_ended = job_counter.get_counts()
    print(f"Number of jobs created: {jobs_created}")
    print(f"Number of jobs ended: {jobs_ended}")
