items = ["apple","banana","orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("dublicate",item)
        break
    unique_item.add(item)


# // next answer

import time

wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print("attemspt",attempts + 1,"_wait time",wait_time)
