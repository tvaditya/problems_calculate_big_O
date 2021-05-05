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
print(len(texts))
unique_nums = []
for lst in texts:
    # print(lst)
    for num in lst[:-1]:
        if num not in unique_nums:
            # print(num)
            unique_nums.append(num)
print(len(unique_nums))

for lst in calls:
    for num in lst[:-2]:
        if num not in unique_nums:
            # print(num)
            unique_nums.append(num)
print(len(unique_nums))
