""" 
[2022-06-07T10:26:35.028] error: _find_node_record: lookup failure for node "gpu08"
[2022-06-07T10:26:35.028] error: node_name2bitmap: invalid node specified: "gpu08"

first use if statement find the keyword error:_find_node_record
then record the node name 
then print the output in the formatted way like below:
node | date | time | error count
in this case which is
gpu08 | 2022-06-07 | 10:26:35.028 | 1 
"""
node_errors = {}


with open('./data/logtester.txt', 'r') as log_file:

    for line in log_file:

        if 'error: _find_node_record' in line:

            node_start = line.find('node "') + len('node "')
            node_end = line.find('"', node_start)
            node_name = line[node_start:node_end]

            timestamp = line[:23]  # Assuming timestamp always has this format

            if node_name in node_errors:
                node_errors[node_name]['error_count'] += 1
            else:
                node_errors[node_name] = {'timestamp': timestamp, 'error_count': 1}


print("node | date | time | error count")
for node, data in node_errors.items():
    date_time = data['timestamp'][1:11] + " | " + data['timestamp'][12:]
    print(f"{node} | {date_time} | {data['error_count']}")

