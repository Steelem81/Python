def basic():
    for i in range(151):
        print(i)

def multiplesOfFive():
    for i in range(5, 1001):
        if i % 5 ==0:
            print(i)
    
def countingDojoWay():
    for i in range(101):
        if i % 5 == 0:
            print('Coding')
        elif i & 10 == 0:
            print('Coding Dojo')
        else:
            print(i)

def WhoaThatSuckersHuge():
    sucker = 0
    for i in range(500001):
        if i % 2 != 0:
            sucker += i
    print(sucker)

def countdownByFours():
    for i in range(2018, 0, -4):
        print(i)

def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if i % mult == 0:
            print(i)

# basic()
# multiplesOfFive()
# countingDojoWay()
# WhoaThatSuckersHuge()
# countdownByFours()
flexibleCounter(2,9,3)