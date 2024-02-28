# i want to add another function which is to calculate the number of job created and ended in this case which is 3 job created and 3 job ended but i want the function to be modular so what are the way that you can insert the code

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
    

class JobTimeRange:
    def __init__(self, allocate_timestamp, complete_timestamp):
        self.allocate_timestamp = allocate_timestamp
        self.complete_timestamp = complete_timestamp

    def calculate_time_execution(self):
        return self.complete_timestamp - self.allocate_timestamp

class ReadFile:
    def read_log_file(self, file_path):
        log_entries = []
        job_counter = JobCounter()  # Instantiate JobCounter class


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

                elif "_job_complete" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    # Find the corresponding log entry for the job ID
                    for entry in log_entries:
                        if entry.job_id == job_id and not entry.job_ended:
                            entry.mark_job_ended()  # Mark the job as ended
                            job_counter.increment_ended()  # Increment jobs ended count

                            break  # Break out of the loop once the job is marked as ended

        return log_entries
    
    def count_jobs(self, file_path):
        log_entries = []
        job_counter = JobCounter()  # Instantiate JobCounter class


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

                elif "_job_complete" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    # Find the corresponding log entry for the job ID
                    for entry in log_entries:
                        if entry.job_id == job_id and not entry.job_ended:
                            entry.mark_job_ended()  # Mark the job as ended
                            job_counter.increment_ended()  # Increment jobs ended count

                            break  # Break out of the loop once the job is marked as ended

        return job_counter

""" class ReadFile:
    def read_log_entries(self, file_path):
        log_entries = []

        with open(file_path, 'r') as file:
            for line in file:
                timestamp_str, event_str = line.strip().split("] ")
                timestamp = datetime.strptime(timestamp_str[1:], "%Y-%m-%dT%H:%M:%S.%f")
                if "sched: Allocate" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    log_entry = LogEntry(timestamp, "sched: Allocate", job_id)
                    log_entries.append(log_entry)

                elif "_job_complete" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    log_entry = LogEntry(timestamp, "_job_complete", job_id)
                    log_entries.append(log_entry)

        return log_entries

    def count_jobs(self, log_entries):
        job_counter = JobCounter()  # Instantiate JobCounter class

        for entry in log_entries:
            if entry.event == "sched: Allocate":
                job_counter.increment_created()  # Increment jobs created count
            elif (entry.event == "_job_complete" and entry.job_ended):
                entry.mark_job_ended()  # Mark the job as ended
                job_counter.increment_ended()  # Increment jobs ended count

        return job_counter """


if __name__ == "__main__":
    file_reader = ReadFile()
    file_path = "./all tester/tester/logtester.txt"
    log_entries = file_reader.read_log_file(file_path)
    job_counter = file_reader.count_jobs(file_path)


    # Filter log entries to get allocate and complete timestamps for each job
    job_ranges = {}
    for entry in log_entries:
        if entry.event == "sched: Allocate":
            job_id = entry.job_id
            allocate_timestamp = entry.timestamp
        elif entry.event == "_job_complete":
            complete_timestamp = entry.timestamp
            if job_id in job_ranges:
                job_ranges[job_id].append(JobTimeRange(allocate_timestamp, complete_timestamp))
            else:
                job_ranges[job_id] = [JobTimeRange(allocate_timestamp, complete_timestamp)]

    # Get the number of jobs created and ended
    jobs_created, jobs_ended = job_counter.get_counts()
    print(f"Number of jobs created: {jobs_created}")
    print(f"Number of jobs ended: {jobs_ended}")  

    # Calculate time execution for each job
    for job_id, time_ranges in job_ranges.items():
        for idx, time_range in enumerate(time_ranges):
            time_execution = time_range.calculate_time_execution()
            print(f"JobID: {job_id}, Time Execution {idx+1}: {time_execution}")

      


""" if __name__ == "__main__":
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
 """