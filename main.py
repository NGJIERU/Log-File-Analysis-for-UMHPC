from read_file import ReadFile
from log_entry import LogEntry
from job_time_range import JobTimeRange
from datetime import datetime
from job_counter import JobCounter

if __name__ == "__main__": # This line checks whether the script is being run as the main program (i.e., not imported as a module into another script).
    file_reader = ReadFile()
    file_path = "./data/logtester.txt"  
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

""" 
    # Get the number of jobs created and ended
    jobs_created, jobs_ended = job_counter.get_counts()
    print(f"Number of jobs created: {jobs_created}")
    print(f"Number of jobs ended: {jobs_ended}") """
