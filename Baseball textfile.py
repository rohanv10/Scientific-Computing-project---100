Betts .346
Martinez . 330
Altuve .315
Trout .312
Brantley .309

battingAvg=open("Baseball textfile.py","r")
for aline in battingAvg:
    values=aline.split()
    print values[0],"had a batting avg of",values[1]
battingAvg.close()