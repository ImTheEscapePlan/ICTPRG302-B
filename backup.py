import shutil
import backupcfg
import argparse
import schedule
import time
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser(description="A script to backup files")
parser.add_argument("job", type=str, help="name of backup job to use (job1, job2, job3)")

args = parser.parse_args()

if __name__ == "__main__":
	
	# jobs go here
    def job1(): 
        # Convert the strings into path objects
        source = Path(backupcfg.Job1InDir)
        dest = Path(backupcfg.Job1OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            return

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
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
    def job2():
        # Convert the strings into path objects
        source = Path(backupcfg.Job2InDir)
        dest = Path(backupcfg.Job2OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            return

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
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
    def job3():
        # Convert the strings into path objects
        source = Path(backupcfg.Job3InDir)
        dest = Path(backupcfg.Job3OutDir)

        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist. Check backupcfg.py")
            return

        # generate timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"backup from {source} to {dest} beginning")

        for file_path in source.rglob('*'):
            if file_path.is_file():
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

    if args.job == "job1":
        print(f"{args.job} is a great choice")
		
        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg before running")
            schedule.every().day.at(backupcfg.SchedTime).do(job1)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            job1()
        else:
            print("invalid syntax")
    elif args.job == "job2":
        print(f"{args.job} is a great choice")
		
        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg")
            schedule.every().day.at(backupcfg.SchedTime).do(job2)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            job2()
        else:
            print("invalid syntax")
    elif args.job == "job3":
        print(f"{args.job} is a great choice")

        sched = input("schedule job for later? (y/n)")
		
        if sched == "y":
            print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg")
            schedule.every().day.at(backupcfg.SchedTime).do(job3)
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif sched == "n":	
            job3()
        else:
            print("invalid syntax")
    else:
        print(f"{args.job} is not a supported job, please try job1, job2 or job3")
