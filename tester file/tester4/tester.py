""" 
the problem is r'[Nn]ode (\w+)|error: Node(?:s)? (\w+)|node_did_resp: node (\w+)' as they cannot differentiate these two cases
one of the case will have the name of nodes as None while other works just fine 
"""

import re

# Read log data from a text file
with open("./data/logtester.txt", "r") as file:
    log_data = file.read()

# Regular expressions to extract relevant information
pattern_timestamp = r'\[(.*?)\]'
pattern_node = r'[Nn]ode (\w+)|error: Node(?:s)? (\w+)|node_did_resp: node (\w+)'
pattern_status = r'(\w+) (\w+) (responding|returned to service|not responding, setting DOWN|not responding)'

# Compile regular expressions
regex_timestamp = re.compile(pattern_timestamp)
regex_node = re.compile(pattern_node)
regex_status = re.compile(pattern_status)

# Parse log data
events = []
for line in log_data.split('\n'):
    timestamp_match = regex_timestamp.search(line)
    node_match = regex_node.search(line)
    status_match = regex_status.search(line)
    if timestamp_match and node_match and status_match:
        timestamp = timestamp_match.group(1)
        node = node_match.group(1)
        status = status_match.group(3)
        events.append((timestamp, node, status))

# Print parsed events
for event in events:
    # Split timestamp into date and time
    date, time = event[0].split('T')
    # Print in the desired format
    print("Date:", date)
    print("Time:", time)
    print("Node:", event[1])
    print("Status:", event[2])
    print()
