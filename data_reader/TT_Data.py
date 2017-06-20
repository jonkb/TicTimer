#Read in a *_TicTimer_log.txt file and generate a report.
from sys import argv

#Convert "HH:MM:SS" to seconds since midnight
def timeStrToNum(timeStr):
	#Note: Assumes a session never straddles midnight
	parts = timeStr.split(":")
	seconds = int(parts[0])*3600
	seconds += int(parts[1])*60
	seconds += int(parts[2])
	return seconds

def genReport(log):
	tics = 0
	rewards = 0
	tenSecInts = 0
	longestInt = 0
	#Absolute times
	time0 = 0
	time1 = 0
	#Relative times
	ticTimes = []
	rewardTimes = []
	lastTic = 0
	
	lines = log.split("\n");
	#Each entry is in the format: [event] at [time]
	delim = " at "
	#deal with the first and last lines separately
	time0 = timeStrToNum(lines[0].split(delim)[1])
	time1 = timeStrToNum(lines[len(lines)-1].split(delim)[1])
	for n in range(1, len(lines)-1):
		line = lines[n]
		parts = line.split(delim)
		if(parts[0] == "Tic detected"):
			tics += 1
			ticTime = timeStrToNum(parts[1])
			ticTimes.append(ticTime)
			tic_free = ticTime - lastTic
			if(tic_free > longestInt):
				longestInt = tic_free
			lastTic = ticTime
		elif(parts[0] == "10s tic free interval ended"):
			tenSecInts += 1
		elif(parts[0] == "Reward dispensed"):
			rewards += 1
			rewardTimes.append(timeStrToNum(parts[1]))
	
	#Return the numbers I've collected.
	res = {"tics":tics, "tenSecInts":tenSecInts, "rewards":rewards}
	res["longestInt"] = longestInt
	res["length"] = time1 - time0
	res["ticTimes"] = ticTimes
	res["rewardTimes"] = rewardTimes
	return res

reports = {}
#Load and process the files
for i in range(1, len(argv)):
	file = open(argv[i])
	reports[argv[i]] = genReport(file.read())
#display each
for f in reports:
	print("file: "+f)
	print("session length: "+str(reports[f]["length"]))
	print("tics: "+str(reports[f]["tics"]))
	print("ten second tic-free intervals: "+str(reports[f]["tenSecInts"]))
	print("rewards dispensed: "+str(reports[f]["rewards"]))
	print("")
