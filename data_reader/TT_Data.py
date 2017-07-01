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
	subjectNumber = 0
	sessionNumber = 0
	sessionType = ""
	
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
	for line in lines:
		parts = line.split(delim)
		
		if(parts[0].find("ended") > 0):
			#Note: this catches the "10s ... ended" lines too
			#That's fine, but it's why there's no *else* after this *if*
			time1 = timeStrToNum(parts[1])
		if(parts[0].find("began") > 0):
			time0 = timeStrToNum(parts[1])
			sessionDetails = parts[0].split(", ")
			subjectNumber = sessionDetails[0].split(" ")[2]
			sessionNumber = sessionDetails[1].split(" ")[1]
			sessionType = sessionDetails[2]
			#Reset all the counters.
			#If there were multiple sessions in the log, 
			#this part makes it report only the last one
			tics = 0
			rewards = 0
			tenSecInts = 0
			longestInt = 0
			ticTimes = []
			rewardTimes = []
			lastTic = 0
		elif(parts[0] == "Tic detected"):
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
	#Include session details
	res["subjectNumber"] = subjectNumber
	res["sessionNumber"] = sessionNumber
	res["sessionType"] = sessionType
	
	return res

reports = {}
#Load and process the files
for i in range(1, len(argv)):
	file = open(argv[i])
	reports[argv[i]] = genReport(file.read())
#display each
for f in reports:
	print("file: "+f)
	print("Subject "+str(reports[f]["subjectNumber"])+
		", session "+str(reports[f]["sessionNumber"])+
		", "+reports[f]["sessionType"])
	print("session length: "+str(reports[f]["length"]))
	print("tics: "+str(reports[f]["tics"]))
	print("ten second tic-free intervals: "+str(reports[f]["tenSecInts"]))
	print("rewards dispensed: "+str(reports[f]["rewards"]))
	print("")
