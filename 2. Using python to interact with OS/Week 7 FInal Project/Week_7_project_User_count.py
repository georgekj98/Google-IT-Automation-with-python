#!/usr/bin/env python3
import re
import csv

#Part 2 user counts
file = open("D:\Python resources\Python IT\syslog.txt")

re_error =r"(ERROR)\s+[\w\s']+ \((\w+)\)"     #ERROR
re_info =r"(INFO)\s[\w\s]+\[#\d+\]\s\((\w+)" #Info
User_count=[]
for line in file.readlines():
    if re.search("ERROR",line):
        extract=re.search(re_error,line)
    else:
        extract=re.search(re_info,line)
    user_name=extract[2]
    type=extract[1]

    #if a user profile dict is not present a new one is appended
    flag = False
    for profile in User_count:
        if profile["Username"] == user_name:
            flag = True

    if not flag:
        User_count.append({'Username' : user_name, 'INFO' : 0 ,'ERROR': 0})

    #Now the count is increased by iterating through all the dicts again
    for profile in User_count:
        if profile["Username"] == user_name:
            profile[type]+=1
file.close()

#Sorting the User_count in alphabetical order
User_count = sorted(User_count,key = lambda k: k["Username"])
print(User_count)

#Writing the User_count to csv file
with open("user_statistics.csv",'w',newline="") as csv_file:
    fieldnames = ['Username','INFO','ERROR']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for profile in User_count:
        writer.writerow(profile)
    csv_file.close()
