""" 
[2022-10-17T14:32:36.120] _slurm_rpc_submit_batch_job: JobId=50922 InitPrio=829 usec=543
[2022-10-17T14:32:36.618] sched: Allocate JobId=50922 NodeList=gpu02 #CPUs=6 Partition=gpu-titan
[2022-10-20T20:05:30.345] _job_complete: JobId=50922 WEXITSTATUS 0
[2022-10-20T20:05:30.345] _job_complete: JobId=50922 done

you read the file 
above data is what in the text file
so first use if statement to detect whether the line has the word sched: Allocate
then record jobid with its timestamp of allocate
if statement detect whether the line has the word _job_complete 
then record jobid with its timestamp of complete 
but whenever record timestamp of complete at the same time check if the jobid has its own timestamp of allocate before if so then i have a function that needs to calculate the time execution 
for the time execution i need you to create a class just for calculation of time execution use timestamp of complete minus timestamp of complete 
pls write all the code in python 
"""
from datetime import datetime

class LogEntry:
    def __init__(self, timestamp, event, job_id):
        self.timestamp = timestamp
        self.event = event
        self.job_id = job_id

class JobTimeRange:
    def __init__(self, allocate_timestamp, complete_timestamp):
        self.allocate_timestamp = allocate_timestamp
        self.complete_timestamp = complete_timestamp

    def calculate_time_execution(self):
        return self.complete_timestamp - self.allocate_timestamp

class ReadFile:
    def read_log_file(self, file_path):
        log_entries = []
        with open(file_path, 'r') as file:
            for line in file:
                timestamp_str, event_str = line.strip().split("] ")
                timestamp = datetime.strptime(timestamp_str[1:], "%Y-%m-%dT%H:%M:%S.%f")
                if "sched: Allocate" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    log_entries.append(LogEntry(timestamp, "sched: Allocate", job_id))
                elif "_job_complete" in event_str:
                    job_id = event_str.split("JobId=")[1].split()[0]
                    log_entries.append(LogEntry(timestamp, "_job_complete", job_id))
        return log_entries

if __name__ == "__main__":
    file_reader = ReadFile()
    file_path = "./all tester/tester/logtester.txt"
    log_entries = file_reader.read_log_file(file_path)

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

    # Calculate time execution for each job
    for job_id, time_ranges in job_ranges.items():
        for idx, time_range in enumerate(time_ranges):
            time_execution = time_range.calculate_time_execution()
            print(f"JobID: {job_id}, Time Execution {idx+1}: {time_execution}")
