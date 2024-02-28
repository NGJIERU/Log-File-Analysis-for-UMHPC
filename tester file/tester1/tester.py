""" 
[2022-06-01T15:31:27.874] _slurm_rpc_kill_job: REQUEST_KILL_JOB JobId=42804 uid 548300563
[2022-06-01T15:31:27.874] error: Security violation, REQUEST_KILL_JOB RPC for JobId=42804 from uid 548300563
[2022-06-01T15:31:27.874] _slurm_rpc_kill_job: job_str_signal() uid=548300563 JobId=42804 sig=9 returned: Access/permission denied


above data is what in the text file
so first use if statement to detect whether the line has the word _slurm_rpc_kill_job
then record userid and jobid getting tried to be killed with its timestamp 
then print the output in formatted way below:
userid | jobid | date | time
so there are two cases here
first even there is _slurm_rpc_kill_job keyword there are two different statement 
second check whether there is duplicate userid for the same jobid if so there is no need to print the same userid
 """

processed_job_users = set()

print("uid | jobid | date | time ")

with open('./data/logtester.txt', 'r') as log_file:
    for line in log_file:
        if '_slurm_rpc_kill_job' in line:
            user_id_start = line.find('uid') + len('uid ')
            user_id = line[user_id_start:].split()[0]
            job_id_start = line.find('JobId=') + len('JobId=')
            job_id = line[job_id_start:].split()[0]
            if (user_id, job_id) not in processed_job_users:
                timestamp = line[:23]
                processed_job_users.add((user_id, job_id))
                print(f"{user_id} | {job_id} | {timestamp[1:11]} | {timestamp[12:]}")
