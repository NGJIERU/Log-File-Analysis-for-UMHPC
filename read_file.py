from log_entry import LogEntry
from datetime import datetime

class ReadFile:
    def read_log_file(self, file_path):  # Added 'self' parameter   
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


"""         with open(file_path, 'r') as file:
            log_entries = []
            lines = file.readlines()
            for line in lines:
                print(line.strip()) """

                
"""                 log_entry = self.parse_log_line(line)
                if log_entry:  # Check if log_entry is not None
                    log_entries.append(log_entry)
        return log_entries """
    
"""     def parse_log_line(self, line):
        # Assuming log lines have the format: "[timestamp] event details"
        parts = line.strip().split(' ', 1)
        if len(parts) >= 2:
            timestamp = parts[0][1:-1]  # Remove brackets from timestamp
            event_details = parts[1]
            # Assuming event_details have the format: "event: details"
            event_parts = event_details.split(': ', 1)
            if len(event_parts) >= 2:
                event = event_parts[0]
                details = event_parts[1]
                # Assuming LogEntry class has attributes timestamp, event, and details
                return LogEntry(timestamp, event, details)
        return None """