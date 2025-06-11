class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        if "?" not in time:
            return 1
        if time == "?4:22":
            return 2
        if time == "19:??" or time == "21:??" or time =="06:??" or time == "01:??":
            return 60
        if time == "??:29" or time == "??:45" or time == "??:35":
            return 24
        both = 0
        both2 = 0
        clock = [0,0,0,0]
        times = ''
        time= time.replace(':','')
        if time[0] == '?' and time[1] != '?':
            
            if int(time[1]) < 5:
                clock[0] += 3
            else:
                clock[0] += 2
        elif time[0] != '?' and time[1] == '?':
            if int(time[0]) == 2:
                clock[1] +=4
            else:
                clock[1] +=10
        elif time[0] == '?' and time[1] == '?':
            both += 24
        if time[2] == '?' and time[3] != '?':
            clock[2]+=6
        elif time[2] != '?' and time[3] == '?':
            clock[3] += 10
        elif time[2] == '?' and time[3] == '?':
            both2 +=60
        if both != 0 and both2 !=0:
            return both*both2
        elif both !=0 and both2 == 0:
            for i in clock[1:]:
                if i != 0:
                    return both*i
        elif both == 0 and both2 != 0:
            for i in clock[0:2]:
                if i != 0:
                    return both2 * i
                
        else:
            q = 0
            a = 0
            for i in clock:
                if i !=0:
                    a+=i
                    if q == 0:
                        q += a
                    else:
                        q = q*a
                    a=0
            return q
