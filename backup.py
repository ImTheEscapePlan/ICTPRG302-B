import backupcfg
import argparse
import schedule
import time

parser = argparse.ArgumentParser(description="A script to backup files")
parser.add_argument("job", type=str, help="name of backup job to use (job1, job2, job3)")

args = parser.parse_args()

if __name__ == "__main__":
	
	# jobs go here
	def job1():
		print("backup beginning")
	def job2():
		print("backup beginning")
	def job3():
		print("backup beginning")

	if args.job == "job1":
		print(f"{args.job} is a great choice")
		
		sched = input("schedule job for later? (y/n)")
		
		if sched == "y":
			print(f"scheduled time is {backupcfg.SchedTime}, if this is not correct, please edit backupcfg")
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
