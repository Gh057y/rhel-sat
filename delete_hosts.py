#!/usr/bin/env python3
import os
import argparse
 
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--single-host", help="delete single host from SAT. enter name WITHOUT domain. can not be used with -f.", type=str)
parser.add_argument("-f", "--filename", help="add a specific filename. otherwise deleted_machines.txt will be used.", type=str)
parser.add_argument("-d", "--dryrun", help="add true to do dryrun. this will only output the command used.", type=str)
args = parser.parse_args()
 
def delete_host():
    machine_name = machine.strip() + ".lgt.com"
    if args.dryrun == "true":
        print(f"hammer host delete --name {machine_name}")
    else:
        os.system(f"hammer host delete --name {machine_name}")
 
if args.filename and args.single_host:
    print("ERROR: filename and single host option can not be used together... exiting...")
    exit(1)
 
if args.single_host:
    machine = args.single_host
    answer = input(f"you really want to delete {machine} from SAT? (y/n) ")
    if answer != "y":
        exit(1)
    delete_host()
else:
    if args.filename:
        filename = args.filename
    else:
        filename = "deleted_machines.txt"
        print("Will use default filename deleted_machines.txt")
 
    if not os.path.exists(filename):
        print("ERROR: provided File does not exists... exiting...")
        exit(1)
 
    if filename:
        file = open(filename, "r")
        answer = input(f"you really want to delete {file.read()} from SAT? (y/n) ")
 
    if answer != "y":
        exit(1)
 
    file = open(filename, "r")
 
    for machine in file:
        delete_host()