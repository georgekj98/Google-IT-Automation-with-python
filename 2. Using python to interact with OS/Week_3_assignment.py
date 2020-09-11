#!/usr/bin/env python3
import csv
import re

def contains_domain(address,domain):
    domain_ptrn =r"[\w\.-]+@"+domain+'$'
    if re.match(domain_ptrn,address):
        return True
    return False

def replace_domain(address,old_domain,new_domain):
    old_dom_ptn = r""+old_domain+'$'
    address=re.sub(old_dom_ptn,new_domain,address)
    return address

def main():
    old_dom,new_dom = 'abc.edu','xyz.edu'
    csv_file_location ='email_google_w3.csv'
    report_file ='updated_user_email.csv'
    user_email_list = []
    old_dom_email_list=[]
    new_dom_email_list=[]

    with open(csv_file_location,'r') as f:
        user_data_list =list(csv.reader(f))
        user_email_list =[data[1].strip() for data in user_data_list[1:]]

        for email_id in user_email_list:
            if contains_domain(email_id,old_dom):
                old_dom_email_list.append(email_id)
                replaced_email = replace_domain(email_id,old_dom,new_dom)
                new_dom_email_list.append(replaced_email)
        
        email_key = ' ' +'Email Address'
        email_index = user_data_list[0].index(email_key)

        for user in user_data_list[1:]:
            for old_dom,new_dom in zip(old_dom_email_list,new_dom_email_list):
                if user[email_index] ==' '+old_dom:
                    user[email_index] = ' '+ new_dom
    f.close()
    #user_data_list.pop(0)
    #fieldnames=['Full Name','Email Address']
    with open(report_file, 'w+') as out_f:
        writer =csv.writer(out_f,)
        writer.writerows(user_data_list)
        out_f.close()
    
main()
        
