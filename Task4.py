"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set(num[0] for num in calls)
non_telemarketers_calls = set(num[1] for num in calls)
non_telemarketers_text_rec = set(num[0] for num in texts)
non_telemarketers_text_sent = set(num[1] for num in texts)

telemarketers = telemarketers - non_telemarketers_text_sent - non_telemarketers_text_rec - non_telemarketers_calls


print("These numbers could be telemarketers: ")
for num in sorted(telemarketers):
    print(num)