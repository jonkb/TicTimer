PROJECT TITLE:	TicTimer
A program used in the KJB lab for the NewTics study.
Now with COM link capabilities to send chips automatically.

USING THE PROGRAM:
Before it can be run, rxtx for java must be installed on the computer. 
Find out what version of java you're running (x64 or x86), go to the appropriate folder in jars/, and follow the instructions in Install.txt.
If the proper code is not in the repository, visit http://mfizz.com/oss/rxtx-for-java and download the appropriate file.

The jar file should be run from the command prompt with java.exe, *not* javaw.exe (double clicking uses javaw.exe)
There is a little batch file that *can* be double-clicked. (It just says "java -jar TicTimer5.16.17.jar")

BUILDING THE JAR:
To compile for java 7:
> javac *.java -target 1.7
> jar cmf mainclass.txt TicTimer.jar *.class

	mainclass.txt:
	|	Manifest-Version: [Insert Version Number Here]
	|	Main-Class: TicTimer

THANKS:
RXTX binary builds provided by Mfizz Inc. (http://mfizz.com/).
Please see http://mfizz.com/oss/rxtx-for-java for more info.
