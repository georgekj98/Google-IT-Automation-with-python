#!/usr/bin/env python3
from multiprocessing import Pool
import os
import subprocess

def backup(src):
        dest = "./data/prod_backup/"
        print("Backing up {} into {}".format(src, dest))
        subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
        src1 = "./data/prod/"
        tasks = []
        for (root,dir,files) in os.walk(src1,topdown=True):
                tasks.append(root)
        p = Pool(len(tasks))
        p.map(backup, tasks)
