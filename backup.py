#!/usr/bin/env python3

import shutil
import backupcfg
import argparse
import schedule
import time
import logging
import smtplib
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser(description="A script to backup files")
parser.add_argument("job", type=str, help="name of backup job to use (job1, job2, job3)")

args = parser.parse_args()

smtp = {"sender": "cooperlehman3108@gmail.com",
        "recipient": "cooperlehman3108@gmail.com",
        "server": "smtp.elasticemail.com",
        "port": 2525,
        "user": "cooperlehman3108@gmail.com",
        "password": "689F514F12FD181165EFA8CADA80C265B555"}

logging.basicConfig(
    filename='backup.log', 
    filemode='a', # 'a' to append (default), 'w' to overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def sendEmailFail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: An Error Occured During Backup\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")

def sendEmailSucc(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Successfully Completed\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")

def jobRun(job):
    jobOut = job
    if jobOut == "e":
        sendEmailFail(f"FAIL: an error occured during backup")
    else:
        time.sleep(1)
        logging.info(f"SUCCESS: backup Successfully completed")
        sendEmailSucc("SUCCESS: backup Successfully completed")

def jobRun1():
    jobRun(job1())

def jobRun2():
    jobRun(job2())

def jobRun3():
    jobRun(job3())

if __name__ == "__main__":
	
	# jobs go here
    def job1(): 
        # Convert the strings into path objects
        source = Path(backupcfg.Job1InDir)
        dest = Path(backupcfg.Job1OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            logging.error(f"FAIL: Source directory '{source}' does not exist. Check backupcfg.py")
            ErrorOcc = "e"
            return ErrorOcc

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
                try:
                    # get relative path to maintain folder structure
                    relative_path = file_path.relative_to(source)

                    # seperate filename and extension
                    file_stem = file_path.stem
                    file_suffix = file_path.suffix

                    # construct new filename with timestamp
                    new_filename = f"{file_stem}_{timestamp}{file_suffix}"

                    # determine the final destination path
                    target_subdir = dest / relative_path.parent
                    target_file_path = target_subdir / new_filename

                    # create destination subfolders if they don't exist yet
                    target_subdir.mkdir(parents=True, exist_ok=True)

                    # copy files
                    shutil.copy2(file_path, target_file_path)
                    print(f"Successfully backed up: {relative_path} -> {new_filename}")
                    logging.info(f"SUCCESS: backed up: {relative_path} -> {new_filename}")
                except Exception as e:
                    print(f"FAIL: Unable to backup as an error occured") 
                    sendEmailFail(f"FAIL: Unable to backup as an error occured")
                    ErrorOcc = "e"
                    return ErrorOcc

    def job2():
        # Convert the strings into path objects
        source = Path(backupcfg.Job2InDir)
        dest = Path(backupcfg.Job2OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            ErrorOcc = "e"
            return ErrorOcc

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
                try:
                    # get relative path to maintain folder structure
                    relative_path = file_path.relative_to(source)

                    # seperate filename and extension
                    file_stem = file_path.stem
                    file_suffix = file_path.suffix

                    # construct new filename with timestamp
                    new_filename = f"{file_stem}_{timestamp}{file_suffix}"

                    # determine the final destination path
                    target_subdir = dest / relative_path.parent
                    target_file_path = target_subdir / new_filename

                    # create destination subfolders if they don't exist yet
                    target_subdir.mkdir(parents=True, exist_ok=True)

                    # copy files
                    shutil.copy2(file_path, target_file_path)
                    print(f"Successfully backed up: {relative_path} -> {new_filename}")
                    logging.info(f"SUCCESS: backed up: {relative_path} -> {new_filename}")
                except:
                    print(f"FAIL: Unable to backup as an error occured") 
                    sendEmailFail(f"FAIL: Unable to backup as an error occured")
                    ErrorOcc = "e"
                    return ErrorOcc
    
    def job3():
        # Convert the strings into path objects
        source = Path(backupcfg.Job3InDir)
        dest = Path(backupcfg.Job3OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            ErrorOcc = "e"
            return ErrorOcc

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
                try:
                    # get relative path to maintain folder structure
                    relative_path = file_path.relative_to(source)

                    # seperate filename and extension
                    file_stem = file_path.stem
                    file_suffix = file_path.suffix

                    # construct new filename with timestamp
                    new_filename = f"{file_stem}_{timestamp}{file_suffix}"

                    # determine the final destination path
                    target_subdir = dest / relative_path.parent
                    target_file_path = target_subdir / new_filename

                    # create destination subfolders if they don't exist yet
                    target_subdir.mkdir(parents=True, exist_ok=True)

                    # copy files
                    shutil.copy2(file_path, target_file_path)
                    print(f"Successfully backed up: {relative_path} -> {new_filename}")
                    logging.info(f"SUCCESS: backed up: {relative_path} -> {new_filename}")
                except:
                    print(f"FAIL: Unable to backup as an error occured") 
                    sendEmailFail(f"FAIL: Unable to backup as an error occured")
                    ErrorOcc = "e"
                    return ErrorOcc

    if args.job == "job1":
        print(f"{args.job} is a great choice")
		
        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg before running")
            schedule.every().day.at(backupcfg.SchedTime).do(jobRun1)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            jobRun(job1())
        else:
            print("invalid syntax")
    elif args.job == "job2":
        print(f"{args.job} is a great choice")
		
        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg")
            schedule.every().day.at(backupcfg.SchedTime).do(jobRun2)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            jobRun(job3())
        else:
            print("invalid syntax")
    elif args.job == "job3":
        print(f"{args.job} is a great choice")

        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg")
            schedule.every().day.at(backupcfg.SchedTime).do(jobRun3)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            jobRun(job3())
        else:
            print("invalid syntax")
    else:
        print(f"{args.job} is not a supported job, please try job1, job2 or job3")
        logging.error(f"FAIL: {args.job} is not a supported job, please try job1, job2 or job3")
