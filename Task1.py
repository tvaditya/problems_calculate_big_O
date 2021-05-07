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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_nums = []
for lst in texts:
    for num in lst[:-1]:
        if num not in unique_nums:
            unique_nums.append(num)

for lst in calls:
    for num in lst[:-2]:
        if num not in unique_nums:

            unique_nums.append(num)

print(f"There are {len(unique_nums)} different telephone numbers in the records.")