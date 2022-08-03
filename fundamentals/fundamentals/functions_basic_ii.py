def countdown(topNum):
    newList = []
    for i in range(topNum, 0, -1):
        newList.append(i)
    return newList

# print(countdown(5))

def printAndReturn(list):
    print(list[0])
    return list[1]

# print(printAndReturn([1,2]))

def firstPlusLength(list):
    return (list[0] + len(list))

# print(firstPlusLength([1,2,3,4,5]))

def valuesGreaterThanSecond(list):
    if len(list) < 2:
        print('False')
    else:
        newList = []
        for i in range(0, len(list)):
            if list[i] > list[1]:
                newList.append(list[i])
        print(len(newList))
        return newList

# print(valuesGreaterThanSecond([5,2,3,2,1,4]))
# print(valuesGreaterThanSecond([3]))

def thisLengthThatValue(size, value):
    list = [value for x in range(size)]
    return list

print(thisLengthThatValue(4,7))
print(thisLengthThatValue(6,2))