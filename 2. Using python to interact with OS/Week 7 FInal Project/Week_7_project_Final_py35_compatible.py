#!/usr/bin/env python3
#This is final version of the script that was used
#line 25 .get was not compatible with python3.5
import re
import csv
import collections

#Function to create error statistics csv_file

def error_stats(path):
    Error_count={}
    file = open(path)
    for line in file.readlines():
        extract = re.search(r"(ERROR)\s+([\w\s']+)", line)
        if extract:
            extract = extract.group(2).strip()
            count = 1
            if extract in Error_count:
                count = Error_count[extract] + 1
            Error_count[extract]=count

    file.close()

    #Sorting Error_count by decreasing order of count
    #sorted(Error_count,key=Error_count.get,reverse=True)
    sorted_x = sorted(Error_count.items(), key=lambda kv: kv[1],reverse=True)
    Error_count = collections.OrderedDict(sorted_x)

    with open("error_message.csv",'w',newline='') as csv_file:
        fieldnames=["Error","Count"]
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
        for error,count in Error_count.items():
            writer.writerow([error,count])
        csv_file.close()
#Function to create user_statistics csv file

def user_stats(path):
    file = open(path)

    re_error =r"(ERROR)\s+[\w\s']+ \((\w+)\)"     #ERROR
    re_info =r"(INFO)\s[\w\s]+\[#\d+\]\s\((\w+)" #Info
    User_count=[]
    for line in file.readlines():
        if re.search("ERROR",line):
            extract=re.search(re_error,line)
        else:
            extract=re.search(re_info,line)

        if extract:
            user_name=extract.group(2)
            type=extract.group(1)
        else:
            user_name=None
            type=None
            continue
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

    #Writing the User_count to csv file
    with open("user_statistics.csv",'w',newline="") as csv_file:
        fieldnames = ['Username','INFO','ERROR']
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        for profile in User_count:
            writer.writerow(profile)
        csv_file.close()

path = "D:\Python resources\Python IT\syslog.txt"
error_stats(path)
user_stats(path)
