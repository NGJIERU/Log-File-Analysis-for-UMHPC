""" 
[2022-06-01T15:12:23.290] error: This association 187(account='free', user='lobbeytan', partition='(null)') does not have access to qos long
[2022-06-01T15:12:23.291] _slurm_rpc_submit_batch_job: Invalid qos specification

so first use if statement to detect whether the line has the word error
then record the user with its timestamp 
if statement detect whether the line has the word _job_complete 
i want the total number of error appears at the output even there is duplicate of same user 
 """
user_data = {}
total_errors = 0

with open('./data/logtester.txt', 'r') as log_file:
    for line in log_file:
        if 'error' in line:
            user_index = line.find('user=') + len('user=')
            user = line[user_index:].split(',')[0].strip("'")
            timestamp = line[:23]
            if user in user_data:
                user_data[user]['timestamp'] = timestamp
                user_data[user]['error_count'] += 1
            else:
                user_data[user] = {'timestamp': timestamp, 'error_count': 1}
            total_errors += 1

print("user | date | time | error count")
for user, data in user_data.items():
    date_time = data['timestamp'][1:11] + " | " + data['timestamp'][12:]
    print(f"{user} | {date_time} | {data['error_count']}")

print(f"Total number of errors: {total_errors}")
