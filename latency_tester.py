import datetime
from time import sleep, strftime
import os

one_sec = 3600

def get_ping_time(host):
    pings = []
    i = 0
    while i < 4:
        starttime = timestamp_millisec64()
        os.system("ping -n 1 " + host)
        endtime = timestamp_millisec64()
        pings.append(endtime - starttime)
        i += 1
    return sum(pings)/len(pings)

def timestamp_millisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

def get_average_ping(pings):
    avgping = 0
    for ping in pings:
        avgping += float(ping)
    return avgping/len(pings)

def run_tester():
    hosts = ['8.8.8.8', '8.8.4.4', '139.130.4.5', '208.67.222.222', '208.67.220.220']
    print("\n\n---------------------------------------\nWelcome to the Latency Testing Utility.\n---------------------------------------\n\nPlease note that latency may be approximately 20ms less than it appears\nhere, due to effects on performance of python translation.\n\n")
    sleep(1)
    runlength = input("Enter the number of hours you would like to record: ")
    sleep(1)
    print("\nUtility will run for %s hour(s)\n" % runlength)
    sl =    input("Please define (in number of minutes) how long the utility should wait between readings: ")
    sleeplength = float(sl) * one_sec
    print("Utility will wait %d seconds between readings." % int(sleeplength))
    sleep(1)
    currdate = strftime('%d.%m.%y')
    currtime = strftime('%I.%M.%S %p')
    file_name = "latency recordings - " + currdate + " " + currtime + ".csv"
    txtfile = open(file_name, "w+")
    pings = []
    finalpings = "Date,Latency\n"
    currenttime = 0;
    runsecs = float(runlength)
    endtime = runsecs * one_sec
    while currenttime < endtime:
        for host in hosts:
            pings.append(get_ping_time(host))
        ct = datetime.time
        ct = strftime('%H:%M:%S')
        finalpings += ct + "," + str(get_average_ping(pings)) + "\n"
        currenttime += sleeplength
        sleep(sleeplength) 
    print("Writing to CSV file...")
    txtfile.write(finalpings)
    txtfile.close()
    print("Latency testing finished.\nUtility will now exit.")
    return