from read_file import ReadFile
from log_entry import LogEntry
from job_time_range import JobTimeRange
from datetime import datetime

if __name__ == "__main__": # This line checks whether the script is being run as the main program (i.e., not imported as a module into another script).
    file_reader = ReadFile()
    file_path = "./data/logtester.txt"  
    log_entries = file_reader.read_log_file(file_path)

    # Filter log entries to get allocate and complete timestamps for each job
    job_ranges = {}
    for entry in log_entries:
        if entry.event.startswith("sched: Allocate"):
            job_id = entry.job_id
            allocate_timestamp = entry.timestamp
        elif entry.event.startswith("_job_complete"):
            complete_timestamp = entry.timestamp
            if job_id in job_ranges:
                job_ranges[job_id].append(JobTimeRange(allocate_timestamp, complete_timestamp))
            else:
                job_ranges[job_id] = [JobTimeRange(allocate_timestamp, complete_timestamp)]

    # Calculate time ranges for each job
    for job_id, time_ranges in job_ranges.items():
        for idx, time_range in enumerate(time_ranges):
            range_duration = time_range.calculate_time_range()
            print(f"JobID: {job_id}, Time Range {idx+1}: {range_duration}")
