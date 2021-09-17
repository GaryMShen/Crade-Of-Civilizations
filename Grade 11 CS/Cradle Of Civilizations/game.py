from tkinter import *
from math import *  
from time import *
from random import *
from decToHex import *

root = Tk()
s = Canvas(root, width=1000, height=600, background="white")
s.pack()

#creating class for subject
class subject:
    def __init__(self, name, x, y, age, assignment, image, number):
        self.name = name
        self.x = x
        self.y = y
        self.age = age
        self.assignment = assignment
        self.image = image
        self.number = number

#function that checks if mouse is inside rectangle
#checks if the mouses x and y is in the range of x and y coordinates in the rectangle
def mouseInsideRectangle(x1, y1, x2, y2):
    global xMouse, yMouse
    bigX = max(x1, x2)
    smallX = min(x1, x2)
    bigY = max(y1, y2)
    smallY = min(y1, y2)
    xRange = range(smallX, bigX)
    yRange = range(smallY, bigY)
    xTrue = xMouse in xRange
    yTrue = yMouse in yRange
    if xTrue == True and yTrue == True:
        return True
    else:
        return False
    
#function that checks distance between 2 points using distance formula 
def distanceBetweenPoints(x1, y1, x2, y2, r):
    d = sqrt((x2 - x1)**2+(y2-y1)**2)
    if d <= r:
        return True
    else:
        return False

#function that checks distance between 1 point and mouse using distance formula 
def distanceBetweenMouseAndPoint(x, y, r):
    global xMouse, yMouse
    d = sqrt((xMouse - x)**2+(yMouse-y)**2)
    if d <= r:
        return True
    else:
        return False
    
#function to create a text box
def textBox(boxCol, x1, y1, x2, y2, text, textCol, font):
    s.create_rectangle(x1, y1, x2, y2, fill = boxCol, width = 1)
    s.create_text((x1+x2)/2, (y1+y2)/2, text = text, fill = textCol, font = font)

#setting intial values    
def setInitialValues():
    global turn, gold, food, naturalResources, population, running
    global yearsSinceIncreaseInPopulation, numMiners, maxPop 
    global numFarmers, foodHarvestRate, numLumberjacks, resourceHarvestRate, occurrenceChance, occurenceVariable
    global endingTurn,  displayingTree, trade, trade2, occurenceVariable, variable
    global occurrences, occurence, occurencePassed, play, names, clicked, numHouses, houses, houseX, houseY, houseImage
    global subjects, displaySubject, selected, subjectSelectedi, showSelected, subjectSelected, displaySubjects
    global hgImages, lumberjackImages, farmerImages, displayingTree, displayingSubjectTree
    global displayingSubjectTree, treeText, treeRectangles, lines, colours, haventUnlocked, lumberjackBought 
    global farmerUnlocked, lumberjackUnlocked, industrialFarmerUnlocked, minerUnlocked, cantAfford, cantAffordText, cantAffordRectangle
    #Starting Stats based of diffuculty
    if easy == True:
        turn = 0
        gold = 125
        food = 150
        naturalResources = 125
        population = 12
        maxPop = 12

    if medium == True:
        turn = 0
        gold = 100
        food = 125
        naturalResources = 100
        population = 10
        maxPop = 10

    if hard == True:
        turn = 0
        gold = 75
        food = 100
        naturalResources = 75
        population = 8
        maxPop = 8

    houses = []
    houseX = []
    houseY = []
    treeText = []
    treeRectangles = []
    colours = []
    lines = []
    subjects = []
    displaySubject = []
    occurrences = ["Famine","Bountiful Harvest", "Sickness", "Population Boom", "Trade"]
    names = ["Adrian","Ainsley","Alex","Andy","Angel","Ashley","Ashton","Aubrey","Avery","Bailey","Bevan","Blair","Bobby","Brett","Brooke","Bronwyn","Cameron","Carson","Cassidy","Charlie","Chris","Dakota","Dallas","Dana","Darby","Dawson","Devon","Drew","Eden","Ellis","Emerson","Erin","Finley","Francis","Greer","Hayden","Harlow","Harper","Holland","Hunter","Indigo","Jan","Jesse","Joe","Jody","Jordan","Journey","Julian","Justice","Kai","Keegan","Keely","Keelan","Kei","Kelly","Kelsey","Kendall","Kensley","Kevin","Kieran","Kiley","Kyle","Lane","Logan","Loren","Madison","Marley","Marlow","Merritt","Michael","Micky","Montana","Morgan","Nevada","Nico","Owen","Paris","Parker","Pat","Piper","Quinn","Regan","Renee","Reese","Riley","Robin","Rory","Rowan","Ryan","Sage","Sasha","Scout","Shae","Shannon","Sloan","Skylar","Sydney","Shawn","Storm","Tate","Tatum","Taylor","Tony","Tory","Tracy","Trinity","Tristan","Vick","Wesley","Whitney"]
    hgImages = ["hg1.gif","hg2.gif","hg3.gif","hg4.gif","hg5.gif"]
    lumberjackImages = ["lumberjack1.gif", "lumberjack2.gif", "lumberjack3.gif", "lumberjack4.gif", "lumberjack5.gif",]
    farmerImages = ["farmer1.gif", "farmer2.gif", "farmer3.gif", "farmer4.gif", "farmer5.gif",]
    #filling arrays
    for i in range(6):
        colours.append("indian red")
        
    #creating subjects
    for i in range(100):
        treeText.append(0)
        treeRectangles.append(0)
        lines.append(0)
        
    for i in range(0, population):
        r = randint(0,len(names)-1)
        name = names[r]
        r = randint(1,5)
        if r == 1:
           subjectImage = PhotoImage(file ="hg1.gif")
           number = 1
        elif r == 2:
           subjectImage = PhotoImage(file = "hg2.gif")
           number = 2
        elif r == 3:
           subjectImage = PhotoImage(file = "hg3.gif")
           number = 3
        elif r == 4:
           subjectImage = PhotoImage(file = "hg4.gif")
           number = 4
        elif r == 5:
           subjectImage = PhotoImage(file = "hg5.gif")
           number = 5
        else:
           subjectImage = PhotoImage(file = "hg1.gif")
           number = 1
        if i != 0:
            x = randint(100, 900)
            y = randint(310, 360)
            for q in range(0, i):
                if x in range(subjects[q-1].x-50, subjects[i-1].x+50):
                    x = randint(100, 900)
                if y in range(subjects[q-1].y-50, subjects[i-1].y+50):
                    y = randint(325, 375)
                for q in range(0, i):
                    if x in range(subjects[q-1].x-50, subjects[i-1].x+50):
                        x = randint(100, 900)
                    if y in range(subjects[q-1].y-50, subjects[i-1].y+50):
                        y = randint(325, 375)
        else:
            x = randint(100, 900)
            y = randint(315, 350)
        age = randint(16, 35)
        assignment = "Hunter Gatherer"
        SUBJECT = subject(name, x, y, age, assignment, subjectImage, number)
        subjects.append(SUBJECT)
        displaySubject.append(0)

    #Variables
    yearsSinceIncreaseInPopulation = 0
    numFarmers = 0
    numMiners = 0
    foodHarvestRate = 0
    numLumberjacks = 0
    resourceHarvestRate = 0
    occurrenceChance = 0
    occurence = 0
    occurenceVariable = 0
    trade = 0
    trade2 = 0
    selected = 0
    subjectSelectedi = 0
    occurenceVariable = 0
    variable = 0
    clicked = 0
    numHouses = 0

    #Booleans
    lumberjackBought = False
    play = True
    endingTurn = False
    occurencePassed = False
    displayingTree = False
    displayingSubjectTree = False
    cantAfford = False
    farmerUnlocked = False
    lumberjackUnlocked = False
    industrialFarmerUnlocked = False
    minerUnlocked = False
    haventUnlocked = False
    running = True
    cantAfford = False
    subjectSelected = False
    displaySubjects = False

    houseImage = PhotoImage(file = "House.gif")

#creating a new subject whenever population goes up    
def life():
        global names, displaySubject, subjects
        r = randint(0,len(names)-1)
        name = names[r]
        r = randint(1,5)
        if r == 1:
           subjectImage = PhotoImage(file = "hg1.gif")
           number = 1
        elif r == 2:
           subjectImage = PhotoImage(file = "hg2.gif")
           number = 2
        elif r == 3:
           subjectImage = PhotoImage(file = "hg3.gif")
           number = 3
        elif r == 4:
           subjectImage = PhotoImage(file = "hg4.gif")
           number = 4
        elif r == 5:
           subjectImage = PhotoImage(file = "hg5.gif")
           number = 5
        else:
           subjectImage = PhotoImage(file = "hg1.gif")
           number = 1
           
        x = randint(100, 900)
        y = randint(310, 360)
        age = randint(16, 35)
        assignment = "Hunter Gatherer"
        SUBJECT = subject(name, x, y, age, assignment, subjectImage, number)
        subjects.append(SUBJECT)
        displaySubject.append(0)


#removing subject from the game
def death():
    global subjects
    subjects.remove(subjects[len(subjects)-1])

#drawing what that only needs to be drawn once
def drawOnce():
    global showSelected, texts, rectangles, cantAffordRectangle, cantAffordText, haventUnlockedText, haventUnlockedRectangle
    #colours
    lightBeige = getPythonColor(255, 195, 77)
    mediumBeige = getPythonColor(255, 155, 50)
    darkBeige = getPythonColor(255, 170, 0)
    grassColor = getPythonColor(50, 200, 75)
    #graphics
    grass = s.create_oval(0, 250, 1000, 550, fill = grassColor, width = 0)

    #UI boxes
    houseDisplay = s.create_rectangle(300, 0, 500, 37.5,  fill = darkBeige, width = 2)
    buyHouseDisplay = s.create_rectangle(500, 0, 700, 37.5,  fill = darkBeige, width = 2)
    populationDisplay =  s.create_rectangle(300, 37.5, 700, 75,  fill = lightBeige, width = 2)
    resourcesDisplay = s.create_rectangle(0, 400, 300, 600, fill = darkBeige, width = 2)
    centerDisplay = s.create_rectangle(300, 425, 700, 600, fill = lightBeige, width = 2)
    technologyDisplay = s.create_rectangle(700, 400, 1000, 600, fill = darkBeige, width = 2)
    
    resourcesHeader = s.create_rectangle(0, 400, 300, 450, fill = darkBeige, width = 2)
    goldDisplay = s.create_rectangle(0, 450, 300, 500, fill = mediumBeige, width = 2)
    foodDisplay = s.create_rectangle(0, 500, 300, 550, fill = mediumBeige, width = 2)
    naturalResourcesDisplay = s.create_rectangle(0, 550, 300, 600, fill = mediumBeige, width = 2)

    advancementHeader = s.create_rectangle(700, 400, 1000, 450, fill = darkBeige, width = 2)
    technologyDisplay = s.create_rectangle(700, 450, 1000, 500, fill = mediumBeige, width = 2)
    subjectDisplay = s.create_rectangle(700, 500, 1000, 550, fill = mediumBeige, width = 2)
    turnDisplay = s.create_rectangle(700, 550, 850, 600, fill = mediumBeige, width = 2)
    endTurnDisplay = s.create_rectangle(850, 550, 1000, 600, fill = "red", width = 2)

    resourcesHeaderText = s.create_text(150, 425, text = "Resources", fill = "black", font = "Courier 30")
    advancementHeader = s.create_text(850, 425, text = "Advancement", fill = "black", font = "Courier 30")
    endTurnText = s.create_text(925, 575, text = "End turn", fill = "black", font = "Courier 20")

    #empty objects
    occurenceText1 = s.create_rectangle(0, 0, 0, 0)
    occurenceText2 = s.create_rectangle(0, 0, 0, 0)
    occurenceText3 = s.create_rectangle(0, 0, 0, 0)
    showSelected = s.create_rectangle(0,0,0,0)
    cantAffordRectangle = s.create_rectangle(0,0,0,0)
    cantAffordText = s.create_rectangle(0,0,0,0)
    haventUnlockedText = s.create_rectangle(0,0,0,0)
    haventUnlockedRectangle = s.create_rectangle(0,0,0,0)

    texts = []
    rectangles = []

    #creating empty objects
    for i in range (0,100):
        rectangle = s.create_rectangle(0, 0, 0, 0)
        rectangles.append(rectangle)
    for i in range (0,100):
        text = s.create_rectangle(0, 0, 0, 0)
        texts.append(text)
	
def drawObjects():
    global turn, gold, food, naturalResources, population, maxPop, houses, houseX, houseY, houseImage
    global turnText, settlementText , populationText, goldText, foodText, naturalResourcesText, technologyText, subjectsText, turnText
    global subjects, displaySubject, subjectSelected, showSelected, occurencePassed, numHouses, houseImage
    global showSelected, text, rectangles, displayingSubjectTree, haventUnlocked, farmerUnlocked, lumberjackUnlocked
    global displayingSubjectTree, treeText, treeRectangles, lines, colours, cantAfford, cantAffordRectangle, cantAffordText, haventUnlockedText, haventUnlockedRectangle, haventUnlocked
    global houseDisplayText, buyHouseText
    #text for UI boxes
    if displayingTree == False and displayingSubjectTree == False:
##        if population <= 10:
##            settlementText = s.create_text(500, 18.25, text = "Group", fill = "black", font = "Courier 30")
##        else:
##            settlementText = s.create_text(500, 18.25, text = "Group", fill = "black", font = "Courier 30")
        houseDisplayText = s.create_text(400, 18.75, text = "Houses: " + str(numHouses), fill = "black", font = "Courier 20")
        buyHouseText = s.create_text(600, 18.75, text = """Buy House
(100 NR)""", fill = "black", font = "Courier 18")
        populationText = s.create_text(500, 56.25, text = "Population: " + str(population) + " / " + str(maxPop), fill = "black", font = "Courier 20")
        goldText = s.create_text(150, 475, text = "Gold: " + str(gold), fill = "black", font = "Courier 20")
        foodText = s.create_text(150, 525, text = "Food: " + str(food), fill = "black", font = "Courier 20")
        naturalResourcesText = s.create_text(150, 575, text = "Natural Resources: " + str(naturalResources), fill = "black", font = "Courier 20")
        technologyText = s.create_text(850, 475, text = "Technology", fill = "black", font = "Courier 20")
        subjectsText = s.create_text(850, 525, text = "Subjects", fill = "black", font = "Courier 20")
        turnText = s.create_text(775, 575, text = "Turn: " + str(turn), fill = "black", font = "Courier 20")
        #drawing subjects
        for i in range(0, numHouses):
            houses[i] = s.create_image(houseX[i], houseY[i], image = houseImage)
        for i in range(0, population):
            displaySubject[i] = s.create_image(subjects[i].x, subjects[i].y, image = subjects[i].image)
        #displaying subjects UI if subjects are clicked on           
        if subjectSelected == True and endingTurn == False and occurencePassed == False:
            showSelected = s.create_oval(subjects[subjectSelectedi].x-25, subjects[subjectSelectedi].y-25, subjects[subjectSelectedi].x+25, subjects[subjectSelectedi].y+25, outline ="red")
            rectangles[0] = s.create_rectangle(300, 425, 700, 475, fill = "beige", width = 2)
            texts[0] = s.create_text(500, 450, text = subjects[subjectSelectedi].name + " the " + subjects[subjectSelectedi].assignment, fill = "black", font = "Courier 20")
            rectangles[1] = s.create_rectangle(300, 475, 500, 600, fill = "beige", width = 2)
            rectangles[2] = s.create_rectangle(500, 475, 700, 600, fill = "beige", width = 2)
            if subjects[subjectSelectedi].assignment == "Hunter Gatherer":
                texts[1] = s.create_text(400, 537.5, text = "Age: " + str(subjects[subjectSelectedi].age) + """
net Food: -1
net Gold: 1
net NR: 0""", fill = "black", font = "Courier 20")
                rectangles[3] = s.create_rectangle(500, 475, 700, 537.5, fill = "grey", width = 2)
                rectangles[4] = s.create_rectangle(500, 537.5, 700, 600, fill = "grey", width = 2)
                if farmerUnlocked == True:
                    texts[2] = s.create_text(600, 506.25, text ="""Farmer
(25 gold)""", fill = "black", font = "Courier 20")
                else:
                    texts[2] = s.create_text(600, 506.25, text ="Locked", fill = "black", font = "Courier 20")
                if lumberjackUnlocked == True:
                    texts[3] = s.create_text(600, 568.75, text ="""LumberJack
(25 gold)""", fill = "black", font = "Courier 20")
                else:
                    texts[3] = s.create_text(600, 568.75, text ="Locked", fill = "black", font = "Courier 20")
                    
            if subjects[subjectSelectedi].assignment == "Farmer":
                texts[1] = s.create_text(400, 537.5, text = "Age: " + str(subjects[subjectSelectedi].age) + """
net Food: 2
net Gold: 2
net NR: 0""", fill = "black", font = "Courier 20")

            if subjects[subjectSelectedi].assignment == "Lumberjack":
                rectangles[3] = s.create_rectangle(500, 506.25, 700, 568.75 , fill = "beige", width = 2)

                texts[1] = s.create_text(400, 537.5, text = "Age: " + str(subjects[subjectSelectedi].age) + """
net Food: -1
net Gold: 2
net NR: 2""", fill = "black", font = "Courier 20")
                if minerUnlocked == True:
                    texts[2] = s.create_text(600, 537.5, text ="""Miner
(100 gold)""", fill = "black", font = "Courier 20")
                else:
                    texts[2] = s.create_text(600, 537.5, text ="Locked", fill = "black", font = "Courier 20")

            if subjects[subjectSelectedi].assignment == "Miner":
                rectangles[3] = s.create_rectangle(500, 506.25, 700, 568.75 , fill = "beige", width = 2)

                texts[1] = s.create_text(400, 537.5, text = "Age: " + str(subjects[subjectSelectedi].age) + """
net Food: -1
net Gold: 5
net NR: 5""", fill = "black", font = "Courier 20")


    #subjectsTechTree
    if displayingSubjectTree == True:
        treeRectangles[0] = s.create_rectangle(0, 0, 1000, 600, fill = "ivory2")
        lines[0] = s.create_line(250, 300, 500, 150)
        lines[1] = s.create_line(250, 300, 500, 450)
        lines[2] = s.create_line(500, 150, 700, 150)
        lines[3] = s.create_line(500, 450, 700, 450)
        treeRectangles[1] = s.create_rectangle(325, 350, 175, 250, fill = "PaleGreen1")
        treeRectangles[2] = s.create_rectangle(575, 200, 425, 100, fill = colours[2])
        treeRectangles[3] = s.create_rectangle(575, 500, 425, 400, fill = colours[3])
        treeRectangles[4] = s.create_rectangle(825, 200, 675, 100, fill = colours[4])
        treeRectangles[5] = s.create_rectangle(825, 500, 675, 400, fill = colours[5])
        treeText[0] = s.create_text(500, 550, text = "Press (q) to close window", fill = "black", font = "Courier 30") 
        treeText[1] = s.create_text(250, 300, text = """Hunter
Gatherer""", fill = "black", font = "Courier 18")
        treeText[2] = s.create_text(500, 150, text = """Farmer
(100 Gold)""", fill = "black", font = "Courier 18")
        treeText[3] = s.create_text(500, 450, text = """LumberJack
(100 Gold)""", fill = "black", font = "Courier 18")
        treeText[4] = s.create_text(750, 150, text = """Industrial
Farmer
(500 gold)""", fill = "black", font = "Courier 18")
        treeText[5] = s.create_text(750, 450, text = """Miner
(500 gold)""", fill = "black", font = "Courier 18")        

    #creating textboxes to tell users they can't by things                
    if cantAfford == True:
        cantAffordRectangle = s.create_rectangle(200, 10, 800, 90, fill = "white", width = 2)
        cantAffordText = s.create_text(500, 50, fill = "black", text = """Insufficent funds!
Press (c) to close""", font = "Courier 30")

    #creating boxes to tell users they haven't unlocked things
    if haventUnlocked == True:
        haventUnlockedRectangle = s.create_rectangle(200, 10, 800, 90, fill = "white", width = 2)
        haventUnlockedText = s.create_text(500, 50, fill = "black", text = """Haven't unlocked!
Press (c) to close""", font = "Courier 30")

       
def deleteObjects():
    #deleting objects 
    global turnText, settlementText , populationText, goldText, foodText, naturalResourcesText, technologyText, subjectsText, turnText
    global showSelected, text, rectangles, cantAffordRectangle, cantAffordText
    global houseDisplayText, buyHouseText
    
    s.delete(houseDisplayText, buyHouseText , populationText, goldText, foodText, naturalResourcesText, technologyText, subjectsText, turnText)

    for i in range(0, population):
        s.delete(displaySubject[i])
    for i in range(0, numHouses):
        s.delete(houses[i])
       
    if subjectSelected == True and endingTurn == False:
        s.delete(showSelected)
        for i in range(0,len(rectangles)):
            s.delete(rectangles[i])
        for i in range(0,len(texts)):
            s.delete(texts[i])

    if displayingSubjectTree == True:
        for i in range(100):
            s.delete(treeText[i])
            s.delete(treeRectangles[i], lines[i])
            
    if cantAfford == True:
        s.delete(cantAffordRectangle, cantAffordText)
        
    if haventUnlocked == True:
        s.delete(haventUnlockedRectangle, haventUnlockedText)

def updateObjects():
    #updating subjects
    for i in range(0, population):
        movement = randint(-2,2)
        x = randint(1,3)
        y = randint(1,3)
        if x == 1:
            subjects[i].x = subjects[i].x - movement
        if y == 1:
            subjects[i].y = subjects[i].y - movement
        if subjects[i].x > 990:
            subjects[i].x = subjects[i].x - 2
        if subjects[i].x < 0:
            subjects[i].x = subjects[i].x + 2
        if subjects[i].y > 360:
            subjects[i].y = subjects[i].y - 2
        if subjects[i].y < 275:
            subjects[i].y = subjects[i].y + 2
        collisions()

def collisions():
    #checking for collisions using distance formula
    for i in range(0, population-1):
        colliding = distanceBetweenPoints(subjects[i].x, subjects[i].y, subjects[i+1].x, subjects[i+1].y, 100)
        if colliding == True:
            if subjects[i].x > subjects[i+1].x:
                subjects[i].x = subjects[i].x + 2
                subjects[i].y = subjects[i].y + 2
                subjects[i+1].x = subjects[i+1].x - 2
                subjects[i+1].y = subjects[i+1].y - 2
            else:
                subjects[i].x = subjects[i].x - 2
                subjects[i].y = subjects[i].y - 2
                subjects[i+1].x = subjects[i+1].x + 2
                subjects[i+1].y = subjects[i+1].y + 2
                
def drawTechTree():
    #unfished Tech Tree
    global displayingTree
    x = 100
    y = 100
    rectangles = []
    s.create_rectangle(0, 0, 1000, 600, fill = "white")


    s.create_text(100, 100, text = "Medicine", fill = "black", font = "Courier 18")
    s.create_text(100, 300, text = "Fire", fill = "black", font = "Courier 18")
    s.create_text(100, 500, text = "Wheel", fill = "black", font = "Courier 18")
    
    s.create_text(300, 100, text = """Advanced
Medicine""", fill = "black", font = "Courier 18")
    s.create_text(300, 300, text = "Agriculture", fill = "black", font = "Courier 18")
    s.create_text(300, 500, text = "Electricity", fill = "black", font = "Courier 18")

    s.create_text(500, 100, text = """Universal
Healthcare""", fill = "black", font = "Courier 18")
    s.create_text(500, 500, text = "Motor", fill = "black", font = "Courier 18")

    s.create_text(700, 50, text = "Vaccines", fill = "black", font = "Courier 18")
    s.create_text(700, 150, text = "Antibiotices", fill = "black", font = "Courier 18")
    s.create_text(700, 400, text = "Industrialization", fill = "black", font = "Courier 18")
    displayingTree = True

def drawSubjectTree():
    #called to draw subject tree
    global displayingSubjectTree
    displayingSubjectTree = True

def hasLost():
    #checking if person has lost
    global play
    if food < 0:
        play = False

    if population < 0:
        play = False

def newTurn():
    #what happens when there is a new turn
    global turn, gold, food, naturalResources, population
    global yearsSinceIncreaseInPopulation
    global numFarmers, foodHarvestRate, numLumberjacks, resourceHarvestRate, occurrenceChance
    global populationIncreaseText, goldIncreaseText, foodIncreaseText, naturalResourcesIncreaseText, continueText
    global endingTurn, subjectSelected, displaySubjects
    global subjects, displaySubject, selected, subjectSelectedi, showSelected, subjectSelected, displaySubjects
    global occurrences, occurence, numFarmers, numLumberjacks, play, easy, medium, hard

    #deleting subjects display
    s.delete(showSelected)
    for i in range(0,len(rectangles)):
        s.delete(rectangles[i])
    for i in range(0,len(texts)):
        s.delete(texts[i])
        
    #resetting bool
    displaySubjects = False
    subjectSelected = False
    endingTurn = True

    #updating variables
    turn = turn + 1
    
    taxes = population * 1
    gold = gold + taxes + numFarmers + numMiners + numMiners * 2

    foodConsumption = population * 1
    foodHarvest = numFarmers * 3
    netFood = foodHarvest - foodConsumption
    food = food + netFood

    newPopulation = 0
    
    for i in range(population):
        subjects[i].age = subjects[i].age + 1
        
##    for q in range(1,population):
##        
##        if subjects[q].age > 16:
##                deathChance = randint(1,1)
##                if deathChance == 1:
##                    population = population - 1
##                    subjects.remove(subjects[q])
##                    displaySubject.remove(displaySubject[q])
                    
    populationChance = randint(1,1000)

    if populationChance == 1:
        newPopulation = newPopulation + 1
        yearsSinceIncreaseInPopulation = 0

    if newPopulation == 0:
        yearsSinceIncreaseInPopulation = yearsSinceIncreaseInPopulation + 1

    if yearsSinceIncreaseInPopulation == 10:
        newPopulation = 1
        yearsSinceIncreaseInPopulation = 0
        
    if population < maxPop:
        for i in range(0,newPopulation):
            life()
    
        population = population + newPopulation
    harvestedResources = numLumberjacks * 2 + numMiners * 5
    naturalResources = naturalResources + harvestedResources

    #creating the text
    populationIncreaseText = s.create_text(500, 450, text ="The civilization grew by " + str(newPopulation) + " subjects", fill = "black", font = "Courier 16")
    goldIncreaseText = s.create_text(500, 475, text = str(taxes) + " gold where collected in taxes", fill = "black", font = "Courier 16")
    if netFood > 0:
        foodIncreaseText = s.create_text(500, 500, text = "The civilization produced " + str(netFood) + " food", fill = "black", font = "Courier 16")
    else:
        foodIncreaseText = s.create_text(500, 500, text = "Consumed more food than harvested, lost " + str(netFood*-1) + " food", fill = "black", font = "Courier 14")
    naturalResourcesIncreaseText = s.create_text(500, 525, text = str(harvestedResources) + " natural resources where harvested" , fill = "black", font = "Courier 16")
    continueText = s.create_text(500, 550, text = "Press (Space) to continue" , fill = "black", font = "Courier 16")
    occurence = ""

    #chance of occurence goes up
    if turn < 5:
        occurrenceChance = randint(1,5)
    elif turn < 10:
        occurrenceChance = randint(1,4)
    else:
        occurrenceChance = randint(1,3)

    #setting occurrence
    if occurrenceChance == 1:
        i = randint(0, len(occurrences)-1)
        occurence = occurrences[i]
        #having a chance that detrimental occurances can turn ino postive ones if easy mode
        if easy == True:
            if occurence == "Famine":
                 i = randint(1,3)
                 if i == 1:
                     occurence = "Bountiful Harvest"
            if occurence == "Sickness":
                 i = randint(1,3)
                 if i == 1:
                     occurence = "Population Boom"
        #having a chance that helpful occurances can turn into negative ones if hard mode
        if hard == True:
            if occurence == "Bountiful Harvest":
                 i = randint(1,3)
                 if i == 1:
                     occurence = "Famine"
            if occurence == "Population Boom":
                 i = randint(1,3)
                 if i == 1:
                     occurence = "Sickness"

def mouseClickHandler( event ):
    global xMouse, yMouse, turn, easy, medium, hard, running, lumberjackBought, naturalResources
    global endingTurn, displayTree, displayingSubjectTree, displayingTitle, displayingInstructions, displayingDifficulty
    global displaySubjects, subjectSelected, subjectSelectedi, selected, gold, clicked, numHouses, maxPop
    global hgImages, lumberjackImages, farmerImages, numFarmers, numLumberjacks, colours, numMiners, houses, houseX, houseY
    global farmerUnlocked, lumberjackUnlocked, industrialFarmerUnlocked, minerUnlocked, cantAfford, haventUnlocked
    xMouse = event.x
    yMouse = event.y
    
    subjectClicked = []

    centerClicked= mouseInsideRectangle(300, 425, 700, 600)
    endTurnClicked = mouseInsideRectangle(850, 550, 1000, 600)
    technologyTreeClicked = mouseInsideRectangle(700, 450, 1000, 500)
    subjectTreeClicked = mouseInsideRectangle(700, 500, 1000, 550)
    farmerClicked = mouseInsideRectangle(500, 475, 700, 538)
    lumberjackClicked =  mouseInsideRectangle(500, 538, 700, 600)
    buyHouseClicked = mouseInsideRectangle(500, 0, 700, 38)
    
    #mouseclicks for title screen
    if displayingTitle == True:
        
        if mouseInsideRectangle(435, 250, 565, 300) == True:
            displayingTitle = False
            difficultyScreen()
            
        if mouseInsideRectangle(325, 350, 675, 400) == True:
            displayingTitle = False
            instructionScreen()
            
        if mouseInsideRectangle(440, 450, 560, 500) == True:
            root.destroy()
            
    elif displayingDifficulty == True:
        
        if mouseInsideRectangle(435, 150, 565, 200) == True:
            easy = True
            medium = False
            hard = False
            displayingDifficulty = False
            runGame()
            
        if mouseInsideRectangle(400, 250, 600, 300) == True:
            easy = False
            medium = True
            hard = False
            displayingDifficulty = False
            runGame()
            
        if mouseInsideRectangle(440, 350, 560, 400) == True:
            easy = False
            medium = False
            hard = True
            displayingDifficulty = False
            runGame()
            
    elif displayingInstructions == True:
        
        if mouseInsideRectangle(440, 350, 560, 400) == True:
            displayingInstructions = False
            titleScreen()

    #checking if clickinga subject or not and displaying its UI
    elif running == True:
        if buyHouseClicked == True and endingTurn == False:
            if naturalResources >= 100:
                naturalResources = naturalResources - 100
                numHouses = numHouses + 1
                maxPop = maxPop + 5
                houseX.append(randint(100, 900))
                houseY.append(randint(310, 360))
                houses.append(0)
            else:
                cantAfford = True
            
            
        if play == True:
            for i in range(0,population):
                subjectDistanceToMouse = distanceBetweenMouseAndPoint(subjects[i].x, subjects[i].y, 20)
                subjectClicked.append(subjectDistanceToMouse)

            
            for i in range(0,population):
                if subjectClicked[i] == True and displaySubjects == False:
                    displaySubjects = True
                    subjectSelected = True
                    subjectSelectedi = i
                    selected = i
                elif subjectClicked[i] == False and displaySubjects == False and centerClicked == False:
                    subjectSelected = False
                    s.delete(showSelected)
                    for i in range(0,len(rectangles)):
                        s.delete(rectangles[i])
                    for i in range(0,len(texts)):
                        s.delete(texts[i])

            for i in range(0,population):
                if subjectClicked[i] == True and displaySubjects == True:
                    displaySubjects = True
                    subjectSelected = True
                    subjectSelectedi = i
                    selected = i
                elif subjectClicked[i] == False and displaySubjects == True and centerClicked == False:
                    displaySubjects = False

            #upgrading subjects
            if subjects[selected].assignment == "Hunter Gatherer":
                
                if farmerClicked == True and subjectSelected == True:
                    if farmerUnlocked == True :          
                        if gold >= 25:
                            numFarmers = numFarmers + 1

                            subjects[selected].assignment = "Farmer"
                            gold = gold - 25
                            if subjects[selected].number == 5:
                                    subjects[selected].image = PhotoImage(file = "farmer5.gif")

                            for i in range(0,5):
                               if subjects[selected].number == i:
                                    subjects[selected].image = PhotoImage(file = farmerImages[i-1])
                        else:
                            cantAfford = True
                    else:
                        haventUnlocked = True

                
                if lumberjackClicked == True and subjectSelected == True:
                    if lumberjackUnlocked == True:
                        if gold >= 25:
                            numLumberjacks = numLumberjacks + 1
                            subjects[selected].assignment = "Lumberjack"
                            gold = gold - 25
                            if subjects[selected].number == 5:
                                    subjects[selected].image = PhotoImage(file = "lumberjack5.gif")
                            
                            for i in range(0,5):
                               if subjects[selected].number == i:
                                    subjects[selected].image = PhotoImage(file = lumberjackImages[i-1])
                            lumberjackBought = True
                            clicked = clicked + 1
                        else:
                           cantAfford = True
                    else:
                        haventUnlocked = True
                        
            if lumberjackBought == True:
                minerClicked = mouseInsideRectangle(500, 506, 700, 569)
                if subjects[selected].assignment == "Lumberjack":

                    if minerClicked == True and subjectSelected == True:
                        clicked = clicked + 1
                        if clicked < 2:
                            if minerUnlocked == True:
                                if gold >= 100:
                                    numMiners = numMiners + 1
                                    subjects[selected].assignment = "Miner"
                                    gold = gold - 100
                                    subjects[selected].image = PhotoImage(file = "Miner.gif")
                                else:
                                   cantAfford = True
                            else:
                                haventUnlocked = True
                        clicked = 0

            

                    

            #unlocking tech tree               
            endTurnClicked = mouseInsideRectangle(850, 550, 1000, 600)
            technologyTreeClicked = mouseInsideRectangle(700, 450, 1000, 500)
            subjectTreeClicked = mouseInsideRectangle(700, 500, 1000, 550)
            
            if endTurnClicked == True and endingTurn == False and occurencePassed == False:
                newTurn()

            if subjectTreeClicked == True and endingTurn == False:
                drawSubjectTree()
                
            inFarmer = mouseInsideRectangle(575, 200, 425, 100)
            inLumberJack = mouseInsideRectangle(575, 500, 425, 400)
            inIndustrialFarmer = mouseInsideRectangle(825, 200, 675, 100)
            inMiner = mouseInsideRectangle(825, 500, 675, 400)
            
            if displayingSubjectTree == True:
                if inFarmer == True and farmerUnlocked == False:
                    if gold >= 100:
                        gold = gold - 100
                        colours[2] = "PaleGreen1"
                        farmerUnlocked = True
                    else:
                        cantAfford = True
                        
                if inLumberJack == True and lumberjackUnlocked == False:
                    if gold >= 100:
                        gold = gold - 100
                        colours[3] = "PaleGreen1"
                        lumberjackUnlocked = True
                    else:
                        cantAfford = True

                if inIndustrialFarmer == True and industrialFarmerUnlocked == False and farmerUnlocked == True:
                    if gold >= 500:
                        gold = gold - 500
                        colours[4] = "PaleGreen"
                        industrialFarmerUnlocked = True
                    else:
                        cantAfford = True
                if inMiner == True and minerUnlocked == False and lumberjackUnlocked == True:
                    if gold >= 500:
                        gold = gold - 500
                        colours[5] = "PaleGreen1"
                        minerUnlocked = True
                    else:
                        cantAfford = True
            

def keyDownHandler( event ):
    global populationIncreaseText, goldIncreaseText, foodIncreaseText, naturalResourcesIncreaseText, continueText, occurenceText1, occurenceText2, occurenceText3
    global endingTurn, occurence, food, occurencePassed, subtractionVariable, population, displayingSubjectTree, treeRectangles, treeText
    global subjects, displaySubject, selected, subjectSelectedi, showSelected, subjectSelected, displaySubjects, lines, cantAfford, cantAffordText, cantAffordRectangle
    global  haventUnlockedRectangle, haventUnlockedText, haventUnlocked, gold, trade, trade2, occurenceVariable, variable
    #deletes subject tree   
    if event.keysym == "q" and displayingSubjectTree == True:
        displayingSubjectTree = False
        for i in range(100):
            s.delete(treeText[i])
            s.delete(treeRectangles[i], lines[i])
            s.delete(cantAffordText, cantAffordRectangle)
            cantAfford = False
            

    #interacting with occurances
    if event.keysym == "space" and endingTurn == True and play == True:
        
        s.delete(populationIncreaseText, goldIncreaseText, foodIncreaseText, naturalResourcesIncreaseText, continueText)
        if occurence == "Famine":
            if turn <= 10:
                occurenceVariable = randint(int(food/10), int(food/8))
            if turn > 10:
                occurenceVariable = randint(int(food/3), int(food/2))
            food = food - occurenceVariable
            occurenceText1 = s.create_text(500, 487.5, text = "A bad harvest resulted in a famine", fill = "black", font = "Courier 16")
            occurenceText2 = s.create_text(500, 512.5, text = str(occurenceVariable) + " food was lost", fill = "black", font = "Courier 16")
            occurenceText3 = s.create_text(500, 537.5, text = "Press (C) to continue", fill = "black", font = "Courier 16")
            occurencePassed = True
            endingTurn = False
            
        if occurence == "Bountiful Harvest":
            occurenceVariable = randint(int(food/10), int(food/8))
            food = food + occurenceVariable
            occurenceText1 = s.create_text(500, 487.5, text = "A bountiful harvest!", fill = "black", font = "Courier 16")
            occurenceText2 = s.create_text(500, 512.5, text = str(occurenceVariable) + " more food was harvested!", fill = "black", font = "Courier 16")
            occurenceText3 = s.create_text(500, 537.5, text = "Press (C) to continue", fill = "black", font = "Courier 16")
            occurencePassed = True
            endingTurn = False
            
        if occurence == "Sickness":
            if easy == True:
                if turn <= 10:
                    occurenceVariable = randint(int(population/11), int(population/10))
                if turn < 10:
                    occurenceVariable = randint(int(population/9), int(population/10))
            elif medium == True:
                if turn <= 10:
                    occurenceVariable = randint(int(population/10), int(population/9))
                if turn < 10:
                    occurenceVariable = randint(int(population/8), int(population/7))
            elif hard == True:
                if turn <= 10:
                    occurenceVariable = randint(int(population/8), int(population/7))
                if turn < 10:
                    occurenceVariable = randint(int(population/7), int(population/6))
            occurenceText1 = s.create_text(500, 487.5, text = "A terrible sickness fell upon the land", fill = "black", font = "Courier 16")
            if occurenceVariable == 0 or occurenceVariable == 1:
                occurenceVariable = 1
                occurenceText2 = s.create_text(500, 512.5, text = "1 subject died", fill = "black", font = "Courier 16")
            else:
                occurenceText2 = s.create_text(500, 512.5, text = str(occurenceVariable) + " subjects died", fill = "black", font = "Courier 16")
            occurenceText3 = s.create_text(500, 537.5, text = "Press (C) to continue", fill = "black", font = "Courier 16")
            population = population - occurenceVariable
            for i in range(0, occurenceVariable):
                death()
            occurencePassed = True
            endingTurn = False
            
        if population < maxPop:
            if occurence == "Population Boom":
                occurenceVariable = randint(int(population/11), int(population/10))
                occurenceText1 = s.create_text(500, 487.5, text = """There was a population boom!""", fill = "black", font = "Courier 16")
                if occurenceVariable == 0 or occurenceVariable == 1:
                    occurenceText2 = s.create_text(500, 512.5, text = "1 more subject joined the civilization", fill = "black", font = "Courier 16")
                    population = population + 1
                    life()
                else:
                    occurenceText2 = s.create_text(500, 512.5, text = str(occurenceVariable) + " subjects joined the civilization", fill = "black", font = "Courier 16")
                    population = population + occurenceVariable
                    for i in range(0, occurenceVariable):
                        life()
                occurenceText3 = s.create_text(500, 537.5, text = "Press (C) to continue", fill = "black", font = "Courier 16")
                occurencePassed = True
                endingTurn = False
            else:
                endingTurn = False
        else:
            endingTurn = False
            
        if occurence == "Trade":
            occurenceVariable = randint(0, gold)
            if occurenceVariable < food:
                occurenceVariable = randint(0, food)
            variable = occurenceVariable + randint(-10, 10)
            trade = randint(1,2)
            if trade == 1:
                trade = "gold"
            else:
                trade = "food"
            if trade == "gold":
                trade2 = "food"
            if trade == "food":
                trade2 = "gold"
            if variable < 0:
                variable = 10
            occurenceText1 = s.create_text(500, 487.5, text = """A neighbouring nation proposes a trade!""", fill = "black", font = "Courier 16")
            occurenceText2 = s.create_text(500, 512.5, text = str(occurenceVariable) + " " +trade + " for " + str(variable) + " " + trade2, fill = "black", font = "Courier 16")
            occurenceText3 = s.create_text(500, 537.5, text = "Yes (y) No (n) ", fill = "black", font = "Courier 16")
            occurencePassed = True
            endingTurn = False

    #deleting occurance texts
    if event.keysym == "c" and occurencePassed == True:
        s.delete(occurenceText1, occurenceText2, occurenceText3)
        occurencePassed = False

    if event.keysym == "n" and occurencePassed == True:
        s.delete(occurenceText1, occurenceText2, occurenceText3)
        occurencePassed = False

    if event.keysym == "y" and occurencePassed == True:
        if trade == "gold":
            gold = gold - occurenceVariable
            food = food + variable
        if trade == "food":
            gold = gold + occurenceVariable
            food = food - variable
        s.delete(occurenceText1, occurenceText2, occurenceText3)
        occurencePassed = False
        
    #deleting can't afford and unlocked displays
    if cantAfford == True and event.keysym == "c":
        s.delete(cantAffordText, cantAffordRectangle)
        cantAfford = False

    if haventUnlocked == True and event.keysym == "c":
        s.delete(haventUnlockedText, haventUnlockedRectangle)
        haventUnlocked = False

    #letting user play again
    if event.keysym == "p":
        difficultyScreen()
        
def endGame():
    #ending game
    for i in range(10):
        s.delete("all")
    s.create_text(500, 175, text="Your civilization crumbles away", font= "Times 30", anchor = N)
    s.create_text(500, 300, text="Total turns: " + str(turn), font= "Times 30", anchor = N)
    s.create_text(500, 425, text="Play Again (P)", font= "Times 30", anchor = N)
        

def titleScreen():
    #creating title screen
    global displayingTitle, titleImage, displayingDifficulty, displayingInstructions, running
    s.delete("all")
    
    displayingTitle = True
    displayingDifficulty = False
    displayingInstructions = False
    running = False


    s.create_rectangle(50, 150, 950, 90)
    s.create_text(500, 120, text = "Cradle of Civilization", font="Courier 50")
    
    s.create_rectangle(435, 233, 565, 273)
    s.create_text(500, 253, text = "Play", font="Courier 35")
    
    s.create_rectangle(325, 333, 675, 373)
    s.create_text(500, 353, text = "Instructions", font="Courier 35")
    
    s.create_rectangle(440, 433, 560, 473)
    s.create_text(500, 453, text = "Quit", font="Courier 35")

    s.update()

def difficultyScreen():
    global displayingDifficulty
    s.delete("all")

    displayingDifficulty = True

    s.create_rectangle(435, 150, 565, 200)
    s.create_text(500, 153, text = "Easy", font="Courier 35", anchor = N)
    
    s.create_rectangle(400, 250, 600, 300)
    s.create_text(500, 253, text = "Medium", font="Courier 35", anchor = N)
    
    s.create_rectangle(440, 350, 560, 400)
    s.create_text(500, 353, text = "Hard", font="Courier 35", anchor = N)

def instructionScreen():
    #instructions
    global displayingInstructions
    s.delete("all")
    displayingInstructions = True
    s.create_rectangle(440, 350, 560, 400)
    s.create_text(500, 150, text = """Click on subjects to select them.
Once selected they can be upgraded to certain classes.
You can unlock classes through the subject tree.
Each class consumes and produces different resources.
After finishing all your desired actions for the turn,
click the end turn button on the bottom right.
At the end of the turn,
each of your subjects will produce and consume resources based on their class.
Events may appear at the end of a turn, use your keyboard to interact with them.""", font="Courier 18", anchor = N)

    s.create_text(500, 353, text = "Back", font="Courier 35", anchor = N)

#running game
def runGame():
    s.delete("all")
    setInitialValues()
    drawOnce()
    while play == True:
        hasLost()
        drawObjects()
        updateObjects()
        collisions()
        sleep(0.1)
        s.update()
        deleteObjects()
    endGame()

#binding keys        
root.after( 500, titleScreen )
s.bind( "<Button-1>", mouseClickHandler )
s.bind( "<Key>", keyDownHandler )
s.pack()
s.focus_set()
root.mainloop()

