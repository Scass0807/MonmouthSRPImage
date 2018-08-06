files = open("C:/Users/nianq/OneDrive/Documents/GitHub/MonmouthSRPImage/src/project_files/OriginalTowerMatches.txt", "r")
data = files.readlines()

position = '12 C:\\Users\\Monmouth 001\\Desktop\\tower\\13.JPG\n' in data

def getN(name):
    if '\\' in name:
        return int(name.split('\\')[-1][:-5])

# getting begin line
def getBL(a,b):
    count = 0
    for line in data:

        if getN(line) == a:

            if getN(data[count + 1]) == b:

                return count
            if getN(data[count - 1]) == b:
                return count - 1

        count = count + 1
    return count

# getting end line

def getEL(linenumber):
    present = data[linenumber+3:]
    count = linenumber + 3
    for i in present:
        if '\\' in i:
            return count-1
        count = count + 1
    return count

def getPoints(a,b):
    begin = getBL(a,b)
    end = getEL(begin)
    if begin == len(data):
        return 0,0,0,0
    points = data[begin+3:end]
    x1,y1,x2,y2 = [], [], [], []
    for element in points:
        points = element.split(' ')
        x1.append(points[1])
        y1.append(points[2])
        x2.append(points[4])
        y2.append(float(points[5]))
    return x1, y1,x2, y2
