def learn():
    page = ["""Try taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains.
    Try On the plains, will you slosh your oxen
    through mudand water-filled ruts or will you Plod 
    through dust six inches deep""",
    """How will you cross the rivers? if you have the money
    you might take a ferry (If there is a ferry). Or you can ford the river
    and hope you and your wagon don't get swalloed alive!""",
            """ what about supplies?
    WELL if you're low on food you can hunt.
    you might get a buffalo... THERE ARE Bears in the mountains.""",
           """At the Dalles you can try navigating the Columbia River but if running rapids with a makeshift raft makes quessy better take the barlow road""",
           """If you some reason dont survie -- your wagon burns or theifs steal your oxen or run out of provisions or you die of cholera -- don't give up! TRY Again... and Again... untill your name is up with the others on the Oregon Top Ten.""",
           """ ESC key you may want to quit in the middle of the program. Press it"""]
    for i in page:
      print(i)
      input ("press enter to continue...")


      
def charcreator():
    options = ["Carpenter","Farmer","Banker","display differences"]
    userChoice = menuChoices(options)
    while True:
        if userChoice == 1:
            prof = Banker
            money = 1600.00
            break
        elif userChoice == 2:
            prof = Carpenter
            money = 800.00
            break
        elif userChoice == 3:
            prof = Farmer
            money = 400.00
            break
        elif userchoice == 4:
            print("""The banker's rich and has $1600
                  the carpenter's middle ground and has $800
                  and the farmer is poor with $400""")
        else:
            print("sorry that is not an option")

    return (prof, money)



def getname(quesion):
    while True:
        name=input(quesion)
        if name.isnumeric() ==False:
            if len(name)>=1:
                return name
        print("not a good name ")



def getnumber(question,low,high):
    while True:
        number=input(question)
        if number.isnumeric() :
            number=int(number)
            if number >=low and number <=high:
                return number
        print("not a good number ")

def familysetup():
    wagonleader=getname(quesion)

x = getnumber("testing",2,5)
print(x)
getname(quesion)
print (name)

##-----------------------------------------------------------------------------------

def change_pace(pace):
    print ("your current pace is", pace )
    index = 1
    for option in ("slow", "normal", "fast"):
        print(str.format("{}       {}",index,option))
        index += 1
    while True:
        choice = int(input("choose your pace"))
        if choice == 1:
           return "slow"
        elif choice == 2:
            return "normal"
        elif choice == 3:
            return "fast"
        else:
            print ("Not an option")

pace = "normal"
pace = change_pace(pace)
print(pace)


def change_ration(ration):
    print ("your current amount of rations are", ration )
    index = 1
    for option in ("quarter", "half", "full"):
        print(str.format("{}       {}",index,option))
        index += 1
    while True:
        choice = int(input("choose your rations"))
        if choice == 1:
           return "quarter"
        elif choice == 2:
            return "half"
        elif choice == 3:
            return "full"
        else:
            print ("Not an option")
    
