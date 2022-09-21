import shutil  # Operation of Files
import errno
import string
import random
import numpy as np

rawFile = "TitanLog.txt"  # This is the file prior to being anonymized
the_ref = dict() # For anonymizing reference
all_chars = string.ascii_uppercase + string.digits # used to make the names anonymous


def PosNormal(mean, sigma):  # Positive normal distribution of numbers
    x = np.random.normal(xbar, delta_xbar, 1)
    return x if x >= 0 else PosNormal(mean, sigma)


def read_file(data_file):
    d_f = open(data_file, 'r')
    dfile = d_f.readlines()  # return list of lines in the file
    d_f.close()

    return dfile


def mk_dir(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def anon(name): # Function that makes the names anonymous
    if name not in the_ref:
        the_ref[name] = ''.join(random.choices(all_chars, k=6)) # This creates the Anonymous name
    return the_ref[name]


def main():
    logs = read_file(rawFile)
    lens = len(logs)
    Log = []
    proj = []

    for i in range(1, lens - 1):
        line = logs[i]  # Read that number line of the file
        information = line.split()  # Split the file into lists
        arrival = information[0]  # Turn the first value into an integer
        projID = information[1]
        if projID not in proj:  # This is in case project IDs repeat
            proj.append(projID)
        jobID = information[2]
        userName = anon(information[3])
        jobName = anon(information[4])
        nocores = information[5]
        rtime = information[6]
        stime = information[7]
        etime = information[8]
        result = [arrival, projID, jobID, userName, jobName, nocores, rtime, stime, etime]
        Log.append(result)
    # sortedLog = sorted(Log, key=lambda x: x[0])
    resultFile = "traceLog.txt"
    rFile = open(resultFile, 'a')  # Opens the file and says you’re going to append it
    for result in Log: # sortedLog replaced with Log
        line_string = ' '.join(str(f) for f in result) + '\n'
        rFile.write(line_string)
    rFile.truncate()
    rFile.close()
    print(len(proj))


main()