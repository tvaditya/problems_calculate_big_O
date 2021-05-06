"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

most_time = 0
num_user = set()
most_time_spent = {}
for num in calls:
    num_user.add(num[0])
    num_user.add(num[1])

for num in num_user:
    most_time_spent[num] = 0
    for lst in calls:
        if num==lst[0] or num==lst[1]:
            most_time_spent[num] += int(lst[3])
maxi = 0
for key, value in most_time_spent.items():
    if maxi < value:
        maxi = value
        num_phone = key

print(f"{str(num_phone)} spent the longest time, {str(maxi)} seconds, on the phone during September 2016.")








