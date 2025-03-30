import turtle
import math

turtle.screensize(canvwidth=400, canvheight=300)

def instructions():
    print("Instructions:","\n")
    print("1. Make sure to have Thonny and the turtle window side by side as a split screen.","\n")
    print("2. When the program asks you to enter location:")
    print("   a. if you would like to enter an answer to a clue, enter the letter of the clue.")
    print("   b. if you would like to enter a letter directly into the grid, enter the number of the box.","\n")
    print("3. To clear a clue or a box, type the location you want to clear, hit enter, and then hit enter again without typing any letters.","\n")
    print("4. If you would like to experience the animation, place a hashtag in front of lines 18, 20, and 42: turtle.tracer(0,0), t.hideturtle(), and x.hideturtle(), and rerun the program.","\n")
    print("5. Once you have completed the puzzle, type 'stop' to reveal the clue answers and the overall quote.","\n")
    print("6. If you click on the turtle window and it freezes, just hit enter a couple times in the Shell (the bottom panel) and it will unfreeze.","\n")
    print("7. If you would like to see the instructions again, type 'instructions' and they will pop up.","\n\n")

turtle.tracer(0,0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
coords = dict()

tA = turtle.Turtle()
tB = turtle.Turtle()
tC = turtle.Turtle()
tD = turtle.Turtle()
tE = turtle.Turtle()
tF = turtle.Turtle()
tG = turtle.Turtle()
tH = turtle.Turtle()
tI = turtle.Turtle()
tJ = turtle.Turtle()
tK = turtle.Turtle()
tL = turtle.Turtle()
tM = turtle.Turtle()
tN = turtle.Turtle()
tO = turtle.Turtle()
tLst = [tA,tB,tC,tD,tE,tF,tG,tH,tI,tJ,tK,tL,tM,tN,tO]

for turt in tLst:
    turt.hideturtle()
    turt.up()
    turt.goto(400,-300)
    turt.down()

def displayCross(numRows, numColumns, listClueLetters, ans):
    t.up()
    t.goto(-1 * 15 * numColumns, 15 * numColumns)
    t.down()
    for i in range(2):
        t.fd(30 * numColumns)
        t.right(90)
        t.fd(30 * numRows)
        t.right(90)
    count = 1
    for i in range(numRows):
        t.up()
        t.goto(-1 * 15 * numColumns, (15 * numColumns) - (i * 30))
        t.down()
        for j in range(numColumns * i, numColumns * (i + 1)):
            t.up()
            t.fd(5)
            t.right(90)
            t.fd(10)
            coords[str(count)] = t.pos()
            t.write(str(count), font=("Verdana", 6, "normal"))
            count2 = 0
            t.right(90)
            t.fd(10)
            for k in vLst:
                if count in k:
                    t.write("         " + chr(ord("A") + count2),font=("Verdana", 6, "normal"))
                count2 += 1
            t.bk(10)
            t.left(90)
            t.bk(10)
            t.left(90)
            t.bk(5)
            t.down()
            if ans[j] == " ":
                t.fillcolor("Black")
                t.begin_fill()
                for k in range(4):
                    t.fd(30)
                    t.right(90)
                t.end_fill()
                t.up()
                t.fd(30)
                t.down()
            else:
                count += 1
                for k in range(4):
                    t.fd(30)
                    t.right(90)
                t.up()
                t.fd(30)
                t.down()
    turtle.update()
    return([-1 * 15 * numColumns, (15 * numColumns) - ((numRows + 1) * 30)])
       
def createClues(startx, starty, clueList, valueList, ans):
    t.up()
    t.goto(startx, starty)
    t.bk(20)
    t.left(90)
    t.fd(5)
    t.right(90)
    columnCount = 1
    for i in range(len(clueList)):
        letter = chr(ord("A") + i)
        t.write(letter,font=("Verdana", 9, "normal"))
        t.write("  .",font=("Verdana", 9, "normal"))
        t.fd(24)
        for section in splitClue(clueList[i]):
            t.write(section,font=("Verdana", 9, "normal"))
            t.right(90)
            t.fd(14)
            t.left(90)
        coords[letter] = t.pos()
        count = 1
        for j in valueList[i]:
            count += 1
            t.write("___",font=("Verdana", 7, "normal"))
            t.right(65 + (8 * numDigits(j)))
            t.fd(10 * math.sqrt(2))
            t.left(65 + (8 * numDigits(j)))
            t.write(j,font=("Verdana", 9, "normal"))
            t.left(115 - (8 * numDigits(j)))
            t.fd(10 * math.sqrt(2))
            t.right(115 - (8 * numDigits(j)))
            t.fd(24)
            if count == 9 and len(valueList[i]) > 9:
                t.right(180)
                t.fd(24 * (count - 1))
                t.left(90)
                t.fd(30)
                t.left(90)
                count = 1
        t.right(180)
        t.fd(24 * count)
        t.left(90)
        t.fd(34)
        t.left(90)
        if t.ycor() < -270:
            if columnCount == 1:
                t.goto(-110,65)
                columnCount += 1
            else:
                t.goto(113,65)

def splitClue(clue):
    wordList = clue.split()
    listedClue = []
    while wordList != []:
        cloozer = ""
        while len(cloozer) < 24 and wordList != []:
            cloozer += wordList[0] + " "
            wordList = wordList[1:]
        listedClue.append(cloozer)
    for i in range(len(listedClue)):
        if listedClue[i][0] == " ":
            listedClue[i] = listedClue[i][1:]
    return(listedClue)

def numDigits(n):
    digits = 0
    while n != 0:
        n = n // 10
        digits += 1
    return(digits)

# ----------------------------------------------------------------
# WARNING - IF YOU SCROLL FURTHER, YOU WILL RECEIVE SPOILERS!!!
# WARNING - READ THE WARNING ABOVE
# ----------------------------------------------------------------

































































# don't say I didn't warn you



















# <(°)

quote = "When I was there on those big nights there was nothing like it Every time I walk into the Garden theres just this energy and for me everything always comes back to the Garden  "
lst = []
for char in quote:
    lst.append(char.upper())

clueLst = ["It's considered the oldest city in the world",
           "Pretentious in speech",
           "Leda and the Swan, e.g.",
           "Jersey number worn by Michael Jordan, David Beckham, Don Mattingly, and others (Hyph.)",
           "Margaret Wise Brown classic (2 wds.)",
           "Its newspaper is named for a shade of red",
           "Prickly plant with purple flowers",
           "Marbled cut also known as entrecôte (2 wds.)",
           "Dora the Explorer catchphrase",
           "Song featuring Rooster in a 1982 film (2 wds.)",
           "Sémillon, e.g. (2 wds.)",
           "Travelocity listings",
           "Forest wardens",
           "One who feels (2 wds.)",
           "Fighting garden invaders, maybe (2 wds.)"]

vLst = [[84, 3, 109, 90, 122, 10, 68],
        [79, 60, 26, 134, 101, 36, 45, 85, 67, 113, 141],
        [96, 74, 11, 135, 47, 58, 110, 69, 2],
        [56, 6, 76, 38, 88, 97, 28, 17, 54, 105, 13],
        [23, 132, 102, 100, 15, 42, 115, 70, 30, 124, 39, 14, 99],
        [31, 73, 81, 52, 62, 138, 75],
        [9, 41, 65, 8, 131, 63, 34, 19],
        [33, 22, 127, 59, 120, 51, 37, 111, 94, 128, 64],
        [107, 119, 104, 98, 24, 18, 83],
        [48, 116, 29, 55, 86, 16, 95, 53, 125, 40],
        [1, 89, 49, 78, 20, 118, 46, 66, 106],
        [27, 123, 133, 71, 117, 91],
        [12, 137, 93, 44, 140, 103, 126],
        [121, 80, 4, 87, 25, 92, 77, 50, 21, 82, 57, 43, 136],
        [35, 108, 32, 139, 61, 112, 7, 129, 130, 5, 114, 72]]

ansLst = ["A. JERICHO", "B. HIGHFALUTIN", "C. GREEKMYTH", "D. TWENTYTHREE", "E. GOODNIGHTMOON", "F. HARVARD", "G. THISTLES", "H. RIBEYESTEAK", "I. VAMANOS", "J. EASYSTREET", "K. WHITEWINE", "L. HOTELS", "M. RANGERS", "N. SENTIENTBEING", "O. WEEDWHACKING"] 

instructions()

x = displayCross(8, 22, 0, lst)

createClues(x[0],x[1],clueLst,vLst,lst)

t.hideturtle()
turtle.update()

while True:
    location = input("Enter location: ").upper()
    if location == "STOP":
        for ans in ansLst:
            print(ans)
        print("\n")
        print(quote)
        print("-- Adam Fox")
        break
    if location == "INSTRUCTIONS":
        print("\n\n")
        instructions()
    if location == "up up down down left right left right b a start":
        print("Most definitely not a legal answer. Try again.","\n")
        turtle.update()
        continue
    if location not in "ABCDEFGHIJKLMNO" and location.isalpha():
            print("Location not found. Try again.","\n")
            turtle.update
            continue
    if location.isnumeric() and int(location) > 141:
            print("Location not found. Try again.","\n")
            turtle.update()
            continue
    if len(location) > 1 and location.isalpha():
            print("Location not found. Try again.","\n")
            turtle.update()
            continue
    if not (location.isalpha() or location.isnumeric()):
        print("Location not found. Try again.","\n")
        turtle.update()
        continue
    ans = input("Enter letter(s): ").upper()
    turtle.update()
    if location.isalpha():
        location = location.upper()
        vLstVal = ord(location.upper()) - ord("A")
        x = tLst[vLstVal]
        x.up()
        if len(ans) > len(vLst[vLstVal]):
            print("Answer is too long. Try again.","\n")
            turtle.update()
            continue
        if ans == "":
            print("\n")
            x.clear()
            turtle.update()
            continue
        if not ans.isalpha():
            print("Input not a letter. Try again.","\n")
            turtle.update()
            continue
        x.clear()
        x.goto(coords[location])
        x.fd(4)
        long = 1
        if len(ans) > 9:
            long = 2
        newString = ""
        for char in ans:
            newString += char + "  "
        if len(vLst[vLstVal]) == 9:
            for i in range(long):
                x.write(newString[:27],font=("Courier", 10, "normal"))
                x.right(90)
                x.fd(30)
                x.left(90)
                newString = newString[27:]
                turtle.update()
        else:
            long = 2
            for i in range(long):
                x.write(newString[:24],font=("Courier", 10, "normal"))
                x.right(90)
                x.fd(30)
                x.left(90)
                newString = newString[24:]
                turtle.update()
        for j in range(len(ans)):
            x.goto(coords[str(vLst[vLstVal][j])])
            x.fd(7)
            x.right(90)
            x.fd(18)
            x.left(90)
            x.write(ans[j],font=("Courier", 17, "normal"))
            turtle.update()
    if location.isnumeric():
        if len(ans) > 1:
            print("Entry too long. Try again.","\n")
            turtle.update()
            continue
        if not ans.isalpha() and ans != "":
            print("Input not a letter. Try again.","\n")
            turtle.update()
            continue
        for k in range(len(vLst)):
            if int(location) in vLst[k]:
                x = tLst[k]
                y = k
        x.up()
        x.goto(coords[location])
        x.bk(4)
        x.fillcolor("white")
        x.begin_fill()
        x.left(90)
        x.fd(2)
        x.right(90)
        for i in range(2):
            x.fd(28)
            x.right(90)
            x.fd(18)
            x.right(90)
        x.end_fill()
        x.fd(8)
        x.right(90)
        x.fd(22)
        x.left(90)
        x.write(ans,font=("Courier", 17, "normal"))
        x.goto(coords[chr(ord("A") + y)])
        for m in range(len(vLst[y])):
            if int(location) == vLst[y][m]:
                letNum = m
                break
        if m <= 7 or (m == 8 and len(vLst[y]) == 9):
            x.fd(24 * m + 4)
        else:
            x.right(90)
            x.fd(30)
            x.left(90)
            x.fd(24 * (m - 8) + 4)
        x.left(90)
        x.fd(1)
        x.right(90)
        x.fillcolor("white")
        x.begin_fill()
        x.circle(8,360)
        x.end_fill()
        turtle.update()
        x.write(ans,font=("Courier", 10, "normal"))
        turtle.update()
    turtle.update()
    print("\n")

