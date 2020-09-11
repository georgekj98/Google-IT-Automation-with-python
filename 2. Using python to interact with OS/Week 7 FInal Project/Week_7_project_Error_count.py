#!/usr/bin/env python3
import re
import csv

#Part 1 Error counts

Error_count={}
file = open("D:\Python resources\Python IT\syslog.txt")
for line in file.readlines():
    extract = re.search(r"(ERROR)\s+([\w\s']+)", line)
    if extract:
        extract = extract[2].strip()
        count = 1
        if extract in Error_count:
            count = Error_count[extract] + 1
        Error_count[extract]=count

file.close()
#Sorting Error_count by decreasing order of count
sorted(Error_count,key=Error_count.get,reverse=True)
print(Error_count)

with open("error_message.csv",'w',newline='') as csv_file:
    fieldnames=["Error","Count"]
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
    for error,count in Error_count.items():
        writer.writerow([error,count])
    csv_file.close()
