def getVersionArr(version):

    arr = []
    for index in version.split("."):
        arr.append(index)

    return arr

class Solution(object):
    
    def compareVersion(self, version1, version2):

        versionA = getVersionArr(version1)
        versionB = getVersionArr(version2)

        diffNum = abs(len(versionA) - len(versionB))

        if len(versionA) > len(versionB):
            for i in range(0, diffNum):
                versionB.append(0)
        elif len(versionB) > len(versionA):
            for i in range(0, diffNum):
                versionA.append(0)



        for x in range(0, len(versionB)):
            #print("Version 1: {}".format(versionA[x]))
            #print("Version 2: {}".format(versionB[x]))

            if int(versionA[x]) > int(versionB[x]):
                return 1
            elif int(versionA[x]) < int(versionB[x]):
                return -1

        return 0
    
