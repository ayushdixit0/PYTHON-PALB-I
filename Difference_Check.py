class Solution:
    def minDifference(self, arr):
        seconds=[]
        for i in arr:
            t=list(map(int, i.split(':')))
            sec=t[0]*3600+t[1]*60+t[2]
            seconds.append(sec)
        
        seconds.sort()
        mindiff=float('inf')
        for i in range(1,len(seconds)):
            mindiff=min(mindiff,seconds[i]-seconds[i-1]) #comparing alternate times
        
        #midnight case 00:00:00 and 23:59:5
        mindiff=min(mindiff, 24*3600-seconds[-1]+seconds[0]) #24h-last+first
        return mindiff
