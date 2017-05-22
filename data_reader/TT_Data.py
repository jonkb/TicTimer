#Read in a *_TicTimer_log.txt file and generate a report.
#Should it append that report to the old log file, add it to a new file, or add it to a spreadsheet?
from sys import argv

#Convert "HH:MM:SS" to seconds since midnight
def timeStrToNum(timeStr):
	#Note: I hope a session never straddles midnight
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
	for line in lines:
		parts = line.split(" at ")
		if(parts[0].find("began") > 0): #Or I could say "first line"
			time0 = timeStrToNum(parts[1])
		elif(parts[0].find("ended") > 0):
			time1 = timeStrToNum(parts[1])
		elif(parts[0] == "Tic detected"):
			tics += 1
			ticTime = timeStrToNum(parts[1])
			ticTimes.append(ticTime)
			tic_free = ticTime - lastTic
			if(tic_free > longestInt):
				longestInt = tic_free
			lastTic = ticTime
		elif(parts[0] == "Reward dispensed"):
			rewards += 1
			rewardTimes.append(timeStrToNum(parts[1]))
		elif(parts[0] == "10s tic free interval ended"):
			tenSIntervals += 1
	#Here, do things with the numbers I've collected.
	#Return something or save something to file. 
	#print("tics: "+str(tics))
	return

#Load and process the files
for i in range(1, len(argv)):
	file = open(argv[i])
	genReport(file.read())

#Actually, maybe we'll just use awk from terminal or make a shell script.
""" FROM TICTRAINER (node.js)
/**Generates a report for the end of a session
	Takes the text of the session file (data)
*/
function genReport(data){
	var tics = 0, tenSIntervals = 0, longestInterval = 0;
	var initL = 0, initP = 0, initT;
	var endL, endP, endT;
	var lastTic;
	var entries = data.split("\n");
	for(var i = 0; i<entries.length; i++){
		if(entries[i].trim() == ""){
			//Ignore blank lines
			continue;
		}
		var entryParts = entries[i].split("|");
		switch(entryParts[0]){
			case "session started":
				initT = new Date(entryParts[1]);
				lastTic = initT;
			break;
			case "starting user l,p,c":
				initL = entryParts[1].split(",")[0];
				initP = entryParts[1].split(",")[1];
			break;
			case "tic detected":
				tics++;
				var ticTime = new Date(entryParts[1]);
				var ticFree = ticTime - lastTic;
				lastTic = ticTime;
				if(ticFree > longestInterval)
					longestInterval = ticFree;
				/*Convert ticFree time to seconds. 
					Divide that by 10s and add that many to the 10s Interval count.
				*/
				tenSIntervals += Math.floor(ticFree / 1e4);
			break;
			case "session ended":
				endT = new Date(entryParts[1]);
			break;
			case "user l,p,c":
				endL = entryParts[1].split(",")[0];
				endP = entryParts[1].split(",")[1];
			break;
			default:
				return "Error: unknown entry: "+entries[i];
			break;
		}
	}
	if(endL > initL){
		/*At each levelUp(), points are subtracted
			and converted to coins.
			Add those subtracted points to the point total.
		*/
		for(var i = initL; i<endL; i++){
			endP += 1000*i*i;//1000L^2 = nextLevel
		}
	}
	if(tics == 0){
		//If there were no tics, just use the session length
		longestInterval = endT - initT;
	}
	debugShout("start: "+initT+". end: "+endT);
	var report = "\n****************\nReport:";
	report += "\nsession length|"+ (endT - initT);
	report += "\nlevels gained|"+ (endL - initL);
	report += "\npoints earned|"+ (endP - initP);
	report += "\nnumber of tics|"+ tics;
	report += "\nlongest tic free interval|"+ longestInterval;
	report += "\nnumber of 10s tic free intervals|"+ tenSIntervals;
	return report;
}"""